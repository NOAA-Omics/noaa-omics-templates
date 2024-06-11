import os
import gspread
import gspread_formatting as gf
from gspread.utils import rowcol_to_a1
import pandas as pd
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
from openpyxl import load_workbook

# Load environment variables
load_dotenv()

# Set up paths and credentials for Google API
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS").replace('\\', '/')
mimarks_file_path = os.getenv("MIMARKS_FILE_PATH")
study_template_dict_sheet_id = os.getenv("STUDY_TEMPLATE_DICT_SHEET_ID")
new_template_id = os.getenv("NEW_TEMPLATE_ID")

# Define the scopes for Google API
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Authenticate with Google using the credentials file
creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
client = gspread.authorize(creds)

def get_mimarks_terms(mimarks_file_path):
    print('Getting MIMARKS terms from downloaded package...')
    # Load the MIMARKS Excel file using openpyxl to get comments
    wb = load_workbook(mimarks_file_path, data_only=True)
    ws = wb.active

    # Create a dictionary with column names as keys and comments as values
    mimarks_terms_with_comments = {}

    # Iterate through the columns in row 12 (0-indexed 11) to get comments
    for col in range(1, ws.max_column + 1):
        cell = ws.cell(row=12, column=col)
        term = cell.value
        comment = cell.comment.text if cell.comment else None
        mimarks_terms_with_comments[term] = comment

    # Print the dictionary to verify
    for term, comment in mimarks_terms_with_comments.items():
        print(f"Term: {term}, Comment: {comment}")

    return mimarks_terms_with_comments

def get_aoml_darwincore_terms(study_template_dict_sheet_id):
    """Function to get AOML and DarwinCore terms from the study-data-template-dict Google Sheet, ex. terms where the 'sheet' column contains only 'sample_data'"""
    study_template_dict_sheet = client.open_by_key(study_template_dict_sheet_id)
    study_template_dict = study_template_dict_sheet.worksheet('study-data-templates')
    
    # Load the sheet data into a DataFrame, starting from row 2 to get the correct headers
    data = study_template_dict.get_all_values()
    headers = data[1]  # 2nd row as headers
    study_template_dict_df = pd.DataFrame(data[2:], columns=headers)  # Data starts from row 3

    # Rows where'sheet' column conntains 'sample_data'
    filtered_data = study_template_dict_df[study_template_dict_df['sheet'] == 'sample_data']

    # Grab all row 'name's (1st column) that were found above ^
    aoml_darwincore_terms = filtered_data.iloc[:, 0].tolist() 

    print("printing aoml and darwincore terms from study-data-template-dict google sheet:")
    print(aoml_darwincore_terms)
    
    return aoml_darwincore_terms

def column_letter(col_idx):
    """Convert a column index into a column letter (1-indexed)."""
    string = ""
    while col_idx > 0:
        col_idx, remainder = divmod(col_idx - 1, 26) #26 for alphabet length
        string = chr(65 + remainder) + string #65 is ASCII For A
    return string

def edit_template(mimarks_terms_with_comments, new_template_id, study_template_dict_sheet_id):
    new_sheet = client.open_by_key(new_template_id)
    sediment_sample_data = new_sheet.worksheet('sediment_sample_data')

    existing_terms = sediment_sample_data.row_values(9)
    core_terms = existing_terms[:-2]
    dm_mb = existing_terms[-2:]

    valid_terms = {term.replace('*', '').strip() for term in mimarks_terms_with_comments.keys()}
    valid_terms.update(get_aoml_darwincore_terms(study_template_dict_sheet_id))
    terms_to_delete = [term for term in core_terms if term not in valid_terms]
    terms_to_add = [term for term, comment in mimarks_terms_with_comments.items() if term.replace('*', '').strip() not in core_terms]

    for term in reversed(terms_to_delete):
        col_index = core_terms.index(term) + 1
        sediment_sample_data.delete_columns(col_index)
        core_terms.remove(term)

    updated_terms = core_terms + terms_to_add + dm_mb
    print("Total terms after update (including dm and mb):", len(updated_terms))

    end_col_letter = column_letter(len(updated_terms))
    range_to_update = f'A9:{end_col_letter}9'
    print("Range to update:", range_to_update)

    sediment_sample_data.update(range_name=range_to_update, values=[updated_terms])

    for i, term in enumerate(updated_terms, start=1):
        if '*' in term:
            cell = gspread.utils.rowcol_to_a1(9, i)
            gf.format_cell(sediment_sample_data, cell, gf.cellFormat(backgroundColor=gf.Color(0.0, 1.0, 0.0)))


def pause_for_user(message):
    """ Pause the script to allow user to check the current step manually """
    input(f"{message} Press Enter to continue...")

if __name__ == "__main__":
    mimarks_terms_with_comments = get_mimarks_terms(mimarks_file_path)
    edit_template(mimarks_terms_with_comments, new_template_id, study_template_dict_sheet_id)
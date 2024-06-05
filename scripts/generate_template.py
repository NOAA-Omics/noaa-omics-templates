import os
import gspread
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

def edit_template(mimarks_terms_with_comments, new_template_id, study_template_dict_sheet_id):
    new_sheet = client.open_by_key(new_template_id)
    sediment_sample_data = new_sheet.worksheet('sediment_sample_data')
    
    # Get current terms from row 9
    existing_terms = sediment_sample_data.row_values(9)
    num_columns = sediment_sample_data.col_count

    # Locate the position of the 'date_modified' and 'modified_by' columns to know where to insert new terms
    try:
        date_modified_index = existing_terms.index('date_modified') + 1
        modified_by_index = existing_terms.index('modified_by') + 1
    except ValueError:
        # If not found, assume they should be at the very end
        date_modified_index = num_columns + 1
        modified_by_index = num_columns + 2

    # Remove these special columns
    indices_to_remove = sorted([date_modified_index, modified_by_index], reverse=True)
    for index in indices_to_remove:
        sediment_sample_data.delete_columns(index)

    # Refresh existing terms and their counts after deletion
    existing_terms = sediment_sample_data.row_values(9)
    num_columns = len(existing_terms)

    # Define valid terms (MIMARKS + AOML/DWC)
    valid_terms = {term.replace('*', '').strip() for term in mimarks_terms_with_comments.keys()}
    valid_terms.update(get_aoml_darwincore_terms(study_template_dict_sheet_id))

    # Remove outdated terms
    columns_to_delete = [i for i, term in enumerate(existing_terms, start=1) if term not in valid_terms]
    for col_index in reversed(columns_to_delete):
        sediment_sample_data.delete_columns(col_index)

    # Refresh terms and column count after deletions
    existing_terms = sediment_sample_data.row_values(9)
    insert_index = len(existing_terms) + 1

    # Insert new terms at the correct position (before the previous 'date_modified')
    for term, comment in mimarks_terms_with_comments.items():
        cleaned_term = term.replace('*', '').strip()
        if cleaned_term not in existing_terms:
            values = [[cleaned_term]]
            sediment_sample_data.insert_cols(values, insert_index)
            insert_index += 1  # Update insert_index to keep appending next new columns correctly

    # Re-add 'date_modified' and 'modified_by' at the correct positions
    sediment_sample_data.insert_cols([['date_modified']], insert_index)
    sediment_sample_data.insert_cols([['modified_by']], insert_index + 1)




def pause_for_user(message):
    """ Pause the script to allow user to check the current step manually """
    input(f"{message} Press Enter to continue...")

if __name__ == "__main__":
    mimarks_terms_with_comments = get_mimarks_terms(mimarks_file_path)
    edit_template(mimarks_terms_with_comments, new_template_id, study_template_dict_sheet_id)

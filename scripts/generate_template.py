import os
import re
import gspread
import gspread_formatting as gf
from gspread_formatting import *
from gspread.utils import rowcol_to_a1
import pandas as pd
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
from openpyxl import load_workbook

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '..', 'script-dependencies', '.env')
load_dotenv(dotenv_path=env_path)

# Copy and paste the name of your Google Sheets API credentials file
credentials_filename = 'data-templates-c7159dc891a7.json' # EDIT ME
credentials_path = os.path.join(os.path.dirname(os.path.realpath(env_path)), credentials_filename)

# Copy and paste MIMARKS package Excel filename
mimarks_filename = 'MIMARKS.survey.sediment.6.0.xlsx' # EDIT ME
mimarks_file_path = os.path.join(os.path.dirname(os.path.realpath(env_path)), mimarks_filename)

# Get Google Sheet IDs from .env file
study_template_dict_sheet_id = os.getenv("STUDY_TEMPLATE_DICT_SHEET_ID")
new_template_id = os.getenv("NEW_TEMPLATE_ID")

#Alternatively, you can directly insert the Google Sheet IDs here instead:
#study_template_dict_sheet_id = "" #EDIT ME
#new_template_id = "" #EDIT ME

# Define scopes for Google API
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Authenticate with Google using the credentials file
creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
client = gspread.authorize(creds)

def get_mimarks_terms(mimarks_file_path):
    """Function to get all terms and their comments from the latest MIMARKs package"""
    print('\n----------------------------------------------')
    print('Getting MIMARKS terms from latest package...')
    
	# Load the MIMARKS Excel file using openpyxl to get comments
    wb = load_workbook(mimarks_file_path, data_only=True)
    ws = wb.active

    # Dictionary with term name as keys and comments as values
    mimarks_terms_with_comments = {}

    print("\nEnter the row number that contains the term names.")
    choice = int(input("Enter row number. Most MIMARKs packages have terms in row 12, or sometimes 13: "))

    # Iterate through the columns to get comments
    for col in range(1, ws.max_column + 1):
        cell = ws.cell(row=choice, column=col)
        term = cell.value
        comment = cell.comment.text if cell.comment else None
        mimarks_terms_with_comments[term] = comment

    # Print the dictionary to verify
    print('\n------------MIMARKS package terms--------------')
    print('Printing MIMARKs Terms with their Comments')
    print('\n')
    for term, comment in mimarks_terms_with_comments.items():
        print(f"{term}:, {comment}")
    print('\n----------------------------------------------')
    
    return mimarks_terms_with_comments

def get_aoml_darwincore_terms(study_template_dict_sheet_id):
    """Function to get AOML and DarwinCore terms from the study-data-template-dict Google Sheet"""
    print('\n----------------------------------------------')
    print('\nLoading data dictionary...')
    
	#Preparing to read Google Sheet
    study_template_dict_sheet = client.open_by_key(study_template_dict_sheet_id)
    study_template_dict = study_template_dict_sheet.worksheet('study-data-templates')
    
    # Load the sheet data into a DataFrame, starting from row 2 to get the correct headers
    data = study_template_dict.get_all_values()
    
    print("\nGoogle Sheet loaded. Getting terms...")

    headers = data[1]  # Term names in row 2
    study_template_dict_df = pd.DataFrame(data[2:], columns=headers)  # Data starts from row 3

	# Regex to match all 'sheet' column values that CONTAIN sample_data
    pattern = r'\b(sample_data)\b'

    # Rows where 'sheet' column contains 'sample_data'
    filtered_data = study_template_dict_df[study_template_dict_df['sheet'].str.contains(pattern, na=False, regex=True)]

    # Grab all row 'name's (1st column) that were found above ^
    aoml_darwincore_terms = filtered_data.iloc[:, 0].tolist()

    print('\n------------AOML + DarwinCore Terms--------------')
    print(aoml_darwincore_terms)
    print('-------------------------------------------------')
    
    return aoml_darwincore_terms

def column_letter(col_idx):
    """Code utility function. Convert a column index into a column letter (1-indexed)."""
    string = ""
    while col_idx > 0:
        col_idx, remainder = divmod(col_idx - 1, 26) #26 for alphabet length
        string = chr(65 + remainder) + string #65 is ASCII For A
    return string

def edit_template(mimarks_terms_with_comments, new_template_id, study_template_dict_sheet_id):
    """Creates a new data template based off a previous one. """
    new_sheet = client.open_by_key(new_template_id)
    print('\n----------------------------------------------')
    data_template_type = input("Enter name of new data template type, i.e.: sediment, water, soil: ")
    sample_data_sheetname = data_template_type + '_sample_data'
    sample_data = new_sheet.worksheet(sample_data_sheetname)

	# Extra work done to move date_modified and modified_by columns to the end, after adding new terms
	# date_modified = dm, and modified_by = mb, in terms of the code
    existing_terms = sample_data.row_values(9)
    core_terms = existing_terms[:-2]
    dm_mb = existing_terms[-2:]
    
	# Temporarily remove '*' from term names for operations, but retain them for future use
    valid_terms = {term.replace('*', '').strip() for term in mimarks_terms_with_comments.keys()}
    valid_terms.update(get_aoml_darwincore_terms(study_template_dict_sheet_id))
    terms_to_delete = [term for term in core_terms if term not in valid_terms]
    terms_to_add = [term for term, comment in mimarks_terms_with_comments.items() if term.replace('*', '').strip() not in core_terms]
    
    print('\nTerms to add to data template: ')
    print(terms_to_add)
    print('\nTerms to be deleted from data template: ')
    print(terms_to_delete)
    
    new_MIMARKS_terms_with_comments = {term.replace('*', '').strip(): comment for term, comment in mimarks_terms_with_comments.items() if term.replace('*', '').strip() not in core_terms}
    print("\nNew terms to be added: ")
    for term in new_MIMARKS_terms_with_comments.items():
        print(f"{term}")
    
    for term in reversed(terms_to_delete):
        col_index = core_terms.index(term) + 1
        sample_data.delete_columns(col_index)
        core_terms.remove(term)

	# list_of_terms is used in the update_data_dictionary function to update new and old terms
    list_of_terms = core_terms + [term.replace('*', '').strip() for term in terms_to_add]
    
    updated_terms = core_terms + [term.replace('*', '').strip() for term in terms_to_add] + dm_mb
    # print("\nTotal terms after update (including date_modified and modified_by):", len(updated_terms))

    end_col_letter = column_letter(len(updated_terms))
    range_to_update = f'A9:{end_col_letter}9'
    # print("\nRange to update:", range_to_update)

    sample_data.update(range_name=range_to_update, values=[updated_terms])

	# Section below is to add associated comment to each term
    requests = []
    format_requests = []  # This will store formatting requests
    for i, term in enumerate(updated_terms, start=1):
        original_term = core_terms + terms_to_add + dm_mb
        cell = rowcol_to_a1(9, i)
        actual_term = original_term[i-1]
        if actual_term in terms_to_add:
            # Add comment to the cell
            comment = mimarks_terms_with_comments.get(actual_term, '')
            if comment:
                requests.append({
                    "updateCells": {
                        "range": {
                            "sheetId": sample_data.id,
                            "startRowIndex": 8,
                            "endRowIndex": 9,
                            "startColumnIndex": i-1,
                            "endColumnIndex": i
                        },
                        "rows": [{
                            "values": [{
                                "note": comment
                            }]
                        }],
                        "fields": "note"
                    }
                })

            # Determine the background color based on the presence of '*'
            if actual_term.startswith('*'):
                bgcolor = Color(0.0, 1.0, 0.0)  # Google sheets Green
            else:
                bgcolor = Color(1.0, 1.0, 0.0)  # Google Sheets yellow

            format_requests.append((cell, CellFormat(backgroundColor=bgcolor)))

    # Execute all requests in one batch update to avoid multiple API calls
    if requests:
        new_sheet.batch_update({'requests': requests})

    # Apply all formatting requests
    if format_requests:
        format_cell_ranges(sample_data, format_requests)

    print("\nGoogle Sheet data template editing complete.")
    print('----------------------------------------------')
    
    return(sample_data_sheetname, new_MIMARKS_terms_with_comments, list_of_terms)

def update_data_dictionary(sample_data_sheetname, new_MIMARKS_terms_with_comments, study_template_dict_sheet_id, list_of_terms):
    """Function to add new terms to data dictionary, and update the 'sheet' column for existing terms"""
    print('----------------------------------------------')
    print('Loading study-data-template-dict Google sheet...')
	# Establish connection to the Google Sheets document
    study_sheet = client.open_by_key(study_template_dict_sheet_id)
    study_template_dict = study_sheet.worksheet('study-data-templates')

    # Fetch AOML and DarwinCore terms to exclude
    aoml_darwincore_terms = get_aoml_darwincore_terms(study_template_dict_sheet_id)
    
    print('\nMaking updates to study-data-template-dict...')

    # Remove AOML/DarwinCore terms and new MIMARKS terms from the list_of_terms
    filtered_terms = [term for term in list_of_terms if term not in aoml_darwincore_terms and term not in new_MIMARKS_terms_with_comments.keys()]

    # Fetch current data to DataFrame for easier manipulation
    data = study_template_dict.get_all_values()
    if data:  # Check if data is not empty
        headers = data[1]  # Assuming the second row contains headers
        df = pd.DataFrame(data[2:], columns=headers)  # Data starts from the third row

        # Trim whitespace from column headers to avoid issues
        df.columns = df.columns.str.strip()

        # Update 'sheet' column for terms that need updating
        updated = False
        for index, row in df.iterrows():
            if row['name'] in filtered_terms and sample_data_sheetname not in row['sheet'].split('|'):
                updated_sheets = row['sheet'] + ' | ' + sample_data_sheetname
                df.at[index, 'sheet'] = updated_sheets
                updated = True

        # Convert the DataFrame back to a list of lists to update the Google Sheet if updates were made
        if updated:
            updated_data = df.values.tolist()
            study_template_dict.update('A3', updated_data, value_input_option='USER_ENTERED')

        # Get the last row number to start appending new rows
        last_row = len(df) + 3  # Adding 3 because data starts from row 3

        # Add new MIMARKS terms
        for term, comment in new_MIMARKS_terms_with_comments.items():
            # Prepare the row content based on the column structure
            row_content = [term, '', '', comment, '', sample_data_sheetname]
            # Append the row to the sheet
            study_template_dict.append_row(row_content, table_range=f"A{last_row}")

            last_row += 1  # Increment to the next row for the next term

    else:
        print("Error, no datasheet found.")

    print('\nUpdate complete. Specified terms have been updated and new terms added to the dictionary.')
    print('----------------------------------------------')

if __name__ == "__main__":
    mimarks_terms_with_comments = get_mimarks_terms(mimarks_file_path)
    sample_data_sheetname, new_MIMARKS_terms_with_comments, list_of_terms = edit_template(mimarks_terms_with_comments, new_template_id, study_template_dict_sheet_id)
    print('Please check your new data template for accuracy before continuing!')
    print('If your data template is correct, update study-data-template-dict to include the new terms')
    choice = input('Would you like to continue and update the data dictionary? (Y / N): ')
    if choice == 'Y':
        update_data_dictionary(sample_data_sheetname, new_MIMARKS_terms_with_comments, study_template_dict_sheet_id, list_of_terms)
    if choice != 'Y':
        print('Exiting program. Restore your data template to previous version in Google Sheets if you discovered errors.')
import os
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the path to the credentials file from the .env file
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
credentials_path = credentials_path.replace('\\', '/')

# Get the path to the MIMARKS Excel file from the .env file
mimarks_file_path = os.getenv("MIMARKS_FILE_PATH")
mimarks_file_path = mimarks_file_path.replace('\\', '/')

# Define the scopes
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Authenticate using the credentials file
creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
client = gspread.authorize(creds)

# Load the MIMARKS file into a DataFrame
mimarks_df = pd.read_excel(mimarks_file_path)

def pause_for_user(message):
    input(f"{message} Press Enter to continue...")

def update_template(client, new_template_id, mimarks_df):
    # Step 1: Load the new template Google Sheet
    print("Loading new template Google Sheet...")
    new_sheet = client.open_by_key(new_template_id)
    sample_data = new_sheet.worksheet('sample_data')
    existing_terms = sample_data.col_values(1)
    pause_for_user("Loaded sample_data sheet from the new template.")
    
    # Step 2: Load the study-data-template-dict Google Sheet
    print("Loading study-data-template-dict Google Sheet...")
    study_template_dict_sheet = client.open_by_key('your_study_template_dict_sheet_id')  # Replace with actual ID
    study_template_dict = study_template_dict_sheet.worksheet('Sheet1')  # Adjust if necessary
    aoml_darwincore_terms = study_template_dict.col_values(study_template_dict.find('sample_data').col)
    pause_for_user("Loaded study-data-template-dict Google Sheet and identified AOML and Darwin Core terms.")
    
    # Step 3: Ensure AOML and Darwin Core terms are kept
    terms_to_keep = aoml_darwincore_terms
    
    # Step 4: Find new terms to add
    new_terms = [term for term in mimarks_df['Term'].tolist() if term not in existing_terms and term not in terms_to_keep]
    print(f"New terms identified: {new_terms}")
    
    # Step 5: Insert new terms into the sample_data sheet
    for term in new_terms:
        sample_data.append_row([term])
    pause_for_user("New terms added to the sample_data sheet.")
    
    # Step 6: Remove package-specific terms that are not in the new MIMARKS package
    terms_to_remove = [term for term in existing_terms if term not in mimarks_df['Term'].tolist() and term not in terms_to_keep]
    for term in terms_to_remove:
        cell = sample_data.find(term)
        sample_data.delete_row(cell.row)
    print(f"Removed terms: {terms_to_remove}")
    pause_for_user("Removed terms that are not in the new MIMARKS package.")
    
    # Step 7: Update NCBI required terms in green
    ncbi_required_terms = mimarks_df[mimarks_df['Required'] == '*']['Term'].tolist()
    for term in ncbi_required_terms:
        cell = sample_data.find(term)
        sample_data.format(f'{cell.row}:{cell.row}', {'backgroundColor': {'red': 0.0, 'green': 1.0, 'blue': 0.0}})
    pause_for_user("Updated NCBI required terms in green.")
    
    print("All steps completed successfully.")

if __name__ == "__main__":
    # ID of the new template Google Sheet (manually created copy)
    new_template_id = 'your_new_template_id'  # Replace with your actual new template ID
    
    # Call the function to update the template
    update_template(client, new_template_id, mimarks_df)

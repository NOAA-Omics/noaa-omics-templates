import os
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials

# Load .env file
load_dotenv()

# Get the path to the credentials file from the .env file
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Make sure the path is correctly interpreted
credentials_path = credentials_path.replace('\\', '/')

SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Authenticate using the credentials file
creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
client = gspread.authorize(creds)

def access_google_sheet():
    spreadsheet_id = '1qpVZ7n4H_5an1ywcxQ__HaEPutf2_pZrxDrOGFfRL48'  # Replace with your actual spreadsheet ID
    sheet = client.open_by_key(spreadsheet_id).sheet1
    data = sheet.get_all_records()
    print(data)

if __name__ == "__main__":
    access_google_sheet()
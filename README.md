# ATTENTION: This branch is legacy code.
This code was written for Version 1 of the data templates. Those templates have since changed, and the scripts are now maintained on the 'main' branch, using Version 2 of the data templates.

# NOAA Omics Study Data Templates

Reach out to bayden.willms@noaa.gov for questions.

## Overview of Scripts

Creating new data templates and updating the data dictionary accordingly have now been automated, in addition to the term markdown file generation in `generate_term_docs.py`. The new script, `generate_template.py`, will perform the following tasks:

1. **Get Latest MIMARKS Terms**: Retrieve the latest terms and their comments from the latest MIMARKS package (Excel file).
2. **Get up-to-date AOML and Darwin Core Terms**: Obtain up-to-date AOML and Darwin Core terms from the data dictionary (Google Sheet).
3. **Compare and Create New Data Template**: Compare terms from those files and an existing data template to create a new data template (Google Sheet) for a new environment.
4. **Update Data Dictionary**: Update the data dictionary (`study-data-template-dict` Google Sheet) with new terms and update existing terms appropriately.

Additionally, there is a script to verify the Google Sheets API connection called `test_auth.py`.


## Setup

### Administrator Setup
An AOML Omics Google Drive admin must grant permission for the Google Sheets and Drive API.

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Log in with AOML Omics account.
3. The project name is `data-templates`.

#### Creating a Service Account
1. Go to **API & Services > Credentials**.
2. Click on "Create Credentials" and select "Service Account".
3. Fill in the service account details (name, ID, description) and click "Create".

#### Assign Roles
1. In the next step, assign the "Editor" role to the service account to grant access to modify Google Sheets.
2. Click "Continue".

#### Create Key
1. Under the service account you created, click "Add Key" and select "JSON".
2. This will download a JSON file with the credentials to your computer.
3. Share this JSON file securely with the user who needs to set up the environment.

#### Grant Access to Service Account
1. The service account has an email address (e.g., `service-account-name@data-templates.iam.gserviceaccount.com`).
2. **Share the Google Sheets with this email address to grant access.**


### User Setup
This project works on both macOS and Windows. Ensure you have Git and Anaconda installed on your computer:

- [Download Git](https://git-scm.com/downloads)
- [Install Anaconda](https://docs.anaconda.com/anaconda/install/)

#### Setup Project Locally
1. Clone the GitHub project to your local machine:
```bash
git clone https://github.com/NOAA-Omics/noaa-omics-templates.git
cd noaa-omics-templates
```

2. Configure Anaconda environment using provided `environment.yml` 
```bash
conda env create -f environment.yml 
conda activate data-templates-env
```

#### Setup Google API Authentication
1. The admin will provide you with your `credentials.json` file.
2. Place the `credentials.json` in your 'script-dependencies' folder.
3. You can use the `test_auth.py` script to test API connection.


## Run

### Preparing Input Files

1. **Create a Copy of an Existing Data Template**:
   - Go to the AOML Omics Google Drive.
   - Create a copy of an existing data template.
   - Rename the copy according to your new environment name.
   - Rename the sheet name, for example, from `water_sample_data` to `sediment_sample_data`.

2. **Download MIMARKS File**:
   - Download the latest MIMARKS package from [NCBI Biosample Templates](https://submit.ncbi.nlm.nih.gov/biosample/template/).
   - Move the downloaded Excel file to the `script-dependencies` folder in the project.
   - Copy and paste the filename into the `generate_template.py` script at the line:
     ```python
     mimarks_filename = 'MIMARKS.survey.sediment.6.0.xlsx' # EDIT ME
     ```

3. **Configure Credentials**:
   - Copy your `credentials.json` filename and paste it into the `generate_template.py` script at the line:
     ```python
     credentials_filename = 'data-templates-c7159dc891a7.json' # EDIT ME
     ```

4. **Set Up Google Sheet IDs**:
   - The Google Sheet ID is available in the URL of the Google Sheet, between `/d/` and `/edit`. For example, in the URL `https://docs.google.com/spreadsheets/d/abc123XYZ456/edit`, the Google Sheet ID is `abc123XYZ456`.
   - You will need two Google Sheet IDs:
     1. One for `study-data-template-dict`.
     2. One for your newly created data template (the one that is a copy of an existing template).
   - Then, copy and paste those IDs into the `generate_template.py` script at the line:
   ```python
   study_template_dict_sheet_id = "abc123XYZ456" #EDIT ME
   new_template_id = "abc123XYZ456" #EDIT ME

### Running the Script

1. **Navigate to the Scripts Folder**:
   ```bash
   cd scripts
   python generate_template.py

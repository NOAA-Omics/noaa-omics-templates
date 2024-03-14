# NCBI submission instructions with NOAA Omics template  

These instructions are specifically for leveraging the NOAA Omics study data templates to submit sample metadata to NCBI BioSamples and raw sequence data to NCBI SRA. Detailed general instructions for submitting data to NCBI are found [here](https://www.ncbi.nlm.nih.gov/sra/docs/submitportal/) and should be referenced along with this guide. 

These instructions assume that you do not already have an existing BioProject or BioSamples, and that you are submitting data for both at the same time through the [SRA Submission Portal](https://submit.ncbi.nlm.nih.gov/subs/sra/). If you already have a BioProject or BioSamples, see the following section.  

## 1. Use study_data to create a BioProject  

1) [initiate a new SRA submission](https://submit.ncbi.nlm.nih.gov/subs/sra/).  

2) Use the study_data sheet to fill in relevant info for the BioProject if you have not already created a BioProject.  

## 2. Use sample_data to create BioSamples 

1) Select the correct BioSample package based on your NOAA Omics template. For example, select the MIMARKS.survey.water package if you used the NOAA_MIMARKS.survey.water template. You do NOT need to download an example Excel template from NCBI.  

2) The sample_data sheet will be used directly to create Biosamples in NCBI. We recommend downloading the Google Sheet as an Excel file, then saving the sample_data sheet as it's own excel file. Delete any columns from this file that you do not want on NCBI (such as date_sheet_modified, modified_by, internal notes). Upload the sample_data Excel file to NCBI.  

## 3. Use prep_data to provide SRA metadata  

It is easiest to submit SRA data to NCBI in batches based on sequencing run or the `amplicon_sequenced`, but you can also submit all of your data at once. We recommend submitting different markers separately. 

Either way, for each submission batch: 

1) In the Google Sheet, create a new sheet that is a copy of the SRA_template sheet and name it based on the marker/sequencing run you are currently submitting.  

2) Copy over data (just the values) from Columns A-M of the prep_data sheet into your new SRA_template sheet in the correct columns. 

3) If you do NOT already have BioSample accessions and are generating them in this submission, delete the biosample_accession column. 

4) Download the filled in SRA template as a .tsv. This is what you will upload for the SRA Metadata to NCBI.

## 4. Continue with file upload.


## Submitting SRA data for existing BioSamples  

If you already have BioSample accessions from a previous submission: 

1) [initiate a new SRA submission](https://submit.ncbi.nlm.nih.gov/subs/sra/).you will still initiate a new submission

2) Copy over data (just the values) from Columns A-M of the prep_data sheet into your new SRA_template sheet in the correct columns. 

3) Add the BioSample accessions to the biosample_accession column in the correct order. Remove the sample_name column, otherwise you submission will fail.
	
4) Download the filled in SRA template as a .tsv. This is what you will upload for the SRA Metadata to NCBI.

5) Continue with file upload.  

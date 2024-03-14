# Water  

| Sheets | Sheet definitions |
|---|---|
| [study_data](https://noaa-omics-templates.readthedocs.io/en/latest/study-data.html) | Metadata about the study, such as project name, description, funding info, and other project-level metadata required by NCBI and OBIS. This is filled out at the start of a project. |
| [water_sample_data](https://noaa-omics-templates.readthedocs.io/en/latest/water-sample-data.html) | Contextual data about the samples collected, such as when it was collected, where it was collected from, what kind of sample it is, and what were the properties of the environment or experimental condition from which the sample was taken. Each row is a distinct sample. Most of this information is recorded during sample collection. Many terms have controlled vocabulary, such as organism, env_broad_scale, waterBody. This file contains information that is submitted to NCBI when generating a BioSample. Other important fields for metadata processing include amplicon_sequenced, which helps to link together different types of metdata. This sheet contains terms from the MIMARKS survey water 6.0 package. For other types of samples (eg, sediment), use the [appropriate file](https://noaa-omics-templates.readthedocs.io/en/latest/index.html#environmental-sample-templates). |
| [prep_data](https://noaa-omics-templates.readthedocs.io/en/latest/prep-data.html) | Contextual data about how the samples were prepared for sequencing. Includes how they were extracted, what amplicon was targeted, how they were sequenced.  The 1st section of this file is in the format for an NCBI SRA upload and should NOT be rearranged or renamed. Each row is a separate sequencing library preparation, distinguished by a unique library_id. One sample from sample_prep could be represented multiple times on this sheet if multiple marker genes were amplified. |
| [analysis_data](https://noaa-omics-templates.readthedocs.io/en/latest/analysis-data.html) | Data about processing from raw sequences to the derived outputs, including software versions, processing parameters, reference database used. Often there is only one row for each amplicon that is sequenced. |
| asv_data | File generated by Tourmaline, containing ASV featureid, DNA sequence, assigned taxonomy, confidence in taxonomy, and read counts for each sample. This file is not stored in the metadata sheet and is not required for submission to NCBI, but is necessary for submission to OBIS. Sample names in the file must match names in the metadata template. |
|  |  |
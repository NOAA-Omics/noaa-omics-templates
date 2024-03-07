# analysis_data sheet  

Data about processing from raw sequences to the derived outputs, including software versions, processing parameters, reference database used. Often there is only one row for each type of molecular preparation that is sequenced.

## Terms  

| Term | Definition | Required By |
|---|---|---|
| amplicon_sequenced | If amplicon metabarcoding was performed, list amplicons separated by a \|? Name MUST match value provided to amplicon_sequenced on prep_data sheet. If metabarcoding not performed, list "not applicable". Only used for internal data management. | Recommended |
| ampliconSize | The length of the amplicon in basepairs. Median? | Recommended |
| trim_method | Method for trimming, including version and parameters | Recommended |
| cluster_method | Approach/algorithm when defining OTUs or ASVs, include version and parameters separated by semicolons Converted to otu_class_appr for Dwc | Recommended |
| pid_clustering | Percent identity used when clustering "species-level" OTUs or ASVs. Converted to otu_class_appr for DwC | Recommended |
| taxa_class_method | Method for assigning taxonomy, including version and parameters separated by semicolons Converted to 'otu_seq_comp_appr' for DwC | OBIS |
| taxa_ref_db | Reference database used for taxonomic assignment Converted to 'otu_db' for DwC | OBIS |
| code_repo | Link to public repository where analysis code is archived  Converted to identificationReferences for Dwc | OBIS |
| sop | Standard operating procedures used in assembly and/or annotation of genomes, metagenomes or environmental sequences. A reference to a well documented protocol, e.g. using protocols.io | Recommended |
| identificationReferences | A list (concatenated and separated) of references (publication, global unique identifier, URI) used in the Identification. Recommended best practice is to separate the values in a list with space vertical bar space ( \| ). | OBIS |
| controls_used | Provide number and types of controls or blanks used. Converted to eventRemarks for the sequencing library event | Recommended |
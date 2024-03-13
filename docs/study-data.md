# study_data Sheet

Metadata about the study, such as project name, description, funding info, and other project-level metadata required by NCBI and OBIS. This is filled out at the start of a project. 

## Terms  

| Term  | Definition | Required By |
|---|---|---|
| [project_id](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/project_id.html) | Internal short id for organizing projects. | Recommended |
| [project_name](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/project_name.html) | Brief title, as a phrase, for public display. This will be the Bioproject and OBIS title | NCBI+OBIS |
| [project_description](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/project_description.html) | Paragraph description of study goals and relevance, will be on BioProject and OBIS. This should provide enough information to help potential users of the data to understand if it may be of interest. | NCBI_OBIS |
| [project_proposal](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/project_proposal.html) | Link to internal project proposal | Internal |
| [project_id_external](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/project_id_external.html) | Short project id, to be used for external searching on OBIS. | OBIS |
| [project_contact](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/project_contact.html) | The list of people and organizations that should be contacted to get more information about the resource, that curate the resource or to whom putative problems with the resource or its data should be addressed. Providing an ORCID identifier is helpful for pulling info about the person(s). | OBIS |
| [type](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/type.html) | For survey projects, this will always be "Occurrence". https://www.gbif.org/data-quality-requirements-occurrences#emlType | OBIS |
| [license](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/license.html) | Publishing license to specify when submitting to OBIS. Datasets should be made available for use under CC0, CC-BY, or CC-BY-NC. GBIF’s recommended best practice is to use the most recent version, which 4.0 for CC-BY and CC-BY-NC. https://ipt.gbif.org/manual/en/ipt/latest/applying-license | OBIS |
| [citation](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/citation.html) | Can provide your own citation for the data as it is on GBIF/OBIS, or get an auto-generated citation. | Optional |
| [keywords](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/keywords.html) | Keywords or key phrase that concisely describes the resource or is related to the resource. | Recommended |
| [associated_parties](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/associated_parties.html) | Provide name and role of associated parties. Recommend to include ORCID ids. See this list: https://rs.gbif.org/vocabulary/gbif/agent_role.xml | Recommended |
| [study_area_description](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/study_area_description.html) | Short description of study area and ecosystem. Can link to an external reference. | Recommended |
| [external_links](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/external_links.html) | External links to be shared on BioProject, eg Github repo. Separated by \| | Recommended |
| [recorded_by](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/recorded_by.html) | A list (concatenated and separated) of names of people, groups, or organizations responsible for recording the original Occurrence. The recommended best practice is to separate the values with a vertical bar (' \| '). Including information about the observer improves the scientific reproducibility (Groom et al. 2020) | Recommended |
| [sampling_description](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/sampling_description.html) | Project-wide information about sampling methods used for the data, shown on OBIS. | Recommended |
| [grant_title](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/grant_title.html) | Funding information, to display on NCBI and OBIS | Recommended |
| [grant_agency](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/grant_agency.html) | Recommend providing name of funding agency and its DOI. A list of funding agencies with DOIs can be found here: https://doi.crossref.org/funderNames?mode=list | Recommended |
| [grant_number](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/grant_number.html) | Funding information, to display on NCBI and OBIS | Recommended |
| [project_proposal](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/project_proposal.html) | Internal link to project proposal | Internal |
| [accessions](https://noaa-omics-templates.readthedocs.io/en/latest/terms/study_data/accessions.html) | Place to add all accession of a project after submitting, eg Bioproject, GBIF, other accessions. Separate with space \| | Internal |
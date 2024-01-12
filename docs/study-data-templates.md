Study Data Templates
======

Use the Table of Contents on the left to navigate to relevant sections for your 'omics data types!

# NOAA Omics Study Data Templates

A new NOAA Omics study data template was developed based on feedback from NOAA partners at AOML, PMEL, and the NOAA Omics Data and Bioinformatics Supergroup. This template incorporates data standards from [MIxS](https://github.com/aomlomics/omics-data-management/wiki/3-Study-Data-Templates#sample-metadata-templates), [Darwin Core](https://dwc.tdwg.org/terms/), and custom recommended NOAA fields to facilitate data management of eDNA survey samples, from project initiation through data submission. For guidance on using the template, check out the template's `README` page or the [documentation wiki](). Additional templates are in development to cover other data types and environments. If you are interested in developing a NOAA Omics template for your data/environment type, please reach out to katherine.silliman@noaa.gov!
 <!-- change this to Read the Docs -->  

* **[NOAA_MIMARKS.survey.water.template](https://docs.google.com/spreadsheets/d/1YBXFU9PuMqm7IT1tp0LTxQ1v2j0tlCWFnhSpy-EBwPw/edit?usp=sharing)**: use for amplicon and/or metagenomic data from water environmental samples 
  + [Filled out example NOAA_MIMARKS template](https://docs.google.com/spreadsheets/d/1b7m5u7Cqj-L6vJYk81CHHDNNXftr3JRNCpGgcVJtCEE/edit?usp=sharing)
* **[NOAA_MIMARKS.survey.host-associated.template](https://docs.google.com/spreadsheets/d/1JtWgX_t5PbG0CpEJWHu906yH8Udek3l4I-KOM80MR6M/edit?usp=sharing)**: use for amplicon and/or metagenomic data from host-associated samples

# Templates for DNA/RNA sequence data

**While the templates below provide some information on metadata formatting and support the minimum metadata required for submission to NCBI, we provide additional formatting guidance and recommended custom metadata fields on the [Metadata Guidelines page](https://github.com/aomlomics/omics-data-management/wiki/4-Metadata-Guidelines#metadata-formats-and-custom-fields).**

## Sample metadata templates

Genomic Standards Consortium (GSC) Minimal Information about any (x) Sequence (MIxS) templates are the standard for sample metadata, which includes information about the primary sample: when it was collected (e.g., date and time), where it was collected from (e.g., latitude, longitude, elevation/depth, site name, country, etc.), what kind of sample it was (e.g., soil, seawater, feces), and the properties of the environment during collection (e.g., temperature, salinity, pH) or experimental condition (e.g., experimental or control, disease state) from which the sample was taken. 

Metadata input templates:

* NCBI provides a [useful link](https://submit.ncbi.nlm.nih.gov/biosample/template/) to download MIxS sample metadata templates based on your sequence data type and sample environment (known as 'packages'). These templates will be appropriate for the majority of NOAA 'Omics projects that generate DNA/RNA sequence data, and can be used to **generate NCBI BioSamples**. The [NOAA Omics study data template](https://docs.google.com/spreadsheets/d/1fAJxtH_ioIN5Ri7dXe4Lsy8SuImg8NR79MUGSOb1vpk/edit?usp=sharing) includes a `sample_data' sheet that can be used for submission to NCBI BioSample.
* The National Microbiome Data Collaborative (NMDC) maintains the [NMDC Submission Portal](https://data.microbiomedata.org/submission/home) that allows inputing metadata with real-time validation. The submission portal supports several different community standards, such as the MIxS standard from GSC, the PROV standard for provenance metadata, the Proteomics Standards Initiative (PSI) standards for metaproteomics, and the Metabolomics Standards Initiative (MSI) standards for metabolomics. 

A guide to choosing the right metadata package given your 'omics data type is below:  

**Table 1.** Suggested MIxS templates for common environmental omics datatypes.

| Data type | Description | Metadata package |
|---|---|---|
| amplicon survey | Use for any type of marker gene sequences, eg, 16S, 18S, 23S, 28S rRNA or COI obtained directly from the environment, without culturing or identification of the organisms. | MIMARKS Survey |
| metagenome | Use for environmental and metagenome sequences. | MIMS Environmental/Metagenome |
| metagenome-assembled genome | Use for metagenome-assembled genome sequences produced using computational binning tools that group sequences into individual organism genome assemblies starting from metagenomic data sets. | MIMAG Metagenome-assembled Genome |
| single amplified genome | Use for single amplified genome sequences produced by isolating individual cells, amplifying the genome of each cell using whole genome amplification, and then sequencing the amplified DNA. | MISAG Single Amplified Genome |
| uncultivated virus genome | Use for uncultivated virus genome identified in metagenome and metatranscriptome datasets. | MIUVIG Uncultivated Virus Genome |
| amplicon specimen | Use for any type of marker gene sequences, eg, 16S, 18S, 23S, 28S rRNA or COI obtained from cultured or voucher-identifiable specimens. | MIMARKS Specimen |
| cultured bacteria or archaea | Use for cultured bacterial or archaeal genomic sequences. | MIGS Cultured Bacterial/Archaeal |
| viral genome | Use for virus genomic sequences. | MIGS Viral |
| eukaryotic genome | Use for eukaryotic genomic sequences. | MIGS Eukaryotic |
| qPCR or ddPCR or rt-PCR | Use for any type of real time PCR, quantitative PCR (qPCR), or digital PCR. | MIQE, RDML, & dMIQE |

For most NOAA 'Omics projects, the `water` or `sediment` environmental packages will be appropriate.

## Preparation metadata templates 

Preparation metadata is directly related to the preparation of the biomaterial undergoing the 'omics assay and the process of performing the assay. A primary sample could be split (aliquoted) and processed through multiple preparation methods; therefore, there could be multiple sets of preparation metadata for a single set of samples.  

NCBI repositories (e.g., SRA, GenBank) provide some templates for the minimum required preparation metadata, while in other cases they require interactive user input. We recommend submitting your sample metadata and generating BioSample accession IDs first, although you can do both steps at the same time. The [NOAA Omics study data template](https://docs.google.com/spreadsheets/d/1fAJxtH_ioIN5Ri7dXe4Lsy8SuImg8NR79MUGSOb1vpk/edit?usp=sharing) includes a `prep_data' sheet that can be used for submission to NCBI SRA.

**High-throughput sequencing data (SRA)**

Projects using high-throughput sequencing data (e.g., amplicon, metagenomic, RNASeq, RAD-Seq) can use the [NCBI SRA template](https://ftp-trace.ncbi.nlm.nih.gov/sra/metadata_table/SRA_metadata_acc.xlsx).

**Sanger sequencing**

Sequencing projects generated without high-throughput sequencing (e.g., single gene Sanger sequencing) can use the [NCBI Genbank template](https://submit.ncbi.nlm.nih.gov/about/bankit/).  
  

# Other omics data types

For NOAA Omics projects that generate biological data other than DNA/RNA sequencing:

## Targeted quantitative surveys (qPCR, ddPCR, rt-PCR)

Projects generated with real time PCR, qPCR, or dPCR and can use the Minimum Information for Publication of Quantitative Real-Time PCR Experiments (MIQE) [Real-time PCR Data Markup Language (RDML) template](https://rdml.org/index.html).

Additional resources for best practices:
1. Environmental Microbiology Minimum Information (EMMI) Guidelines [Borchardt et al. 2021](https://pubs.acs.org/doi/full/10.1021/acs.est.1c01767)
2. The MIQE guidelines: minimum information for publication of quantitative real-time PCR experiments [Bustin et al. 2009](https://pubmed.ncbi.nlm.nih.gov/19246619/)
3. Guidance on the Use of Targeted Environmental DNA (eDNA) Analysis for the
Management of Aquatic Invasive Species and Species at Risk from the Canadian Science Advisory Secretariat [Abbot et al. 2021](https://westernregionalpanel.org/wp-content/uploads/2021/04/Canada_eDNAGuidanceDoc.pdf) 
4. Best Practices in qPCR and dPCR Validation in Regulated Bioanalytical Laboratories [Hays et al. 2022](https://link.springer.com/article/10.1208/s12248-022-00686-1) from the American Association of Pharmaceutical Scientists Workshop
3. [Sanders et al. 2018](https://www.sciencedirect.com/science/article/pii/S2214753517302097)
4. [Langlosi et al. 2021](https://onlinelibrary.wiley.com/doi/full/10.1002/edn3.164)


## Proteomics

| Sample Data | Required? | Definition or Example | Recommended Format | Repository |
|---|---|---|---|---|
|MS data|Y|Original proprietary files provided by the instruments used in the study (e.g. Thermo RAW)| [mzML](https://www.psidev.info/mzML); </br> *Controlled vocabulary:* [MS ontology](https://www.ebi.ac.uk/ols/ontologies/ms); </br> *File formatting details:* [Pride](https://www.ebi.ac.uk/pride/markdownpage/pridefileformats)| [PRIDE](https://www.ebi.ac.uk/pride/markdownpage/pridefileformats)
|Sequencing  data | N | Amino acid sequences, Whole genome sequences, RNA seq, Whole Exome Sequences | [FASTA](https://www.ncbi.nlm.nih.gov/genbank/fastaformat/), [FASTQ](https://www.ncbi.nlm.nih.gov/sra/docs/submitformats/#:~:text=Fastq%20consists%20of%20a%20defline,There%20are%20many%20variations.)| [MassIVE](https://massive.ucsd.edu/ProteoSAFe/static/massive.jsp), </br> [PRIDE](https://www.ebi.ac.uk/pride/markdownpage/pridefileformats) (as optional data), [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra)|

**Other options for repositories, as well as general data submission [guidelines](http://www.proteomexchange.org/docs/guidelines_px.pdf) can be found on the ([ProteomeXchange](https://www.proteomexchange.org/)) website.**

## Metabolomics  

| Sample Data | Required? | Definition or Example | Recommended Format | Repository |
|---|---|---|---|---|
|Raw NMR or MS data| Y | *NMR*: can be free induction decay (FID) or fourier transformed (FT) ; Should also include instrument and software versions.| Open Source Formats ([mzML](https://www.psidev.info/mzML), [mzXML](https://sashimi.sourceforge.net/schema_revision/mzXML_2.1/Doc/mzXML_2.1_tutorial.pdf), [CDF](https://cdf.gsfc.nasa.gov/))| [Metabolomics Workbench](https://www.metabolomicsworkbench.org/data/faq.php)|
|Sequencing Data| N | Whole genome, Amplicon, Transcriptome | [FASTA](https://www.ncbi.nlm.nih.gov/genbank/fastaformat/), [FASTQ](https://www.ncbi.nlm.nih.gov/sra/docs/submitformats/#:~:text=Fastq%20consists%20of%20a%20defline,There%20are%20many%20variations.) | [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra)|

# Formats for processed omics data

If your 'omics data is processed using bioinformatics, the resulting file(s) from those analyses should also be archived. Below are suggested formats and destinations repositories for common environmental 'omics datasets.  


**Table 2.** Suggested formats and destinations repositories for common environmental omics datasets. Please note that, although NOAA's Coral Reef Information System ([CoRIS](https://www.coris.noaa.gov/CoRIS)) is the preferred venue for archiving NOAA-funded coral reef data, all CoRIS submissions are handled by NCEI.

Data type | Data formats (non-exhaustive) | Repository
-- | -- | --
DNA reference sequences | GenBank format | [NCBI GenBank](https://www.ncbi.nlm.nih.gov/genbank/submit/)
DNA sequence data (amplicon, metagenomic, RAD-Seq) | Raw FASTQ | [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra/docs/submit/)
Amplicon Sequence Variants | Reference FASTA | [GBIF/OBIS](https://github.com/aomlomics/edna2obis), or directly to NCEI](https://www.ncei.noaa.gov/archive)
RNA sequence data (RNA-Seq) | Raw FASTQ | [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra/docs/submit/)
Functional genomics data (quantitative gene expression, ChIP-Seq, HiC-seq, methylation seq) | Metadata, processed data (e.g., raw read counts), SRA accessions| [NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/info/submission.html)
RNA transcript assemblies | FASTA or SQN file | [NCBI TSA](https://www.ncbi.nlm.nih.gov/genbank/tsa/)
Genome assemblies | FASTA or SQN file, optional AGP file to orient scaffolds | [NCBI WGS](https://www.ncbi.nlm.nih.gov/genbank/genomesubmit/)
Quantitative PCR data | Tab-delimited text | [NCEI](https://www.ncei.noaa.gov/archive)
Mass spectrometry data (metabolomics, proteomics) | Raw mass spectra, MZML, MZID | [ProteomeXChange](https://www.proteomexchange.org/), [Metabolomics Workbench](https://www.metabolomicsworkbench.org/)
Coral reef data | Tab-delimited text, HDF, or netCDF (less preferable) | [CoRIS](https://www.coris.noaa.gov/CoRIS) (via [NCEI](https://www.ncei.noaa.gov/archive))
Feature observation tables and feature metadata | BIOM (HDF5) format (feature observation tables), tab-delimited text (feature metadata) | GBIF/OBIS](https://github.com/aomlomics/edna2obis) or directly to [NCEI](https://www.ncei.noaa.gov/archive)(https://www.ncei.noaa.gov/archive) (size permitting), [Zenodo](https://zenodo.org/), or [Figshare](https://figshare.com/)
Reference database | FASTA (sequences) and TSV (taxonomy) | [Zenodo](https://zenodo.org/) or [FigShare](https://figshare.com/) or [Dryad](https://datadryad.org/stash)
Analysis code | Commented code and Jupyter notebooks | GitHub (optionally archived on [Zenodo](https://zenodo.org/) or [FigShare](https://figshare.com/) or [Dryad](https://datadryad.org/stash))
Figure code   | Commented code for recreating figures (R, etc) | GitHub (optionally archived on [Zenodo](https://zenodo.org/) or [FigShare](https://figshare.com/) or [Dryad](https://datadryad.org/stash))


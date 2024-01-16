#!/usr/bin/env python

# Code to create a manifest file from the NOAA_MIMARKS metadata template
# v1.0.1
# Author: Katherine Silliman

# import libraries
import pandas as pd
import sys
import os
import argparse


# usage
usage = '''
manifest_from_noaa_template.py -i template_in -s sample_sheet -f fastq_sheet -a amplicon -p paired -P path -o output_prefix

    -i, --template_in - full path of metadata Excel file (required)
    -s, --sample_sheet - name of the sheet in 'template_in' with sample names, default = 'water_sample_data'
    -f, --fastq_sheet - name of the sheet in 'template_in' with fastq file names, default = 'amplicon_prep_data'
    -a, --amplicon - name of amplicon to generate a manifest file, (required)
    -p, --paired - True or False, are these paired end samples, default = True
    -P, --path - path to the sequencing files, to prefix the filenames (required)
    -o, --output_prefix - Prefix for output files, default is ""

'''


argParser = argparse.ArgumentParser()
argParser.add_argument("-i", "--template_in", help="full path of metadata Excel file (required)")
argParser.add_argument("-s", "--sample_sheet", default="water_sample_data",help="name of the sheet in 'template_in' with sample names, default = water_sample_data")
argParser.add_argument("-f", "--fastq_sheet", default='amplicon_prep_data',help="name of the sheet in 'template_in' with fastq file names, default = 'amplicon_prep_data'")
argParser.add_argument("-a", "--amplicon", help="name of amplicon to generate a manifest file, use 'None' to not filter by amplicon ")
argParser.add_argument("-p", "--paired", default=True,help="True or False, are these paired end samples, default = True")
argParser.add_argument("-P", "--path",help="path to the sequencing files, to prefix the filenames (required)")
argParser.add_argument("-o", "--output_prefix", default="",help="Prefix for output files, default is "" ")


args = argParser.parse_args()

# read in excel
data = pd.read_excel(
    args.template_in, [args.sample_sheet,args.fastq_sheet],
    index_col=None, na_values=[""], comment="#"
)

# remove * from headers, to make backwards compatible with older templates
data[args.sample_sheet].columns = data[args.sample_sheet].columns.str.replace("*","")

# extract rows from prep sheet that match given amplicon
if args.amplicon != None:
    prep = data[args.fastq_sheet][data[args.fastq_sheet]['amplicon_sequenced'].str.contains(args.amplicon)]
    if args.paired:
        files = prep.loc[:,['sample_name','filename','filename2']]
    else:
        files = prep.loc[:,['sample_name','filename']]
    merged = data[args.sample_sheet].merge(files,how='right',on='sample_name')
# if no amplicon is specified, use all rows in prep sheet
else:
    prep = data[args.fastq_sheet]
    if args.paired:
        files = prep.loc[:,['sample_name','filename','filename2']]
    else:
        files = prep.loc[:,['sample_name','filename']]
    merged = data[args.sample_sheet].merge(files,how='right',on='sample_name')

#save metadata file
meta = merged.drop(columns=[col for col in merged.columns if 'filename' in col])
# TODO: add code to split columns in metadata file to extract numeric values

# print metadata file
meta.to_csv(args.output_prefix+'metadata.tsv',sep='\t',index=False)

#save manifest
# need to split up filenames into 2 rows
if args.paired:
    man_pe = merged.loc[:,['sample_name','filename','filename2']]
    man_pe = pd.melt(man_pe, id_vars=['sample_name'], value_vars=['filename', 'filename2'], 
        var_name='direction',value_name='absolute-filepath')
    man_pe['direction'] = man_pe['direction'].replace({'filename': 'forward', 'filename2': 'reverse'})
    man_pe['absolute-filepath'] = args.path + '/'+man_pe['absolute-filepath'].astype(str)
    man_pe = man_pe.rename(columns={'sample_name': 'sample-id'})

    man_pe.to_csv(args.output_prefix+'manifest_pe.csv',index=False)

    #print SE manifest
    man_se = man_pe[man_pe['direction'] != 'reverse']
    man_se.to_csv(args.output_prefix+'manifest_se.tsv',sep='\t',index=False)
#if not paired-end sequencing, only make SE manifest
else:
    man_se = merged.loc[:,['sample_name','filename']]
    man_se = man_se.rename(columns={'sample_name': 'sample-id', 'filename': 'absolute-filepath'})
    man_se['direction'] = 'forward'
    man_se['absolute-filepath'] = args.path + '/'+man_se['absolute-filepath'].astype(str)

    man_se.to_csv(args.output_prefix+'manifest_se.csv',index=False)






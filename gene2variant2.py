#!/usr/bin/python
import fileinput
import re
import json
import requests
import urllib

gene_name = raw_input("Please type your gene name, all caps, and press enter: ")

Lookup_geneID={}

for each_line_of_text in fileinput.input(['/home/xiuwenli/Assignment5/Homo_sapiens.GRCh37.75.gtf']):
    gene_id_matches = re.findall('gene_id \"(.*?)\";',each_line_of_text)
    gene_name_matches = re.findall('gene_name \"(.*?)\";',each_line_of_text)
    if gene_id_matches:
       if gene_name_matches:
          Lookup_geneID[gene_id_matches[0]] = gene_name_matches[0]

from re import sub
url = "http://rest.ensembl.org/overlap/id/ENSG00000130203.json?feature=variation"
response = urllib.urlopen(url)
data = json.loads(response.read())
for i in range(0, len(data)):
    dic = data[i]
    id_names = dic['id']
    consequence_type = dic['consequence_type']
    consequence_new = consequence_type.replace("_"," ")
    clinical_significance = dic['clinical_significance']
    if clinical_significance:
       print "Variant " + id_names + " is a " + consequence_new + ", " + "and is clinically " + clinical_significance[0].upper()
    else:
       print "Variant " + id_names + " is a " + consequence_new + ". "
   
     

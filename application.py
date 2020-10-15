#Read-in script for Number of figures and sheets

# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd
import csv
import numpy as np

# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir("F:\Work space\Senior_Spring\Senior Research CSC 450\PatentsView-Code-Snippets-master\databases")
file_name_APP = "application.tsv.zip"
f_name_APP = "application.tsv"
file_name_Brief = "brf_sum_text_2020.tsv.zip"
f_name_Brief = "brf_sum_text_2020.tsv"
file_name_Detail = "detail-desc-text-2020.tsv.zip"
f_name_Detail = "detail-desc-text-2020.tsv"
file_name_government = "government_organization.tsv.zip"
f_name_government = "government_organization.tsv"
file_name_inv = "inventor.tsv.zip"
f_name_inv = "inventor.tsv"
# Selecting the zip file.
zf_APP = zip.ZipFile(file_name_APP)
# Reading the selected file in the zip.
df_APP = pd.read_csv(zf_APP.open(f_name_APP), delimiter="\t", quoting = csv.QUOTE_NONNUMERIC)
# Selecting the zip file.
#zf_Brief = zip.ZipFile(file_name_Brief)
## Reading the selected file in the zip.
#df_Brief = pd.read_csv(zf_Brief.open(f_name_Brief), delimiter="\t", quoting = csv.QUOTE_NONNUMERIC)
#zf_Detail = zip.ZipFile(file_name_Detail)
## Reading the selected file in the zip.
#df_Detail = pd.read_csv(zf_Detail.open(f_name_Detail), delimiter="\t", quoting = csv.QUOTE_NONNUMERIC)
#zf_government = zip.ZipFile(file_name_government)
## Reading the selected file in the zip.
#df_government = pd.read_csv(zf_government.open(f_name_government), delimiter="\t", quoting = csv.QUOTE_NONNUMERIC)
#zf_inv = zip.ZipFile(file_name_inv)
## Reading the selected file in the zip.
#df_inv = pd.read_csv(zf_inv.open(f_name_inv), delimiter="\t", quoting = csv.QUOTE_NONNUMERIC)
file_name_uspc = "uspc_current.tsv.zip"
f_name_uspc = "uspc_current.tsv"
zf_uspc = zip.ZipFile(file_name_uspc)
chunksize = 15*(10 ** 5)
count = 1
n_obs = 0
df_uspc = pd.read_csv(zf_uspc.open(f_name_uspc), delimiter="\t", chunksize=chunksize, quoting=csv.QUOTE_NONNUMERIC)
    #print('processing chunk: ' + str(count))
    #n_obs += len(df)
    #count += 1
# Print first five observations
#df_APP.head()
#print("=====================  Applications   ====================================")
#print(df_APP.head())
print(df[df['patent_id']=="1.46437e+07"])
## Print summary of data: number of columns, observations, and each variable data type
##print(len(df_APP))
##df_APP.info()
## Print basic summary statistics for numerical variables
##print(df_APP.describe(exclude=[np.number]))
#print("==========================================================================")


# Print first five observations
print(df_APP.head())
#print("============================= Brief ====================================")
#print(df_Brief.head())
#print("========================================================================")
#print("=========================================================================")
#
#
## Print first five observations
##df_APP.head()
#print("============================= Detail ====================================")
#print(df_Detail.head())
#print("========================================================================")
#print("============================= Government ====================================")
#print(df_government.head())
#print("========================================================================")
#print("=============== Inventor ========================")
#print(df_inv.head())
#print("========================================================================")
#print("=============== USPC ========================")
#print(df_uspc.head())
#print("========================================================================")
    #4637773
patentID = input("Enter patent ID: ")
df_new=df_APP["patent_id"]==patentID
  
# display 7430869
df_APP.where(df_new, inplace = True) 
print(df_APP[df_APP['patent_id']=="10000026"])
# display 
#print(df_new)
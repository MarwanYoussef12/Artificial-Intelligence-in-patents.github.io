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

file_name = "inventor_gender.tsv.zip"
f_name = "inventor_gender.tsv"
# Selecting the zip file.
zf = zip.ZipFile(file_name)
# Reading the selected file in the zip.
df = pd.read_csv(zf.open(f_name), delimiter="\t", quoting = csv.QUOTE_NONNUMERIC)
print(df[df['disambig_inventor_id_20200331']=="10000158-1"])

print("=========================================")
# Print first five observations

print("======================= Inventor gender ========================")
print(df.head())
print("========================================================================")
print(df.sample)
# Print summary of data: number of columns, observations, and each variable data type
print(len(df))
df.info()
# Print basic summary statistics for numerical variables
print(df.describe(exclude=[np.number]))
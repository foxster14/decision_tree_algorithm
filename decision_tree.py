import pandas as pd
import xlsxwriter

path = '/Users/sarahfox/OneDrive - Dunwoody College of Technology/Junior Year/Data Science/Decision Trees/' #path where all files are stored

filename = 'drug_classification.csv'

## Import sheets
data_frame = pd.read_csv(path + filename)
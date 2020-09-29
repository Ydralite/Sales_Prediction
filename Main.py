#!kaggle competitions download -c competitive-data-science-predict-future-sales

import kaggle
import zipfile
import glob
import pandas as pd

def unzip(zip_file, destination):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(destination)


# Get files - run first time
#zip = 'C:\\Users\\anton\\competitive-data-science-predict-future-sales.zip'
#destin = 'C:\\Users\\anton\\competitive-data-science-predict-future-sales'

#unzip(zip, destin)


files = (glob.glob('C:\\Users\\anton\\competitive-data-science-predict-future-sales\\*'))

items = pd.read_csv(files[0])
item_categories = pd.read_csv(files[1])
sales_train = pd.read_csv(files[2])
sample_submission = pd.read_csv(files[3])
shops = pd.read_csv(files[4])
test = pd.read_csv(files[5])
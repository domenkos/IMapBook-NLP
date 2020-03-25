import pandas as pd

DATA_DIR = '../data/'
FILENAME = 'AllDiscussionDataCODED_USE_THIS_14Feb2020_MH.xls'

data = df = pd.read_excel( io=DATA_DIR + FILENAME ).dropna( 'columns', 'all' )
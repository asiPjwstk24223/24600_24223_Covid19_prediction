import os
import zipfile
import pandas as pd

os.environ['KAGGLE_USERNAME'] = 'kacperbocian'
os.environ['KAGGLE_KEY'] = 'e759ad68412feb864a51bfc58727ca52'

from kaggle.api.kaggle_api_extended import KaggleApi
from sklearn.model_selection import train_test_split


api = KaggleApi()
#api.authenticate()

datasets = [
    "takbiralam/covid19-symptoms-dataset",
    "zhiruo19/covid19-symptoms-classification"
]

def download_and_extract(dataset):
    """Download and extract zip files from Kaggle."""
    api.dataset_download_files(dataset, unzip=True)

for dataset in datasets:
    download_and_extract(dataset)

csv_files = [f"{file}" for file in os.listdir("./") if file.endswith(".csv")]
dataframes = [pd.read_csv(file) for file in csv_files]
data1 = dataframes[0]
data2 = dataframes[1]
data1['fever'] = data1['fever'].astype(int)
data2.rename(columns = {'bodyPain':'bodypain','runnyNose':'runnynose','diffBreath':'diffbreath','infectionProb':'infected'}, inplace = True)
combined_df = pd.concat([data1,data2], ignore_index=True)
train, test = train_test_split(combined_df, test_size=0.3)
train.to_csv('train.csv', index=False)
test.to_csv('test.csv', index=False)
combined_df.to_csv('combined.csv', index=False)
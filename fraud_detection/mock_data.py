import numpy as np
import pandas as pd

TARGET = 'isFraud'

##split dataset
filename = 'kaggle_data/fraud_detection.csv'
data = pd.read_csv(filename)
print("load data")
data["id"] = data.index + 1
# split dataset  
size = len(data.index)
for column in data.columns:
    data[column] = np.random.choice(data[column], size, replace=False)
mock_data_train = data.iloc[:int(0.8*size)]
mock_data_test = data.iloc[int(0.8*size):]
mock_data_sample_submission = mock_data_test[['id', TARGET]]
mock_data_test = mock_data_test.drop(TARGET, axis=1)
mock_data_train.to_csv('kaggle_data/train.csv')
print("kaggle_data/train.csv")
mock_data_test.to_csv('kaggle_data/test.csv')
print("kaggle_data/test.csv")
mock_data_sample_submission.to_csv('kaggle_data/sample_submission.csv')
print("kaggle_data/sample_submission.csv")


## data of ramp test 
train_filename = 'kaggle_data/train.csv'
data = pd.read_csv(train_filename)
size = 100000
mock_data = data.iloc[:100000]
for column in mock_data.columns:
    mock_data[column] = np.random.choice(data[column], size, replace=False)
mock_data_train = mock_data.iloc[:80000]
mock_data_test = mock_data.iloc[80000:]
mock_data_sample_submission = mock_data_test[['id', TARGET]]
mock_data_test = mock_data_test.drop(TARGET, axis=1)
mock_data_train.to_csv('data/train.csv')
mock_data_test.to_csv('data/test.csv')
mock_data_sample_submission.to_csv('data/sample_submission.csv')


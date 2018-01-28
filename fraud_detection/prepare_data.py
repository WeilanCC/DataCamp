import pandas as pd
from sklearn.utils import shuffle

kaggle_dataset = 'kaggle_data/fraud_detection.csv'
kaggle_data = pd.read_csv(kaggle_dataset)

kaggle_data.insert(0, 'id', range(len(kaggle_data)))

kaggle_data = shuffle(kaggle_data)

size = len(kaggle_data)
kaggle_data_train = kaggle_data.iloc[:int(0.8 * size)]
kaggle_data_test = kaggle_data.iloc[int(0.8 * size):]

kaggle_data_train.to_csv('kaggle_data/train.csv', index=False)
kaggle_data_test.to_csv('kaggle_data/test.csv', index=False)

train_dataset = 'kaggle_data/train.csv'
data = pd.read_csv(train_dataset)

size = 100000
data = data.iloc[:size]

data = shuffle(data)

data_train = data.iloc[:int(0.8 * size)]
data_test = data.iloc[int(0.8 * size):]
TARGET = 'isFraud'
data_sample_submission = data_test[['id', TARGET]].copy()
data_sample_submission[TARGET] = 0

data_train.to_csv('data/train.csv', index=False)
data_test.to_csv('data/test.csv', index=False)
data_sample_submission.to_csv('data/sample_submission.csv', index=False)

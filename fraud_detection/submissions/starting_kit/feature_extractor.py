import numpy as np
from sklearn import preprocessing

class FeatureExtractor():
    def __init__(self):
        self.le = preprocessing.LabelEncoder()
        self.enc = preprocessing.OneHotEncoder()

    def fit(self, X_df, y):
        return self

    def transform(self, X_df):
        X_df = X_df.drop(['nameDest','nameOrig'],axis = 1)
        X_categorical = X_df.select_dtypes(include=[object])
        X_label = X_categorical.apply(self.le.fit_transform)
        self.enc.fit(X_label)
        dummy = self.enc.transform(X_label).toarray()
        X_df = X_df.drop(['type'],axis = 1)
        return np.concatenate((X_df.values, dummy), axis=1)

class FeatureExtractor():
    def __init__(self):
        pass

    def fit(self, X_df, y):
        pass

    def transform(self, X_df):
        X_df = X_df.drop(['nameDest','nameOrig','type'],axis = 1)
        return X_df.values

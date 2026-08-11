class DataTransformer:

    def clean_data(self, df):

        df = df.drop_duplicates()
        df = df.fillna("Unknown")

        return df
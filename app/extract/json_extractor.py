import pandas as pd
import json


class JsonExtractor:

    def read_mock_data(self, file_path):
        with open(file_path, "r") as file:
            response = json.load(file)
        df = pd.DataFrame(response["value"])

        print("\nJSON Data Loaded Successfully!")
        print(df)

        return df
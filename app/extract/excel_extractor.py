import pandas as pd

class ExcelExtractor:

    def read_file(self, file_path):
        df = pd.read_excel(file_path)

        print("\nExcel Data Loaded Successfully!")
        print(df)

        return df
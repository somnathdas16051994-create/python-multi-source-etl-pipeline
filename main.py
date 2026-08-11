import pandas as pd
from app.extract.excel_extractor import ExcelExtractor
from app.extract.json_extractor import JsonExtractor
from app.extract.sharepoint_extractor import SharePointExtractor
from app.config.settings import (SITE_ID, LIST_ID)

from app.transform.data_transform import DataTransformer
from app.database.mysql_service import MySQLService

def run_pipeline():

    print("\n===== ETL PIPELINE STARTED =====")

    # Excel Extract
    excel_extractor = ExcelExtractor()
    excel_df = excel_extractor.read_file("data/raw/employees.xlsx")
    print("\nExcel Data:")
    print(excel_df)

    #Sharepoint Extract
    sharepoint_extractor = SharePointExtractor()
    sharepoint_df = sharepoint_extractor.get_sharepoint_data(SITE_ID, LIST_ID)
    print("\nSharePoint Data:")
    print(sharepoint_df)

    #Dummy Json Extract
    json_extractor = JsonExtractor()
    json_df = json_extractor.read_mock_data("data/mock/sharepoint_response.json")
    print("\nJSON Data:")
    print(json_df)

    #Combine DataFrame
    df = pd.concat([excel_df, sharepoint_df, json_df], ignore_index = True)
    print("\nCombined Data:")
    print(df)

    # Transform
    transform = DataTransformer()
    cleaned_df = transform.clean_data(df)

    print("\nCleaned Data")
    print(cleaned_df)

    # Load
    mysql = MySQLService()
    mysql.load_data(cleaned_df)

    print("\n===== ETL PIPELINE COMPLETED =====")


if __name__ == "__main__":

    run_pipeline()
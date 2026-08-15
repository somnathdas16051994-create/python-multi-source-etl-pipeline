import pandas as pd

from app.extract.excel_extractor import ExcelExtractor


def test_read_excel_file():
    extractor = ExcelExtractor()

    df = extractor.read_file("data/raw/employees.xlsx")

    assert isinstance(df, pd.DataFrame)
    assert not df.empty

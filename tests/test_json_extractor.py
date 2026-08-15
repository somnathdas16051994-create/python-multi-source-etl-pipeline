import pandas as pd

from app.extract.json_extractor import JsonExtractor


def test_read_mock_json_data():
    extractor = JsonExtractor()

    df = extractor.read_mock_data(
        "data/mock/sharepoint_response.json"
    )

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
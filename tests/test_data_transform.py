import pandas as pd

from app.transform.data_transform import DataTransformer


def test_clean_data_removes_duplicates_and_fills_missing_values():

    df = pd.DataFrame({
        "employee_id": [1, 1, 2],
        "employee_name": ["John", "John", None]
    })

    transformer = DataTransformer()

    result = transformer.clean_data(df)

    assert len(result) == 2
    assert result["employee_id"].is_unique
    assert "Unknown" in result["employee_name"].values

from sqlalchemy import create_engine, text
from app.config.settings import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


class MySQLService:
    def __init__(self):
        self.engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    def load_data(self, df):

        # df.to_sql(name = "sharepoint", con = self.engine, if_exists = "append", index = False)
        # print("Data Loaded Successfully")
        # # print(df.head())

        query = text("""
        INSERT INTO sharepoint (employee_id, name, department)
        VALUES (:employee_id, :name, :department)
        ON DUPLICATE KEY UPDATE
        name = VALUES(name),
        department = VALUES(department)
        """)

        with self.engine.begin() as conn:
            for _, row in df.iterrows():
                conn.execute(query,
                {
                    "employee_id" : row["Employee_ID"],
                    "name" : row["Name"],
                    "department" : row["Department"]
                }
            )
        print("Data Loaded Successfully!")
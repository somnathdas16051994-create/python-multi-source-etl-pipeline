import requests
import pandas as pd
import msal
from app.config.settings import (CLIENT_ID, TENANT_ID, CLIENT_SECRET)


class SharePointExtractor:

    def __init__(self):

        self.tenant_id = TENANT_ID
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET

    def get_access_token(self):

        authority = (
            f"https://login.microsoftonline.com/"
            f"{self.tenant_id}"
        )

        app = msal.ConfidentialClientApplication(
            self.client_id,
            authority=authority,
            client_credential=self.client_secret
        )

        result = app.acquire_token_for_client(
            scopes=["https://graph.microsoft.com/.default"]
        )

        if "access_token" not in result:
            raise Exception(f"Unable to acquire access token : {result}")

        return result["access_token"]
    

    def get_sharepoint_data(self, site_id, list_id):
        token = self.get_access_token()

        headers = {
           "Authorization": f"Bearer {token}",
            "Accept": "application/json"
        }

        url = (
            f"https://graph.microsoft.com/v1.0/"
            f"sites/{site_id}/lists/{list_id}/items"
            f"?expand=fields"
        )
        all_records = []

        while url:

            response = requests.get(url, headers=headers, timeout = 30)

            response.raise_for_status()

            data = response.json()
        
            records = [
                item["fields"]
                for item in data.get("value", [])
            ]
            all_records.extend(records)
            
            url = data.get("@odata.nextLink")

        df = pd.DataFrame(all_records)

        print("\nSharePoint Data Loaded Successfully!")
        print(df)

        return df

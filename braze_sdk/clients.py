import requests
import json
import base64
from requests.structures import CaseInsensitiveDict
import os
import numpy as np
import random


class ExportClient(object):
    DEFAULT_ENDPOINT = 'https://rest.iad-06.braze.com'

    def __init__(self, api_key):
        self.end_point = ExportClient.DEFAULT_ENDPOINT
        self.api_key = api_key

    def ids(self, ids):
        url = f"{self.end_point}/users/export/ids"
        payload = json.dumps({
            "external_ids": ids
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        return requests.request("POST", url, headers=headers, data=payload)


class UserDataClient(object):
    DEFAULT_ENDPOINT = 'https://rest.iad-06.braze.com'

    def __init__(self, api_key):
        self.end_point = UserDataClient.DEFAULT_ENDPOINT
        self.api_key = api_key

    def add_custom_attributes(self, df, external_id_column, exclude_columns=[]):
        """Add custom attributes for list of users.

        Args:
            df (pandas dataframe): df with schema
                (eg: external_id, custom_attribute1, custom_attribute2....)
            external_id_column (str): name of the column in the dataframe
                which is external_id
            exclude_columns (list[optional]): list of columns to excludes.
        """
        url = f"{self.end_point}/users/track"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        headers["Authorization"] = f'Bearer {self.api_key}'
        attributes = []
        for i in range(len(df)):
            row = {'external_id': df.iloc[i][external_id_column]}
            for index, c in enumerate(df.columns):
                if c in exclude_columns:
                    continue
                elif 'second' in c:
                    row[c] = float(np.nan_to_num(df.iloc[i][c]))
                else:
                    row[c] = int(np.nan_to_num(df.iloc[i][c]))
            attributes.append(row)
        data = json.dumps({"attributes": attributes})
        return requests.post(url, headers=headers, data=data)

    def delete_custom_attributes(self, df):
        """Delete custom attributes specified as columns in df.

        Args:
            df (pandas dataframe): dataframe with user_id the columns to be deleted.
        """
        url = f"{self.end_point}/users/track"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        headers["Authorization"] = f'Bearer {self.api_key}'
        attributes = []
        for i in range(len(df)):
            row = {"external_id": df.iloc[i]['user_id']}
            # Setting values to None will remove the attributes
            for index, c in enumerate(df.columns):
                if c in ['shard', 'user_id']:
                    continue
                row[c] = None
            attributes.append(row)
        data = json.dumps({"attributes": attributes})
        return requests.post(url, headers=headers, data=data)

import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import argparse

from split_data import csv_files


def upload():
    SERVICE_ACCOUNT_FILE = 'credencials.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)

    csv_files={"combined.csv":"data", "train.csv":"train", "test.csv":"test"}
    client = gspread.authorize(creds)



    SPREADSHEET_ID = os.getenv('GOOGLE_SHEET_ID')
    spreadsheet = client.open_by_key(SPREADSHEET_ID)

    for k,v in csv_files.items():
        df= pd.read_csv(k)
        df.fillna('', inplace=True)
        worksheet  = spreadsheet.worksheet(v)
        worksheet.clear()
        values = df.values.tolist()
        worksheet.append_row(df.columns.tolist())
        worksheet.append_rows(values)

    print("CSV successfully uploaded to Google Sheet.")


if __name__ == "__main__":

    upload()
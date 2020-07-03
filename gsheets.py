# https://medium.com/@vince.shields913/reading-google-sheets-into-a-pandas-dataframe-with-gspread-and-oauth2-375b932be7bf

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
         'levels-282216-37bc0521c00b.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("Levels").sheet1

data = wks.get_all_values()
headers = data.pop(0)

df = pd.DataFrame(data, columns=headers)
print(df.head())
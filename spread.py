import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('dbms.json',scope)
client = gspread.authorize(creds)

sheet = client.open('info').sheet1

data= sheet.get_all_records()
result = sheet.row_values(1)
print(result)
sheet.update_cell(1,1,'CHANGED')
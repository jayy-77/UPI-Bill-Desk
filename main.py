from prettytable import PrettyTable
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

import Qr_operations

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("upibilldesk-daee7232a5ac.json", scope)
client = gspread.authorize(creds)

sheet = client.open("upi_bill_desk_data").sheet1
data_table = PrettyTable(['Index','Name','Price','Quantity'])
procduct_data_dict = sheet.get_all_records()
local_product_data = {
    'index':[],
    'product':[],
    'price':[],
    'quantity':[]
}

for i in procduct_data_dict:
    local_product_data['index'].append(i['index'])
    local_product_data['product'].append(i['product'])
    local_product_data['price'].append(i['price'])
    local_product_data['quantity'].append(i['quantity'])
    data_table.add_row([i['index'],i['product'],[i['price']],i['quantity']])
print(data_table)

choice = None
bill_amount = 0

while True:
    product_choice = input("Index <space> Quantity: ")
    iq_lst = product_choice.split()
    if product_choice != 'q':
        if local_product_data['quantity'][int(iq_lst[0])-1] - int(iq_lst[1]) >= 0:
            bill_amount += local_product_data['price'][int(iq_lst[0])-1] * int(iq_lst[1])
            local_product_data['quantity'][int(iq_lst[0])-1] -= int(iq_lst[1])
            sheet.update_cell(int(iq_lst[0])+1, 4, local_product_data['quantity'][int(iq_lst[0])-1])
        else:
            print("Insuffiecient stock")
    else:
        Qr_operations.make_upi_qr(bill_amount)
        bill_amount = 0

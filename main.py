from prettytable import PrettyTable
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import Qr_operations

#Credentials for console cloud of google
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("upibilldesk-daee7232a5ac.json", scope)
client = gspread.authorize(creds)

sheet = client.open("upi_bill_desk_data").sheet1
data_table = PrettyTable(['Index','Name','Price','Quantity'])
procduct_data_dict = sheet.get_all_records()
local_product_data = {
    'index': [],
    'product': [],
    'price': [],
    'quantity': []
}
for i in procduct_data_dict:
    local_product_data['index'].append(i['index'])
    local_product_data['product'].append(i['product'])
    local_product_data['price'].append(i['price'])
    local_product_data['quantity'].append(i['quantity'])
    data_table.add_row([i['index'],i['product'],[i['price']],i['quantity']])
print(data_table)

bill_amount = 0
l=[]
while True:
    product_choice = input("Index <space> Quantity: ")
    if product_choice != 'q':
        iq_lst = product_choice.split()
        if local_product_data['quantity'][int(iq_lst[0])-1] - int(iq_lst[1]) >= 0:
            bill_amount += local_product_data['price'][int(iq_lst[0])-1] * int(iq_lst[1])
            l += [[int(iq_lst[0])-1,int(iq_lst[1])]]
        else:
            print("Insuffiecient stock")
    else:
        Qr_operations.make_upi_qr(bill_amount)
        choice = input("Status ? Success | Failed (Y/N)")
        if choice.lower() == 'y':
            for i in l:
                local_product_data['quantity'][i[0]] -= i[1]
                sheet.update_cell(i[0]+2, 4, local_product_data['quantity'][i[0]])
            bill_amount = 0
            l = []
            break
        else:
            l = []
            bill_amount = 0
exec(open("main.py").read())
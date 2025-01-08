import json
from openpyxl import Workbook

json_file = input("Please enter your json file's name with .JSON format")
output_excel_file = "customers.xlsx"


def read_json(file_path):
    try:
        file = open(file_path, 'r')
        data = json.load(file)
        return data
    except FileNotFoundError:
        print("JSON file wasn't found!")
        return None
    except json.JSONDecodeError:
        print("Error decoding the JSON file!")
        return None


def write_to_excel(customers, output_file):
    wb = Workbook()
    ws = wb.active
    ws.title = "Customers list"
    ws.append(["name", "last name", "phone number"])
    for customer in customers:
        ws.append([customer.get("first_name"), customer.get("last_name"), customer.get("phone")])

    wb.save(output_file)
    print(f"Excel file successfully saved with the name{output_excel_file}")


customers_data = read_json(json_file)
write_to_excel(customers_data, output_excel_file)
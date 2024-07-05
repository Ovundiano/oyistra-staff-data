import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('oyistra-staff-data')

def get_employee_data():
    """
    Get employee details input from the user
    """
    print("Enter employee details")
    print("Details should be Emp No, Position, Emp Name, Age, Wages, Contract Hours")
    print("Emp No must be a whole number not decimal, Position should be the rank of emp, Emp Name should be alphabets not numbers, Age should be whole number not decimal, Wages should be numbers, Contract Hours can be whole or decimal number, should be separated by commas")
    print("Example: 001, Sales Manager, Robert Albert, 20, 30000, 42\n")

    data_str = input("Enter employee details: ")
    print(data_str)

get_employee_data()


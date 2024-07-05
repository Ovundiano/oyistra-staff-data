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
    print("Details should be 6 value: Emp No, Position, Emp Name, Age, Wages, Contract Hours")
    print("Emp No must be a whole number not decimal, Position should be the rank of emp, Emp Name should be alphabets not numbers, Age should be whole number not decimal, Wages should be numbers, Contract Hours can be whole or decimal number which should be separated by commas")
    print("Example: 001, Sales Manager, Robert Albert, 20, 30000, 42\n")

    data_str = input("Enter employee details: ")

    employee_data = data_str.split(",")
    validate_data(employee_data)

def validate_data(details):
    """
    Inside the details, convert Emp No and Age string into integers, Wages and Contract Hours strings into integers or floats.
    Raise ValueError if strings cannot be converted into integers or floats,
    or if there aren't the same 6 details.
    """
    try:
        if len(details) != 6:
            raise ValueError(
                f"Incomplete details entered, 6 details are required and you entered {len(details)}"
            )
    except ValueError as e:
        print(f"invalid data: {e}, please try again./n")

get_employee_data()


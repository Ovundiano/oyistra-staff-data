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

data = SHEET.worksheet('data')

details = data.get_all_values()

def get_employee_data():
    """
    Get employee details input from the user
    """
    print("Enter employee details.\n")
    print("Details should be 6 value: Emp No, Position, Emp Name, Age, Wages, Contract Hours.\n")
    print("Emp No must be a whole number not decimal, Position should be the rank of the employee, Emp Name should be in alphabets not numbers, Age should be whole number not decimal, Wages should be numbers, Contract Hours can be whole or decimal number and each details should be separated by commas.\n")
    print("Example: 001,Sales Manager,Robert Albert,20,30000,42\n")

    detail_str = input("Enter employee details: ")

    employee_detail = detail_str.split(",")
    validate_data(employee_detail)

def validate_data(details):
    """
    Inside the details, convert Emp No and Age string into integers, Wages and Contract Hours strings into integers or floats.
    Raise ValueError if strings cannot be converted into integers or floats,
    or if there aren't the same 6 details.
    """
    try:
        if not details[0].isdigit():
            raise ValueError(
                f"Invalid data type for {details[0]}. Expected EmpNo in integer"
            )
        if not is_alpha_or_space(details[1]):
            raise ValueError(
                f"Invalid data type for {is_alpha_or_space(details[1])}. Expected employee position in alphabet"
            )
        if not is_alpha_or_space(details[2]):
            raise ValueError(
                f"Invalid data type for {is_alpha_or_space(details[2])}. Expected employee name in alphabet"
            )
        if not details[3].isdigit():
            raise ValueError(
                f"Invalid data type for {details[3]}. Expected employee age in integer"
            )
        if not details[4].isdigit():
            raise ValueError(
                f"Invalid data type for {details[4]}. Expected employee wages in integer"
            )
        if not details[5].isdigit():
            raise ValueError(
                f"Invalid data type for {details[5]}. Expected employee contract hours in digit"
            )
        if len(details) != 6:
            raise ValueError(
                f"Invalid list of employee details entered, 6 details are required and you entered {len(details)} details"
            )
    except ValueError as e:
        print(f"Validation error: {e}, please try again.\n")



get_employee_data()




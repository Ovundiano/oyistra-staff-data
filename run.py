import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Style

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

def get_employee_detail():
    """
    Get employee details input from the user.
    Run a while loop to collect a valid string of employee details from users
    via the terminal, which must be a string of numbers and alphabets separated
    by commas. The loop will repeatedly request employee details, until details provided are valid.
    """
    while True:
        print("{Fore.YELLOW}Example: 001,Sales Manager,Robert Albert,20,30000,42\n")

        detail_str = input("Enter employee details:\n")

        employee_detail = detail_str.split(",")
        
        if validate_data(employee_detail):
            print("Employee details are valid!")
            break

    return employee_detail

def validate_data(details):
    """
    Inside the details, convert Emp No and Age string into integers, Wages and Contract Hours strings into integers or floats.
    Raise ValueError if strings cannot be converted into integers or floats,
    or if there aren't the same 6 details.
    """
    try:
        if len(details) != 6:
            raise ValueError(
                f"Invalid list of employee details entered,6 details are required and you entered {len(details)} details"
            )

        if not details[0].isdigit():
            raise ValueError(
                f"Invalid data type for {details[0]}. Expected EmpNo in digit"
            )

        if not is_alpha_or_space(details[1]):
            raise ValueError(
                f"Invalid data type for {(details[1])}. Expected employee position in alphabet"
            )

        if not is_alpha_or_space(details[2]):
            raise ValueError(
                f"Invalid data type for {(details[2])}. Expected employee name in alphabet"
            )

        if not details[3].isdigit():
            raise ValueError(
                f"Invalid data type for {details[3]}. Expected employee age in digit"
            )

        if not details[4].isdigit():
            raise ValueError(
                f"Invalid data type for {details[4]}. Expected employee annual wages in digit"
            )

        if not details[5].isdigit():
            raise ValueError(
                f"Invalid data type for {details[5]}. Expected employee contract hours in digit"
            )

    except IndexError:
        raise ValueError("List doesn't have enough items")

    except ValueError as e:
        print(f"Validation error: {e}, please try again.\n")
        return False

    return True

def is_alpha_or_space(string):
    for char in string:
        if not char.isalpha() or char.isspace():
            return False
        return True

def update_employee_data_worksheet(detail):
    """Update data worksheet with list of new employee details provided."""
    print("Updating worksheet with employee details entered...\n")
    detail_worksheet = SHEET.worksheet("data")
    detail_worksheet.append_row(detail)
    print("You have successfully updated employee data in worksheet.\n")

def main_employee_detail():
    """Run all functions in program"""
    detail = get_employee_detail()
    update_employee_data_worksheet(detail)

print(f"""
Welcome to Oyistra Staff Data Storage Board\n
Enter employee details.\n
Details should be 6 value: Emp No, Position, Emp Name, Age, Wages, Contract Hours.\n
Emp No must be a whole number not decimal, Position should be the rank of the employee in alphabets, Name should be in alphabets not numbers, Age, Wages and Contract Hours should be whole numbers not decimal and each details should be separated by commas.\n
""")
main_employee_detail()

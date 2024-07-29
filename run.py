import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore
from simple_term_menu import TerminalMenu
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('oyistra-staff-data')

data = SHEET.worksheet("data")

details = data.get_all_values()


def get_employee_detail():
    """
    Get employee details input from the user.
    Run a while loop to collect a valid string of employee details from users
    via the terminal, which must be a string of numbers and alphabets separated
    by commas.
    The loop will repeatedly request employee details, until details
    are valid.
    """
    while True:
        print(Fore.RED + "Example: 001,Sales Manager,Ovunda Eche,20,30000,42\n")

        detail_str = input(Fore.WHITE + "Enter employee details:\n")

        employee_detail = detail_str.split(",")
        if validate_data(employee_detail):
            print(Fore.YELLOW + "Employee details are valid!\n")
            break

    return employee_detail


def validate_data(details):
    """
    Inside the details, convert Emp No, Age, Wages and Contract Hours strings
    into integers.
    Raise ValueError if strings cannot be converted into integers
    or if the details are not 6 details.
    """
    try:
        if len(details) != 6:
            raise ValueError(f"""
{Fore.RED}Invalid list of employee details entered, 6 details are required and
you entered {len(details)} details""")

        if not details[0].isdigit():
            raise ValueError(f"""
{Fore.RED}Invalid data type enetered for Employee No. You enetered {details[0]}
expected Employee No in whole number""")

        if not is_alpha_or_space(details[1]):
            raise ValueError(f"""
{Fore.RED}Invalid data type entered for employee position, You enetered
{(details[1])}. Expected employee position in letters""")

        if details[1] not in ["sales manager", "sales consultant", "sales representative", "finance officer", "human resources"]:
            raise ValueError(f"""
{Fore.RED}You enetered {(details[1])} as employee position. Employee position
should either be sales consultant, sales manager, human resources, 
finance officer or sales representative""")
        else:
            is_alpha_or_space(details[1])

        if not is_alpha_or_space(details[2]):
            raise ValueError(f"""
{Fore.RED}Invalid data type enetered for employee name, You enetered
{(details[2])}. Expected employee name in letters""")

        if not details[3].isdigit():
            raise ValueError(f"""
{Fore.RED}Invalid data type enetered for employee age, You enetered
{details[3]}. Expected employee age in whole numbers""")

        if int(details[3]) < 18:
            raise ValueError(f"""
{Fore.RED}You enetered {details[3]} as employee age. Employee age entered
is below 18!""")
        elif int(details[3]) > 65:
            raise ValueError(f"""
{Fore.RED}You enetered {details[3]} as employee age. Employee age entered is
above 65!""")
        else:
            details[3].isdigit()

        if not details[4].isdigit():
            raise ValueError(f"""
{Fore.RED}Invalid data type enetered for wages, You entered {details[4]}.
Expected employee wages in numbers""")

        if int(details[4]) < 35000:
            raise ValueError(f"""
{Fore.RED}You enetered {details[4]} as employee wages. Employee wages entered
is below 35000!""")
        elif int(details[4]) > 65000:
            raise ValueError(f"""
{Fore.RED}You enetered {details[4]} as employee wages. Employee wages entered
is above 65000!""")
        else:
            details[4].isdigit()

        if not details[5].isdigit():
            raise ValueError(f"""
{Fore.RED}Invalid data type entered for contract hours, You enetered
{details[5]}. Expected employee contract hours in numbers""")

        if int(details[5]) < 16:
            raise ValueError(f"""
{Fore.RED}You enetered {details[5]} as contract hours. Contract hours entered
is less than 16hours!""")
        elif int(details[5]) > 42:
            raise ValueError(f"""
{Fore.RED}You enetered {details[5]} as contract hours. Contract hours entered
is more than 42hours!""")
        else:
            details[5].isdigit()

    except IndexError:
        raise ValueError("List doesn't have enough items")

    except ValueError as e:
        print(Fore.WHITE + f"Validation error: {e}, please try again.\n")
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
    print(f"""{Fore.YELLOW}You have successfully updated employee data in
        worksheet.\n""")


def view_employee_details_entered():
    """Collects columns of employee details from data worksheet and returning
    the datas as a list of lists."""
    detail_worksheet = SHEET.worksheet("data")
    columns = []
    for ind in range(1, 7):
        column = detail_worksheet.col_values(ind)
        columns.append(column)
        print(tabulate(columns[-1]))


def main():
    """Run all functions in program"""
    # Shows welcoming message
    print(Fore.WHITE + f"""
Welcome to Oyistra Staff Data Storage Board\n
Please, pick an option in the {Fore.RED}menu!
    """)
    options = ["1. Enter Employee Details", "2. View Employee Details Entered",
               "3. Exit"]
    exitting = False
    while exitting is not True:
        main_menu = TerminalMenu(options)
        menu_option_index = main_menu.show()
        menu_options_choice = options[menu_option_index]
        if menu_options_choice == "3. Exit":
            print(Fore.YELLOW + f"""
Good bye from Oyistra Staff Storage Data Board!
See You Later!
            """)
            exitting = True
        elif menu_options_choice == "2. View Employee Details Entered":
            print(f"""{Fore.YELLOW}These are the details of Oyistra Staff
            in the storage board.\n""")
            view_employee_details_entered()
        else:
            if menu_options_choice == "1. Enter Employee Details":
                print(f"""
{Fore.WHITE}Enter employee details.\n
{Fore.RED}Details should be 6 values: Emp No, Position, Emp Name, Age, Wages,
Contract Hours.\n
{Fore.WHITE}Emp No must be a whole number not decimal, Position should be the
department of the employee in letters, Name should be in letters not numbers,
Age,Wages and Contract Hours should be whole numbers not decimal and each
details should be separated by commas.\n
            """)
                detail = get_employee_detail()
                update_employee_data_worksheet(detail)
            else:
                menu_option_index = main_menu.show()


main()

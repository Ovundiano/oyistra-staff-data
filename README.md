# OYISTRA-STAFF-DATA

![Responsive-Mock-heroku](documentation/responsive-heroku-view.png)
![Responsive-Mock-spreadsheet](documentation/spreadsheet.png)

  Oyistra Staff Data is a website designed for the collection of employees details.

  Employee details ranges from the employee numbers, positions, names, wages, ages and contract hours.
  Below are the links to oyistra-heroku where employee details are entered and oyistra-spreadsheet where details are stored.

[oyistra-heroku](https://oyistra-staff-data-3f59f12d77b3.herokuapp.com/) [oyistra-spreadsheet](https://docs.google.com/spreadsheets/d/1kHBdajrLnGRutdMd_iQ3cj9XT7uqmDMTrZvOMFGT_Bw/edit?gid=0#gid=0)

## How to access the oyistra staff data:

- Enter link [link](https://oyistra-staff-data-3f59f12d77b3.herokuapp.com/) alternatively you can also copy the link: `https://oyistra-staff-data-3f59f12d77b3.herokuapp.com` and paste it in the browser.
- Wait for the page to load and then you click 'RUN PROGRAM'.
- Choose from the options displayed.
- Enter employee details.
- View employee details entered.
- Exit.

## Users experience
- As a user what comes to your mind at first is to understand what oyistra staff data entails.
- How to key in the necessary details required as a user.
- How to view details entered.
- How to exit the program once the valid details has been entered.

## Features

- **When the program is loaded**

- The user will be ushered in with a welcoming message.
- - Shows the terminal menu with three options:

    1. Enter Employee Details;

    1. View Employee Details Entered;

    1. Exit;

![welcome-message](documentation/welcome-message.png)

The user can manipulate the terminal menu with the arrow keys to choose an option and the enter key to confirm the choice.

- **When the user chooses "Enter Employee Details**

The User will see instructions with an example of how to enter empolyee details and where to enter employee details.

![enter-employee-details](documentation/enter-employee-details.png)

- **When the user enters invalid employee details**

When the user enters details that is not equal to six, the user will see an error message and a provision to re-enter employee details.

![error-message](documentation/error-message-1.png)

When the user enter words in place of numbers for Emp No, the user will see an error message and a provision to re-enter employee details.

![error-message](documentation/error-message-2.png)

When a user enters numbers in place of words for Position, the user will see an error message and a provision to re-enter employee details.

![error-message](documentation/error-message-3.png)

When a user enters numbers in place of words for Name, the user will see an error message and a provision to re-enter employee details.

![error-message](documentation/error-message-4.png)

When the user enter words in place of numbers for Age, the user will see an error message and a provision to re-enter employee details.

![error-message](documentation/error-message-5.png)

When the user enter words in place of numbers for Wages, the user will see an error message and a provision to re-enter employee details.

![error-message](documentation/error-message-6.png)

When the user enter words in place of numbers for Contract Hours, the user will see an error message and a provision to re-enter employee details.

![error-message](documentation/error-message-7.png)

- **When the user enters valid details**

The user will see a message of employee details are valid and updating of worksheet.
Below the validatory message, the user can find the terminal menu with the options to enter employee details, view employee details or exit.

![valid-details](documentation/valid-message.png)

- **When the user chooses "View Employee Details Entered"**

The user sees the details of all employees data that has been entered in the spreadsheet.
Below the etails of all employees data that has been entered, the user can find the terminal menu with the options to enter employee details, view employee details or exit.

![view-details](documentation/view-employee-details-.png)

- **When the user chooses "Exit"**

The user will see a goodbye message, and the program will be stopped.

![exit-program](documentation/exit-program.png)

## Technologies Used

### Language:

- [Python 3.8.5](https://www.python.org/downloads/release/python-385/)

### Frameworks/Libraries and Tools:
#### Python modules/packages:


##### Third-party imports:

- [Simple Terminal Menu](https://pypi.org/project/simple-term-menu/) was used for the implementation of menu.
- [Colorama](https://pypi.org/project/colorama/) was used to add colors and styles to the project.

#### Other tools:

- [Gitpod](https://gitpod.io/workspaces/) was used as the main tool to write and edit code.
- [GitHub](https://github.com/) was used to host the code of the website.
- [heroku.com](https://www.heroku.com/) was used for the deployment of project.
- [am i responsive](https://ui.dev/amiresponsive) was used to screenshot devices for responsive design for README purpose.


# OYISTRA-STAFF-DATA

![Responsive-Mock-heroku](documentation/responsive-mock-heroku.png)
![Responsive-Mock-spreadsheet](documentation/responsive-mock-spreadsheet.png)

  Oyistra Staff Data is a website designed for the collection of employees details.

  Employee details ranges from the employee numbers, positions, names, wages, ages and contract hours.
  Below are the links to oyistra-heroku where employee details are entered and oyistra-spreadsheet where details are stored.

[oyistra-heroku-link](https://oyistra-staff-data-3f59f12d77b3.herokuapp.com)

[oyistra-spreadsheet-link](https://docs.google.com/spreadsheets/d/1kHBdajrLnGRutdMd_iQ3cj9XT7uqmDMTrZvOMFGT_Bw/edit?gid=0#gid=0)

## How to access the oyistra staff data:

- Enter the [link](https://oyistra-staff-data-3f59f12d77b3.herokuapp.com/) alternatively you can also copy the link: `https://oyistra-staff-data-3f59f12d77b3.herokuapp.com` and paste it in the browser.
- Wait for the page to load and then you click 'RUN PROGRAM'.
- Choose from the options displayed.
1.  Enter employee details.
2.  View employee details entered.
3.  Exit.

## Users experience
- As a user what comes to your mind at first is to understand what oyistra staff data entails.
- How to key in the necessary details required as a user.
- How to view details entered.
- How to exit the program once the valid details has been entered.

## Features

- **When the program is loaded**

- The user will be ushered in with a welcoming message.
- Shows the terminal menu with three options:

1. Enter Employee Details;

2. View Employee Details Entered;

3. Exit;

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

## Bugs

### Solved bugs
1. The function ```view_employee_details_entered``` did not give the correct list of employee detials entered. It was duplicating the list with increase from one to six list of lists.

 - *Solutions:* I added [-1] to the pprint(columns) and it printed the correct output of lists items.

     ```python
     def view_employee_details_entered():
    """Collects columns of employee details from data worksheet and returning the datas as a list of lists."""
    detail_worksheet = SHEET.worksheet("data")
    columns = []
    for ind in range(1, 7):
        column = detail_worksheet.col_values(ind)
        columns.append(column)
        pprint(columns[-1])
    ```

2. The method ```if not details[].isalpha()``` was raising ValueError when alphabets was entered with space.

  - *Solutions:* I added a function ```is_alpha_or_space(string)```. Instead of checking if the string isalpha(), we'll check if our function is_alpha_or_space(), it returns false when we pass the string to it and also updated the use in the function ```validate_data(details)```

  ```python
  is_alpha_or_space(string):
    for char in string:
        if not char.isalpha() or char.isspace():
            return False
        return True
  ```
  ```python
  if not is_alpha_or_space(details[])
  ```

### Unsolved Bugs

  - None.

## Testing

### Validator

- **run.py**
 - No errors were found when passed through the official [Pep8 Python Validator](https://pep8ci.herokuapp.com/). This checking was done manually by copying python code and pasting it into the validator.

![Python Validator](documentation/python-validator-1.png)

- Github does not show the last empty line in the file, I added a screenshot of it. The screenshot shows that the code is structured according to PEP8 requirements.

![Python Validator](documentation/python-validator-2.png)

## Deployment

- The program was deployed to [Heroku](https://dashboard.heroku.com).

### To deploy the project to Heroku so it can be run as a remote web application:
- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/Ovundiano/oyistra-staff-data.git`

  1. Create your own GitHub repository to host the code.
  1. Run the command `git remote set-url origin <Your GitHub Repo Path>` to set the remote repository location to your repository.

  1. Push the files to your repository with the following command:
  `git push`
  1. Create a Heroku account if you don't already have one here [Heroku](https://dashboard.heroku.com).
  1. Create a new Heroku application on the following page here [New Heroku App](https://dashboard.heroku.com/apps):

      - ![New Heroku App](documentation/new-app.png)

  1. Go to Setting tab:

      - ![Setting Tab](documentation/setting.png)

      

  2. Go to the Deploy tab:

      - ![Deploy Tab](documentation/deploy.png)

      - ![Deployment Method](documentation/deployment/deployment_method.png)

  1. Link your GitHub account and connect the application to the repository you created.

      - ![Link GitHub account](documentation/deployment/link_to_github.png)

  1. Go to the Settings tab:
  
      - ![Settings Tab](documentation/deployment/settings_tab.png)

  1. Click "Add buildpack":

      - ![Add Buildpack](documentation/deployment/add_buildpack.png)

  1. Add the Python and Node.js buildpacks in the following order:

      - ![Add Python and Node.js](documentation/deployment/add_python_and_node_js.png)

  1. Click "Reveal Config Vars."

      - ![Reveal Config Vars](documentation/deployment/reveal_config_vars.png)

  1. Add 1 new Config Vars:
      - Key: PORT Value: 8000
      - *This Config was provided by [CODE INSTITUTE](https://codeinstitute.net/)*.

  1. Go back to the Deploy tab:

      - ![Deploy Tab](documentation/deployment/deploy_tab.png)

  1. Click "Deploy Branch":

      - ![Deploy Branch](documentation/deployment/deploy_branch.png)

      - Wait for the completion of the deployment.

      - ![Deploying Branch](documentation/deployment/deploying_branch.png)

  1. Click "Open app" to launch the application inside a web page.

      - ![View Button](documentation/deployment/view_app.png)

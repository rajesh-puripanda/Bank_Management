# NOTE Imports for inquirer py, for interactive and colourful inputs and validation
from InquirerPy import inquirer
from InquirerPy.validator import NumberValidator
from InquirerPy import get_style
import os
import re
import sys

# NOTE Importing Console from Rich Library to print out colourful statements in the console
from rich.console import Console

# NOTE Overwriting the given styles with a theme that fits our Project
style = get_style({"questionmark": "#97bff5", "answermark":"#1a73e8 bold","answer": "#1a73e8 bold","input":"#97bff5","validator":"#fff"}, style_override=False)

console = Console()
sys.path.append(os.path.realpath("."))

# NOTE Importing the main file to route after successful authentication
from main_project import app

# TODO - UserID validation -> Validating if User Exists or not
def userID_validation(result) -> bool:
    """Ensure the input is not empty."""
    return len(result) > 0


# Using File I/O Processes for Remember me functionality
with open("C:\\Users\\Naresh\\Downloads\\Banking\\MAIN\\login_credential.txt", "r") as login_details:
    userID = login_details.readline()
    password = login_details.readline()
    console.print("Authentication", style="bold underline blue", end='\n \n')

    if not (userID):
        userID = inquirer.text(message="Enter your User ID ?", style=style,validate=userID_validation).execute()

        # TODO - Fetch from the database
        original_password = "1234"

        password = inquirer.secret(
        message="Enter your password:",
        transformer=lambda _: "[Authenticated]",
        validate=lambda text: text == original_password,style=style,
        invalid_message=" Incorrect password ",
    ).execute()

        remember_me  = False
        remember_me = inquirer.confirm(message="Remember Me?", default=True,style=style,).execute()
        if remember_me:
            # TODO - Save it in file login credentials 
            pass

        app(userID.strip())
        
    else:
        # TODO - Validate Password
        console.print("[Authenticated]", style="bold blue on white")
        app(userID.strip())

# NOTE Imports for Rich Module ( used in the project for colourful highlighting of text in the console)
# NOTE Imports for inquirer py, for interactive and colourful inputs and validation
from InquirerPy import inquirer
from InquirerPy import get_style
import os
import re
import sys

from pprint import pprint
from rich.console import Console

console = Console()
sys.path.append(os.path.realpath("."))

# NOTE Overwriting the given styles with a theme that fits our Project
style = get_style({"questionmark": "#97bff5", "answermark":"#1a73e8 bold","answer": "#1a73e8 bold","input":"#97bff5","validator":"#fff"}, style_override=False)

username = ""

# NOTE - Basically an anchor to the menu at all inner routes from this file
def proceed():
    proceed = False
    proceed = inquirer.confirm(message="Proceed?", default=True, style=style).execute()
    if proceed:
        main()


# NOTE About the project and credit to Mr. Pius Mathew Sir

def about_project():
    print()    
    console.print('''Welcome to [bold white on blue underline] the Bank [/bold white on blue underline]! 

Experience innovative banking, top-notch security, and personalized service with us. Together, we are redefining the future of finance.

[bold underline]Team Members:[/bold underline]
1. [bold blue on white] Rajesh Kumar Puripanda ( Team Leader ) [/bold blue on white]
2. [bold blue on white] Sreesankar Jagadeesh [/bold blue on white]
3. [bold blue on white] Ismail Ali [/bold blue on white]
4. [bold blue on white] Jeel Ramoliya [/bold blue on white]

We extend our heartfelt thanks to [bold white on blue] Mr. Pius Mathew [/bold white on blue] for his invaluable support. ''')
    print('\n')
    proceed()

def main():
    print()    
    console.print(f" Welcome {username} ".format(username), style="bold uu white on blue")
    print()

    action = inquirer.select(
        message="How may we assist you!",
        choices=[
            "Transactions","Loans / Deposits", "Accounts", "Beneficiary", "Cards","Financial Calculator", "About the Bank ( Project )", "Exit"
        ],
        style=style,
    ).execute()


    if (action=="About the Bank ( Project )"):
        about_project()
    else:
        console.print(" Thank you for choosing ISB Bank. ", style="bold black on white")
        
def admin_main():
    print("Admin")

    
def app(name):
    print("\n \n")
    console.print('''[#abdcff]██╗███████╗██████╗     ██████╗  █████╗ ███╗   ██╗██╗  ██╗[/#abdcff]
[#83cbff]██║██╔════╝██╔══██╗    ██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝[/#83cbff]
[#65bfff]██║███████╗██████╔╝    ██████╔╝███████║██╔██╗ ██║█████╔╝ [/#65bfff]
[#4ab4ff]██║╚════██║██╔══██╗    ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ [/#4ab4ff]
[#1ea1ff]██║███████║██████╔╝    ██████╔╝██║  ██║██║ ╚████║██║  ██╗[/#1ea1ff]
[#0396ff]╚═╝╚══════╝╚═════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝[/#0396ff]''', style="bold")
    print("\n")    
    if (name.lower().strip())=="admin":
        admin_main()
    else:
        global username
        username =  name
        main()
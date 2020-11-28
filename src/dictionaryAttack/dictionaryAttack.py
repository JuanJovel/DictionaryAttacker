'''
November 28, 2020

@author: Juan Jovel
@author: Sami Marzougui
'''
from pathlib import Path;

# Reads the passwords from the resource folder and returns a list containing all the passwords
# without the newline character.
def readFile() -> list:
    
    # Creates empty list of passwords.
    passwords = [];
    
    # Finds the path outside of the current directory.
    myAbsolutePath = str(Path(__file__).parent.parent.parent)
    
    # Specifies the path of the password .txt file
    passwordFilePath = myAbsolutePath+"\\res\\10-million-password-list-top-1000.txt";
    
    # Opens the file
    file = open(passwordFilePath, "r");
    
    # Adds every line to the list
    for password in file:
        passwords.append(password.strip("\n"));
    
    # Returns a list of all the passwords
    return passwords;
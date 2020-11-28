'''
November 28, 2020

@author: Juan Jovel
@author: Sami Marzougui
'''
from pathlib import Path;
import hashlib;

# Reads the passwords from the resource folder and returns a list containing all the passwords
# without the newline character.
def readFile() -> list:
    
    # Creates empty list of passwords.
    passwords = [];
    
    # Finds the path outside of the current directory.
    myAbsolutePath = str(Path(__file__).parent.parent.parent);
    
    # Specifies the path of the password .txt file
    passwordFilePath = myAbsolutePath+"\\res\\10-million-password-list-top-1000.txt";
    
    # Opens the file
    file = open(passwordFilePath, "r");
    
    # Adds every line to the list
    for password in file:
        passwords.append(password.strip("\n"));
    
    # Returns a list of all the passwords
    return passwords;

def hashString(aString: str, hashType: int) -> str:
    
    if (hashType == 512):
        # Hashes the string using Python's hashlib library
        hashedString = hashlib.sha512(aString.encode('utf-8')).hexdigest();
    
        # Returns the hashed string.
        return hashedString;
    
    else:
        # Hashes the string using Python's hashlib library
        hashedString = hashlib.sha256(aString.encode('utf-8')).hexdigest();
    
        # Returns the hashed string.
        return hashedString;
        

password = input("Enter a password: ")
hashType = int(input("Select a SHA hash (256 or 512): "))

passwordSize = len(password);

# Hashes the password
password = hashString(password, hashType)
    
passwordList = readFile();
    
# TODO: Find if a word is in a password
for element in passwordList:
    if passwordSize < len(element):
        continue;

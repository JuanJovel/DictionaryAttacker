'''

A program that performs a dictionary attack on a given password.

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

# Returns a list that excludes all the words that are bigger than the length of the password.
def optimizeDictionary(oldDictionary: list, passwordLength: int) -> list:
    
    # Optimizes the dictionary so only words within the constraints are included.
    newDictionary = [element for element in oldDictionary if len(element) <= passwordLength]
    
    return newDictionary;

originalPassword = input("Enter a password: ")
hashType = int(input("Select a SHA hash (256 or 512): "))

passwordSize = len(originalPassword);

# Hashes the password
originalPassword = hashString(originalPassword, hashType)

# Reads password list from file
passwordList = readFile();

# Adjusts the list to rule out impossible words based on the password size.
passwordList = optimizeDictionary(passwordList, passwordSize)

# Use a dictionary to keep track of the order of the password.
passwordFound = {};

# Runs through all the elements
for element in passwordList:
    # If we have figured out every word in the password, then no need to check any further.
    if (len(originalPassword) == 0):
        break;
    
    # Hash the current element.
    element = hash(element, hashType);
    
    # If the hash of the element is a substring of the password.
    if (element in originalPassword):
        # order and add to dictionary.
        pass;

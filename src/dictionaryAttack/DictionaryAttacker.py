'''

A class that performs a dictionary attack on a given password.

November 28, 2020

@author: Juan Jovel
@author: Sami Marzougui
'''
from pathlib import Path;
import hashlib;
import binascii;


class DictionaryAttacker:
    

    # Reads the passwords from the resource folder and returns a list containing all the passwords
    # without the newline character.
    def readDictionary(self) -> list:
    
        # Creates empty list of passwords.
        dictionary = [];
    
        # Finds the path outside of the current directory.
        myAbsolutePath = str(Path(__file__).parent.parent.parent);
    
        # Specifies the path of the password .txt file
        dictionaryFilePath = myAbsolutePath + "\\res\\10-million-password-list-top-1000.txt";
    
        # Opens the file
        file = open(dictionaryFilePath, "r");
    
        # Adds every line to the list
        for password in file:
            dictionary.append(password.strip("\n"));
    
        # Returns a list of all the passwords
        return dictionary;

    def hashString(self, aString: str, hashType: int) -> str:
    
        if (hashType == 512):
            # Hashes the string using Python's hashlib library
            hashedString = hashlib.pbkdf2_hmac('sha512', aString.encode('utf-8'), 'staticSalt'.encode('utf-8'), 1000)
    
            # Returns the hashed string.
            return binascii.hexlify(hashedString)
    
        else:
            # Hashes the string using Python's hashlib library
            hashedString = hashlib.pbkdf2_hmac('sha256', aString.encode('utf-8'), 'staticSalt'.encode('utf-8'), 1000)
    
            # Returns the hashed string.
            return binascii.hexlify(hashedString)


    # Returns a list that excludes all the words that are bigger than the length of the password.
    def optimizeDictionary(self, oldDictionary: list, passwordLength: int) -> list:
        
        # Rules out any words longer than the password.
        newDictionary = [element for element in oldDictionary if len(element) <= passwordLength];
        
        # TODO: Explore combinations based on the length of the password.
        
        return newDictionary;

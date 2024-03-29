'''

A class that performs a dictionary attack on a given password.

November 28, 2020

@author: Juan Jovel (jjovel99@vt.edu)
@author: Sami Marzougui (samim19@vt.edu)

'''
from pathlib import Path;
import hashlib;
import binascii;
import itertools;


class DictionaryAttacker:
    
    isCombination = False;
    numberOfGuesses = 0;
    
    def __init__(self, plainTextPassword: str, hashType: int):
        '''
        Initializes a DictionaryAttacker with a given password and type of hashing.
        
        @param plainTextPassword: The password to be cracked using the DictionaryAttacker, 
                                  only used to calculate the length.
        @param hashType: The type of hash to be used as an integer, either 256 or 512.
        '''
        self.hashType = hashType;
        self.hashedPassword = self.hashString(plainTextPassword);
        self.passwordLength = len(plainTextPassword);
        
    def readDictionary(self) -> list:
        '''
        Reads the dictionary located in the resource folder.
        
        @return A list of strings containing all the words in the dictionary text file.
        '''
    
        # Creates empty list of passwords.
        dictionary = [];
    
        # Finds the path outside of the current directory.
        myAbsolutePath = str(Path(__file__).parent.parent.parent);
    
        # Specifies the path of the password .txt file
        dictionaryFilePath = myAbsolutePath + "\\res\\10-million-password-list-top-150.txt";
    
        # Opens the file
        file = open(dictionaryFilePath, "r");
    
        # Adds every line to the list
        for password in file:
            dictionary.append(password.strip("\n"));
    
        # Returns a list of all the passwords
        return dictionary;

    def hashString(self, aString: str) -> str:
        '''
        Hashes the given string using the hash type specified in the constructor.
        
        @return The hashed string in hex.
        '''
        if (self.hashType == 512):
            # Hashes the string using Python's hashlib library
            hashedString = hashlib.pbkdf2_hmac('sha512', aString.encode('utf-8'), 'staticSalt'.encode('utf-8'), 50)
    
            # Returns the hashed string.
            return binascii.hexlify(hashedString)
    
        else:
            # Hashes the string using Python's hashlib library
            hashedString = hashlib.pbkdf2_hmac('sha256', aString.encode('utf-8'), 'staticSalt'.encode('utf-8'), 50)
    
            # Returns the hashed string.
            return binascii.hexlify(hashedString)
    
    def optimizeDictionary(self, oldDictionary: list) -> list:
        '''
        Returns a dictionary that excludes all the words that are bigger than the length of the password.
        
        @param oldDictionary: The unoptimized dictionary.
        @return A list that is optimized to crack the password.
        '''
        
        # Rules out any words longer or shorter than the password.
        if (not self.isCombination):
            newDictionary = [element for element in oldDictionary if len(element) == self.passwordLength];
        
        # TODO: Explore combinations based on the length of the password.
        else:
            # Eliminate all words that aren't strictly smaller than the password.
            newDictionary = [element for element in oldDictionary if len(element) < self.passwordLength];
            
        return newDictionary;
    
    def attack(self, dictionary: list) -> str:
        '''
        Performs a dictionary attack using the given dictionary.
        
        @param dictionary: A dictionary to use for the attack.
        @return The cracked password in string form.
        '''
        # Initializes the password found to an empty string.
        passwordFound = "";
        if (not self.isCombination):
            # Runs through the dictionary.
            for element in dictionary:
                
                #Increments the guess counter
                self.numberOfGuesses += 1;
            
                # If the hash of an element in the dictionary matches the hashed password we cracked the password.
                if (self.hashString(element) == self.hashedPassword):
                    
                    # Set the password found to the plain text element.
                    passwordFound = element;
                
                    # Exit the loop, we don't need to check any further.
                    break;
        
        # If it is a combination the combination attack method takes over.   
        else:
            passwordFound = self.__combinationAttack(dictionary);
            
        # Return the password found, will be empty if attack was unsuccessful using given dictionary.
        return passwordFound;
    
    def setIsCombination(self, newValue: bool):
        '''
        Sets the combination instance variable to the parameter.
        
        @param newValue: The new boolean value for isCombination instance variable.
        
        '''
        
        self.isCombination = newValue;
        
    def __combinationAttack(self, dictionary: list) -> str:
        '''
        Uses the itertools library to perform a dictionary attack if the password
        is a combination of words from the dictionary.
        
        @param dictionary: The dictionary to use for the attack.
        
        '''
        
        # Initializes the password found to an empty string.
        passwordFound = "";
        
        # Looks through all possible combinations of words.
        for i in range(2, len(dictionary) + 1):
            
            # Generates a combination.
            generator = itertools.product(dictionary, repeat=i);
            
            # Try-except block to handle the StopIteration when there's no more combinations.
            try:
                while(True):
                    
                    # Joins the tuple returned into a string.
                    currentGuess = ''.join(next(generator));
                    
                    # Only tries the passwords that have the same length as the one we are
                    # looking for.
                    if (len(currentGuess) == self.passwordLength):
                        # Increments guess counter.
                        self.numberOfGuesses += 1;
                        
                        # Checks if the hash matches.
                        if (self.hashString(currentGuess) == self.hashedPassword):
                            
                            # If it does we have found the password.
                            passwordFound = currentGuess;
                            return passwordFound;
            
            # If this is thrown there are no more combinations of that amount of words.
            except StopIteration:
                
                # Move on to the next amount.
                pass;
        
        # If the password wasn't found this string will be empty.
        return passwordFound;
    
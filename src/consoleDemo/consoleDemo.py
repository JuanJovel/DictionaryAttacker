'''
A console demo of the DictionaryAttacker.

November 30, 2020

@author: Juan Jovel
@author: Sami Marzougui
'''

from dictionaryAttack.DictionaryAttacker import DictionaryAttacker;

attacker = DictionaryAttacker();

originalPassword = input("Enter a password: ")
hashType = int(input("Select a SHA hash (256 or 512): "))

if (hashType != 256 and hashType != 512):
    print("SHA" + str(hashType) + " not supported...");
    print("Using SHA256")

passwordSize = len(originalPassword);

# Hashes the password
originalPassword = attacker.hashString(originalPassword, hashType)

# Reads password list from file
passwordList = attacker.readDictionary();

# Adjusts the list to rule out impossible words based on the password size.
passwordList = attacker.optimizeDictionary(passwordList, passwordSize)

# Use a dictionary to keep track of the order of the password.
passwordFound = {};

# Runs through all the elements
for element in passwordList:
    # If we have figured out every word in the password, then no need to check any further.
    if (len(originalPassword) == 0):
        break;
    
    # Hash the current element.
    element = attacker.hashString(element, hashType);
    
    # If the hash of the element is a substring of the password.
    if (element in originalPassword):
        # order and add to dictionary.
        pass;

'''
A console demo of the DictionaryAttacker.

November 30, 2020

@author: Juan Jovel
@author: Sami Marzougui
'''

from dictionaryAttack.DictionaryAttacker import DictionaryAttacker;
import time;

attacker = DictionaryAttacker();

originalPassword = input("Enter a password: ")
hashType = int(input("Select a SHA hash (256 or 512): "))

if (hashType != 256 and hashType != 512):
    print("SHA" + str(hashType) + " not supported...");
    print("Using SHA256")

passwordSize = len(originalPassword);

# Hashes the password
hashedPassword = attacker.hashString(originalPassword, hashType)

# Reads password list from file
passwordList = attacker.readDictionary();

# Maybe this should be an instance variable of the DictionaryAttacker class.
# Use a dictionary to keep track of the order of the password.
passwordFound = ""
    
# A password we will modify as we loop
testPassword = originalPassword;

startTime = time.time();

# Adjusts the list to rule out impossible words based on the password size.
passwordList = attacker.optimizeDictionary(passwordList, len(testPassword))
    
for element in passwordList:
    # Hash the current element.
    plainTextElement = element;
    hashedElement = attacker.hashString(element, hashType);
    
    # If the hash of the element is a substring of the password.
    if (hashedElement in hashedPassword):
        passwordFound = plainTextElement;
        break;
            
endTime = time.time();
print("Password was cracked using dictionary attack in: "+str(endTime-startTime)+" seconds")
print("The password is: "+ passwordFound);

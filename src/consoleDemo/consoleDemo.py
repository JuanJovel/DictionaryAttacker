'''
A console demo of the DictionaryAttacker.

November 30, 2020

@author: Juan Jovel
@author: Sami Marzougui
'''

from dictionaryAttack.DictionaryAttacker import DictionaryAttacker;
import time;


originalPassword = input("Enter a password: ")
hashType = int(input("Select a SHA hash (256 or 512): "))

attacker = DictionaryAttacker(originalPassword, hashType);

if (hashType != 256 and hashType != 512):
    print("SHA" + str(hashType) + " not supported...");
    print("Using SHA256")

# Reads password list from file
passwordList = attacker.readDictionary();

# Maybe this should be an instance variable of the DictionaryAttacker class.
passwordFound = ""

startTime = time.time();

# Adjusts the list to rule out impossible words based on the password size.
passwordList = attacker.optimizeDictionary(passwordList);

passwordFound = "";
# Preliminary attack: Will only work for a single word in the dictionary, no combinations.
passwordFound = attacker.attack(passwordList);

# If the length of the password found after the preliminary attack is zero, then the password MUST be a combination.
if (len(passwordFound) == 0):
    pass;

endTime = time.time();
print("Password was cracked using dictionary attack in: "+str(endTime-startTime)+" seconds")
print("The password is: "+ passwordFound);

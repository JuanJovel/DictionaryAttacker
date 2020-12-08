'''

A class that performs a dictionary attack on a given password.

November 28, 2020

@author: Juan Jovel
@author: Sami Marzougui

'''

from tkinter import *  # @UnusedWildImport
from tkinter import ttk  # @Reimport
from dictionaryAttack.DictionaryAttacker import DictionaryAttacker;
import time;

hashType = 0


def clicked_button1():
    password = passwordField.get()
    myHashType = hashType;
    crackPassword(password, myHashType)


def crackPassword(password: str, hashType: int):
    
    #Instantiates a new DictionaryAttacker object.
    attacker = DictionaryAttacker(password, hashType);
    
    # Reads password list from file
    passwordList = attacker.readDictionary();
    tempList = passwordList
    
    # Starts a timer
    startTime = time.time();

    # Adjusts the list to rule out impossible words based on the password size.
    passwordList = attacker.optimizeDictionary(passwordList);
    
    passwordFound = "";  # @UnusedVariable
    
    # Preliminary attack: Will only work for a single word in the dictionary, no combinations.
    passwordFound = attacker.attack(passwordList);
    
    # If the length of the password found after the preliminary attack is zero, 
    # then the password MUST be a combination.
    if (len(passwordFound) == 0):
        attacker.setIsCombination(True);
        passwordList = attacker.optimizeDictionary(attacker.readDictionary());

    # Brute-force combination attack.
    passwordFound = attacker.attack(passwordList);
    
    # Stop the timer.
    endTime = time.time();
    
    # Add the timer to the window.
    timeElapsed = "{:.2f}".format(endTime - startTime)
    if (timeElapsed == '0.00'):
        timeElapsed = '< 0.1'
    timeLabel.configure(text="Time Elapsed: " + str(timeElapsed) + " seconds")
    
    # Add info to the window.
    pwordFoundTextLabel.configure(text="Password found was: " + passwordFound)
    numGuessesTextLabel.configure(text="Number of Guesses: "+str(attacker.numberOfGuesses))
    dictSizeLabel.configure(text="Dictionary Size: " + str(len(tempList)))

def selectHash(hashTypeSelected: int):
    if (hashTypeSelected == 256):
        hashType = 256;

    elif (hashTypeSelected == 512):
        hashType = 512;


# Create window element.
root = Tk()
root.title('Dictionary Attack')
root.geometry('550x450')
rootFont = 'Candara'
style = ttk.Style()
style.configure('.', font=('Candara', 14))

# Create elements

# Labels.
subtitleLabel = ttk.Label(root, text="Try to Crack a Password", font = ('Candara', 16, "bold"))
pwordTextLabel = ttk.Label(root, text="Enter password below:")
hashTextLabel = ttk.Label(root, text="Select SHA Hashing Type:")
pwordFoundTextLabel = ttk.Label(root, text='')
numGuessesTextLabel = ttk.Label(root, text='')
timeLabel = ttk.Label(root, text="")
dictSizeLabel = ttk.Label(root, text = "")

# Password Field
passwordField = ttk.Entry(root, width=30)

# Check boxes
sha256CheckBox = ttk.Checkbutton(root, text='SHA256', command=lambda: selectHash(256))
sha512CheckBox = ttk.Checkbutton(root, text='SHA512', command=lambda: selectHash(512))

# Crack Button
crackButton = ttk.Button(root, text='Crack', command=lambda: crackPassword(passwordField.get(), hashType))


# Place elements.
subtitleLabel.grid(column=1)
hashTextLabel.grid(column=1)
sha256CheckBox.grid(column=1)
sha512CheckBox.grid(column=1)
pwordTextLabel.grid(column=1, rowspan=10)
passwordField.grid(column=1)
crackButton.grid(column=1)
timeLabel.grid(column=1)
dictSizeLabel.grid(column=1)
pwordFoundTextLabel.grid(column=1)
numGuessesTextLabel.grid(column=1)


root.mainloop()

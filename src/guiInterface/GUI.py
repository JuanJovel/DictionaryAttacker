'''

A class that performs a dictionary attack on a given password.

November 28, 2020

@author: Juan Jovel
@author: Sami Marzougui

'''

from tkinter import *
from tkinter import ttk
from dictionaryAttack.DictionaryAttacker import DictionaryAttacker;
import time;

hashType = 0


def clicked_button1():
    password = passwordField.get()
    myHashType = hashType;
    crackPassword(password, myHashType)


def crackPassword(str1: str, str2: str):
    attacker = DictionaryAttacker(str1, str2);
    # Reads password list from file
    passwordList = attacker.readDictionary();

    startTime = time.time();

    # Adjusts the list to rule out impossible words based on the password size.
    passwordList = attacker.optimizeDictionary(passwordList);

    passwordFound = "";
    # Preliminary attack: Will only work for a single word in the dictionary, no combinations.
    passwordFound = attacker.attack(passwordList);
    # If the length of the password found after the preliminary attack is zero, then the password MUST be a combination.
    if (len(passwordFound) == 0):
        attacker.setIsCombination(True);
        passwordList = attacker.optimizeDictionary(attacker.readDictionary());

    # Brute-force combination attack.
    passwordFound = attacker.attack(passwordList);

    endTime = time.time();
    timeElapsed = "{:.2f}".format(endTime - startTime)
    if (timeElapsed == '0.00'):
        timeElapsed = '< 0.1'
    timeLabel.configure(text="Time Elapsed: " + str(timeElapsed) + " seconds")
    pwordFoundTextLabel.configure(text="Password found was: " + passwordFound)
    numGuessesTextLabel.configure(text="Number of Guesses: "+str(attacker.numberOfGuesses))


def selectHash(hashTypeSelected: int):
    if (hashTypeSelected == 256):
        hashType = 256;

    elif (hashTypeSelected == 512):
        hashType = 512;


root = Tk()
root.title('Dictionary Attack')
root.geometry('800x600')
rootFont = 'Candara'
style = ttk.Style()
style.configure('.', font=('Candara', 14))

pwordTextLabel = ttk.Label(root, text="Enter password below:")
hashTextLabel = ttk.Label(root, text="Select SHA Hashing Type:")

passwordField = ttk.Entry(root, width=30)
sha256CheckBox = ttk.Checkbutton(root, text='SHA256', command=lambda: selectHash(256))
sha512CheckBox = ttk.Checkbutton(root, text='SHA512', command=lambda: selectHash(512))
# passwordField3 = Entry(root, font = ('Helvetica', 16))
# passwordField4 = Entry(root, font = ('Helvetica', 16))

crackButton1 = ttk.Button(root, text='Crack', command=clicked_button1)  # enter command = function name here
# crackButton2 = Button(root, text = 'Crack', font = ('Helvetica', 16)) #enter command = function name here
# crackButton3 = Button(root, text = 'Crack', font = ('Helvetica', 16)) #enter command = function name here
# n4 = Button(root, text = 'Crack', font = ('Helvetica', 16)) #enter command = function name here

pwordFoundTextLabel = ttk.Label(root, text='')
numGuessesTextLabel = ttk.Label(root, text='')

hashTextLabel.grid(column=1)
sha256CheckBox.grid(column=1)
sha512CheckBox.grid(column=1)
pwordTextLabel.grid(column=1, rowspan=10)
passwordField.grid(column=1)
timeLabel = ttk.Label(root, text="Time Elapsed: ")
timeLabel.grid(column=1)
# passwordField3.place(relx = 0.25, rely = 0.55, width = 200, height = 80, anchor = CENTER)
# passwordField4.place(relx = 0.25, rely = 0.75, width = 200, height = 80, anchor = CENTER)

crackButton1.grid(column=1)
pwordFoundTextLabel.grid(column=1)
numGuessesTextLabel.grid(column=1)
# crackButton2.place(relx = 0.60, rely = 0.35, width = 200, height = 80, anchor = CENTER)
# crackButton3.place(relx = 0.60, rely = 0.55, width = 200, height = 80, anchor = CENTER)
# crackButton4.place(relx = 0.60, rely = 0.75, width = 200, height = 80, anchor = CENTER)

root.mainloop()

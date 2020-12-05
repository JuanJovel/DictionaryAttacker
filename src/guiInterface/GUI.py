'''

A class that performs a dictionary attack on a given password.

November 28, 2020

@author: Juan Jovel
@author: Sami Marzougui

'''

import tkinter
from dictionaryAttack.DictionaryAttacker import DictionaryAttacker;
import time;

def clicked_button1():
    password = passwordField.get()
    hashtype = hashTypeField.get()
    crackPassword(password, hashtype)

def crackPassword(str1, str2):
    attacker = DictionaryAttacker(str1, str2);
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
        attacker.setIsCombination(True);
        passwordList = attacker.optimizeDictionary(attacker.readDictionary());

    # Brute-force combination attack.
    passwordFound = attacker.attack(passwordList);

    endTime = time.time();
    timeLabel.configure(text = "Time Elapsed " + str(endTime-startTime) + " seconds")



root = tkinter.Tk()
root.title('Dictionary Attack')

pwordTextLabel = tkinter.Label(root, text = "Enter password below:", font = ('Helvetica', 20, 'bold'))
hashTextLabel = tkinter.Label(root, text = "Enter hashType below: (256 or 512)", font = ('Helvetica', 20, 'bold'))

hashTextLabel.place(relx = 0.15, rely = 0.05, anchor = tkinter.CENTER)

passwordField = tkinter.Entry(root, font = ('Helvetica', 16))
hashTypeField = tkinter.Entry(root, font = ('Helvetica', 16))
#passwordField3 = tkinter.Entry(root, font = ('Helvetica', 16))
#passwordField4 = tkinter.Entry(root, font = ('Helvetica', 16))

crackButton1 = tkinter.Button(root, text = 'Crack', font = ('Helvetica', 16), command = clicked_button1) #enter command = function name here
#crackButton2 = tkinter.Button(root, text = 'Crack', font = ('Helvetica', 16)) #enter command = function name here
#crackButton3 = tkinter.Button(root, text = 'Crack', font = ('Helvetica', 16)) #enter command = function name here
#n4 = tkinter.Button(root, text = 'Crack', font = ('Helvetica', 16)) #enter command = function name here


hashTextLabel.place(relx = 0.25, rely = 0.05, anchor = tkinter.CENTER)
pwordTextLabel.place(relx = 0.25, rely = 0.30, anchor = tkinter.CENTER)

timeLabel = tkinter.Label(root, text = "Time Elapsed: ", font = ('Helvetica', 20))
timeLabel.place(relx = 0.55, rely = 0.4, anchor = tkinter.CENTER)

passwordField.place(relx = 0.25, rely = 0.4, width = 200, height = 80, anchor = tkinter.CENTER)
hashTypeField.place(relx = 0.25, rely = 0.15, width = 200, height = 80, anchor = tkinter.CENTER)
#passwordField3.place(relx = 0.25, rely = 0.55, width = 200, height = 80, anchor = tkinter.CENTER)
#passwordField4.place(relx = 0.25, rely = 0.75, width = 200, height = 80, anchor = tkinter.CENTER)

crackButton1.place(relx = 0.60, rely = 0.15, width = 200, height = 80, anchor = tkinter.CENTER)
#crackButton2.place(relx = 0.60, rely = 0.35, width = 200, height = 80, anchor = tkinter.CENTER)
#crackButton3.place(relx = 0.60, rely = 0.55, width = 200, height = 80, anchor = tkinter.CENTER)
#crackButton4.place(relx = 0.60, rely = 0.75, width = 200, height = 80, anchor = tkinter.CENTER)


root.mainloop()

'''

A class that performs a dictionary attack on a given password.

November 28, 2020

@author: Juan Jovel
@author: Sami Marzougui

'''
import tkinter
from tkinter import *  # @UnusedWildImport
from tkinter import ttk  # @Reimport
from dictionaryAttack.DictionaryAttacker import DictionaryAttacker;
import time;
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sets up fields that will be used in several functions
hashType = 0
hasPlotted = False

# Initializes arrays to store data to be plotted
timeArr256 = []
pwordLengArr256 = []
numGuessArr256 = []
timeArr512 = []
pwordLengArr512 = []
numGuessArr512 = []


# Cracks a password with the given password and hash type
def crackPassword(password: str, hashType: int):
    
    # Instantiates a new DictionaryAttacker object.
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
    numGuessesTextLabel.configure(text="Number of Guesses: " + str(attacker.numberOfGuesses))
    dictSizeLabel.configure(text="Dictionary Size: " + str(len(tempList)))
    
    # Checks which hashType was used, and add the information to the
    # different arrays
    if (hashType == 256):
        timeArr256.append(endTime - startTime)
        pwordLengArr256.append(len(passwordFound))
        numGuessArr256.append(attacker.numberOfGuesses)
    
    elif (hashType == 512):
        timeArr512.append(endTime - startTime)
        pwordLengArr512.append(len(passwordFound))
        numGuessArr512.append(attacker.numberOfGuesses)
    

# Plots both plots of the SHA-256
def plot256Plots():
    global hasPlotted, canvas1, canvas2
    
    # Checks if there already is a plot
    if (not hasPlotted):
        # Calls both plot functions for SHA-256
        plot256Plot1()
        plot256Plot2()
        
        # Sets the plot to true
        hasPlotted = True
        
        # Changes the button to a reset plot button and removes the other button
        plot256Button.configure(text = "Reset Plots")
        plot512Button.grid_forget()
    
    elif (hasPlotted):
        # Remove the old plots
        canvas1.get_tk_widget().destroy()
        canvas2.get_tk_widget().destroy()
        
        # Sets the plot back to false
        hasPlotted = False
        
        # Changes the button back, and reads the other plot button
        plot256Button.configure(text = "Plot SHA-256 Results")
        plot512Button.grid(column=2, row = 4)
        

def plot512Plots():
    global hasPlotted, canvas1, canvas2
    
    # Checks if there already is a plot
    if (not hasPlotted):
        # Calls both plot functions for SHA-512
        plot512Plot1()
        plot512Plot2()
        
        # Sets the plot to true
        hasPlotted = True
        
        # Changes the button to a reset plot button and removes the other button
        plot512Button.configure(text = "Reset Plots")
        plot256Button.grid_forget()

    elif (hasPlotted):
        # Remove the old plots
        canvas1.get_tk_widget().destroy()
        canvas2.get_tk_widget().destroy()
        
        # Sets the plot back to false
        hasPlotted = False
        
        # Changes the button back, and reads the other plot button
        plot512Button.configure(text = "Plot SHA-512 Results")
        plot256Button.grid(column=2, row = 3)

# Creates a plot of password length vs time for the SHA-512
def plot512Plot1():
    global canvas1
    
    # Creates a figure and subplot
    fig = Figure(figsize=(7, 4), dpi=100) 
    plot1 = fig.add_subplot(111)
    
    # Plots a scatterplot  of length vs time
    plot1.scatter(pwordLengArr512, timeArr512) 
    
    # Adds labels to the scatter plot
    fig.suptitle('The Length of the Password vs Time it Takes to Crack')
    plot1.set_xlabel('Length of Password (# of characters)')
    plot1.set_ylabel('Time to Crack (seconds)')
    
    # Creates the Tkinter canvas 
    canvas1 = FigureCanvasTkAgg(fig, master=root)   
    canvas1.draw() 
  
    # Places the canvas on the Tkinter window 
    canvas1.get_tk_widget().place(relx = 0.6, rely = 0.25, anchor = tkinter.CENTER) 


# Creates a plot of password length vs time for the SHA-256
def plot256Plot1():
    global canvas1

    # Creates a figure and subplot
    fig = Figure(figsize=(7, 4), dpi=100) 
    plot1 = fig.add_subplot(111)
    
    # Plots a scatterplot  of length vs time   
    plot1.scatter(pwordLengArr256, timeArr256)
    
    # Adds labels to the scatter plot    
    fig.suptitle('The Length of the Password vs Time it Takes to Crack')
    plot1.set_xlabel('Length of Password (# of characters)')
    plot1.set_ylabel('Time to Crack (seconds)')
  
    # Creates the Tkinter canvas 
    canvas1 = FigureCanvasTkAgg(fig, master=root)   
    canvas1.draw() 
  
    # Places the canvas on the Tkinter window 
    canvas1.get_tk_widget().place(relx = 0.6, rely = 0.25, anchor = tkinter.CENTER)


# Creates a plot of password length vs number of guesses for the SHA-512  
def plot512Plot2():
    global canvas2

    # Creates a figure and subplot
    fig = Figure(figsize=(7, 4), dpi=100) 
    plot1 = fig.add_subplot(111)
    
    # Plots a scatterplot  of length vs time
    plot1.scatter(pwordLengArr512, numGuessArr512, c = 'red') 
    
    # Adds labels to the scatter plot   
    fig.suptitle('The Length of the Password vs The Number of Guesses')
    plot1.set_xlabel('Length of Password (# of characters)')
    plot1.set_ylabel('Number of Guesses')
    
    # Creates the Tkinter canvas 
    canvas2 = FigureCanvasTkAgg(fig, master=root)   
    canvas2.draw() 
  
    # Places the canvas on the Tkinter window 
    canvas2.get_tk_widget().place(relx = 0.6, rely = 0.75, anchor = tkinter.CENTER)
    


# Creates a plot of password length vs number of guesses for the SHA-256 
def plot256Plot2():
    global canvas2
    
    # Creates a figure and subplot
    fig = Figure(figsize=(7, 4), dpi=100) 
    plot1 = fig.add_subplot(111)

    # Plots a scatterplot  of length vs time
    plot1.scatter(pwordLengArr256, numGuessArr256, c = 'red')
    
    # Adds labels to the scatter plot   
    fig.suptitle('The Length of the Password vs The Number of Guesses')
    plot1.set_xlabel('Length of Password (# of characters)')
    plot1.set_ylabel('Number of Guesses')
  
    # Creates the Tkinter canvas 
    canvas2 = FigureCanvasTkAgg(fig, master=root)   
    canvas2.draw() 
  
    # Places the canvas on the Tkinter window 
    canvas2.get_tk_widget().place(relx = 0.6, rely = 0.75, anchor = tkinter.CENTER)
 

# Create window element.
root = Tk()
root.title('Dictionary Attack')

# Display in full-screen
root.state('zoomed')

rootFont = 'Candara'
style = ttk.Style()
style.configure('.', font=('Candara', 14))

# Create elements

# Labels.
subtitleLabel = ttk.Label(root, text="Try to Crack a Password", font=('Candara', 16, "bold"))
pwordTextLabel = ttk.Label(root, text="Enter password below:")
hashTextLabel = ttk.Label(root, text="Select SHA Hashing Type:")
pwordFoundTextLabel = ttk.Label(root, text='')
numGuessesTextLabel = ttk.Label(root, text='')
timeLabel = ttk.Label(root, text="")
dictSizeLabel = ttk.Label(root, text="")
plotLabel = ttk.Label(root, text = "Plot The Passwords You've Cracked")
plotLabel.grid(column = 2, row = 1, padx=50)

# Password Field
passwordField = ttk.Entry(root, width=30)

# SHA type field
shaField = ttk.Entry(root, width=30)

# Crack Button
crackButton = ttk.Button(root, text='Crack', command=lambda: crackPassword(passwordField.get(), int(shaField.get())))

# Plot buttons
plot256Button = ttk.Button(root, text="Plot SHA-256 Results", command=plot256Plots)
plot512Button = ttk.Button(root, text="Plot SHA-512 Results", command=plot512Plots)

# Place elements.
subtitleLabel.grid(column=1, row = 1)
hashTextLabel.grid(column=1, row = 2)
shaField.grid(column=1, row = 3)
pwordTextLabel.grid(column=1, row=4)
passwordField.grid(column=1, row = 5)
crackButton.grid(column=1, row = 6)
timeLabel.grid(column=1, row = 7)
dictSizeLabel.grid(column=1, row = 8)
pwordFoundTextLabel.grid(column=1, row = 9)
numGuessesTextLabel.grid(column=1, row = 10)
plot256Button.grid(column=2, row = 3)
plot512Button.grid(column=2, row = 4)

root.mainloop()

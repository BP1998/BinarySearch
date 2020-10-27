#Binary search implemented in python.
#Author: Brian Peters

#I'm using tkinter for some visuals to show the search working.
#I'm not experienced in making interfaces, but I feel that this is better than command line at least

#imports

#used for GUI
import tkinter as tk
from tkinter import *

#used for math with ceil and floor
import math
from math import floor
from math import ceil

#used for random number generation for list creation
import random

#Used to prime the visuals for the search
def StartSearch(searchNum, labels, ind, widget):
    for label in labels:
        label.config(bg="white")
    BinarySearch(searchNum, labels, ind, widget)

#implimentation of binary search from memory
def BinarySearch(searchNum, labels, ind, widget):
    if(ind > len(labels)):
        ind = len(labels) - 1

    num = int(searchNum.get())

    labels[ind].config(bg="red")
    curr = int(labels[ind]["text"])

    if curr > num:
        ind = ind - ceil(ind/2)
    elif curr < num:
        ind = ind + ceil(ind/2)
    else:
        labels[ind].config(bg = "green")
        return
    widget.after(1000, lambda: BinarySearch(searchNum, labels, ind, widget))
    return

#Helper function to generate the list
def GenList(size, max, min, spinbox):
    listobj = []
    size = int(spinbox.get())
    for num in range(0, size):
        temp = random.randint(min, max)
        listobj.append(temp)
    listobj.sort()
    return listobj

#Function to spawn up the seperate widget used for the search visualization with he setting selected
def ExecuteSearch(size, max, min, spinbox):
    listobj = GenList(size, max, min, spinbox)
    widget = Tk()
    col = 0
    labels = []
    for val in listobj:
        labels.append(tk.Label(widget, text=str(val), fg='black', relief=tk.RIDGE, width=10, padx=0, pady=0))
        labels[col].grid(sticky=W, column=col, row=0)
        col += 1

    searchNum = tk.Spinbox(widget, state='readonly', values = listobj)
    searchNum.grid(row=1, column=1)

    start = int(len(labels) / 2)
    searchButton = tk.Button(widget, text = "SEARCH", command = lambda: StartSearch(searchNum, labels, start, widget))
    searchButton.grid(column = 0, row = 1)
    widget.mainloop()

#####Main######
#declare some variables
searchList = []
size = 10
max = 100
min = 0

#Set up root for tkinter
root = Tk()
root.title("Binary Search")
root.minsize(500, 500)
root.config(bg = '#c7d4d2')

button1 = tk.Button(root, text="START SEARCH", fg="blue", command= lambda: ExecuteSearch(size, max, min, spin1))
button1.config(bg = '#dbe0c3', fg = '#353940')
button1.pack()

#Build Spinbox
spinLabel = Label(text = "List size")
spinLabel.pack()

spin1 = tk.Spinbox(root, from_ = 5, to = 50, state = 'readonly', relief=tk.RIDGE)
spin1.config(bg = '#dbe0c3', buttonbackground = '#dbe0c3', fg = '#353940')
spin1.pack()

root.mainloop()

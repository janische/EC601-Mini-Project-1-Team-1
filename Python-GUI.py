from tkinter import *  #Tkinter package

import searchTwitter as ST

import sys
import os

# GUI app
window = Tk()
window.title("Analysis feedback from Tweets' contents")  
window.geometry('500x300')  #size of window

# label   
lbl = Label(window, text = "PLease type in Twitter's account name!", font = ("Arial Bold", 10))
lbl.grid(column = 0, row = 0)

# input let user type in
txt1 = Entry(window, width = 20)
txt1.grid(column = 0, row = 1)

lbl = Label(window, text = "Key1 in word", font = ("Arial Bold", 10))
lbl.grid(column = 0, row = 2)

# key 1
txt2 = Entry(window, width = 20)
txt2.grid(column = 0, row = 3)

lbl = Label(window, text = "Key2 in word", font = ("Arial Bold", 10))
lbl.grid(column = 0, row = 4)

# key2
txt3 = Entry(window, width = 20)
txt3.grid(column = 0, row = 5)

lbl = Label(window, text = "Key3 in word", font = ("Arial Bold", 10))
lbl.grid(column = 0, row = 6)

# key 3
txt4 = Entry(window, width = 20)
txt4.grid(column = 0, row = 7)

lbl = Label(window, text = "Number of tweets needed in Integer, less than 100 will be appreciated", font = ("Arial Bold", 10))
lbl.grid(column = 0, row = 8)

# numberTweets
txt5 = Entry(window, width = 20)
txt5.grid(column = 0, row = 9)

# get user account name
def getinput():
  #res = "Account name is: " + txt1.get()
  #lbl.configure(text = res)
  ST.main(txt1.get(), txt2.get(), txt3.get(), txt4.get(), txt5.get())

btn = Button(window, text="Get account name", command = getinput)
btn.grid(column=0, row = 10)



"""
# can run the python file
def clicked():
  os.system('python searchTwitter.py')

# button
btn = Button(window, command = clicked, text = "Begin search", bg = "green", fg= "white")
btn.grid(column = 0, row = 1)
"""

window.mainloop() 


"""
Program: Index window of my GUI project
Author: Carlos Lizarazu Linares
Last date modified: 
"""
#import tkinter and others
from tkinter import *
from PIL import ImageTk, Image

#create the window
indexwindow = Tk()
indexwindow.title("Index")
indexwindow.geometry("500x700")
indexwindow.config(bg='Grey')
""" This session is for the frames"""

#This frame is for the logo
logoframe = LabelFrame(indexwindow, text="Logo frame", padx=100)
logoframe.grid()
logoframe.config(bg='White')
#add the Image
img = ImageTk.PhotoImage(Image.open("logo.png"))
logo = Label(logoframe, image=img)
logo.grid(pady=20, padx=30)

#This frame is for the info
infoframe = LabelFrame(indexwindow, text='Frame info', padx=15, pady=10)
infoframe.grid()
infoframe.config(bg='blue')
#add the label name
name = Label(infoframe, text="Name", padx=15, pady=10)
name.grid(row=0, column=0)
#add the box name
entername = Entry(infoframe, width=25)
entername.grid(row=0, column=2, padx=20)
entername.config(bg='white')

#add the label age
age = Label(infoframe, text="Age", padx=20, pady=5)
age.grid(row=3, column=0)
#add the box age
enterage = Entry(infoframe, width=25)
enterage.grid(row=3, column=2, padx=20)
enterage.config(bg='white')

#This frame is for the buttons
buttonframe = LabelFrame(indexwindow, text="Button frame", padx=20, pady=5)
buttonframe.grid()
buttonframe.config(bg="green")

"""this secction will have the code of the the new windows"""

"""This is the kg/cm window"""
def kgcmwin():
  #create the window
  mainwindow = Tk()
  mainwindow.title("kg/cm")
  mainwindow.geometry("500x700")
  mainwindow.config(bg='Grey')
  """ This session is for the frames"""

  #This frame is for the buttons at the top
  topframe = LabelFrame(mainwindow, text="top frame", padx=150)
  topframe.grid()
  topframe.config(bg='red')
  #add the button for back
  backb = Button(topframe, text="BACK", bg="black", fg="yellow")
  backb.grid(row=0, column=2, padx=50)
  """
  #This frame is for the logo
  logoframe2 = LabelFrame(mainwindow, text="Logo frame", padx=100)
  logoframe2.grid()
  logoframe2.config(bg='White')
  #add the Image
  img2 = ImageTk.PhotoImage(Image.open("logo.png"))
  logo2 = Label(logoframe2, image=img2)
  logo2.grid(pady=20, padx=30)
  """
  #This frame is for the info
  infoframe = LabelFrame(mainwindow, text='Frame info', padx=15, pady=10)
  infoframe.grid()
  infoframe.config(bg='blue')
  #add the label weight
  weight = Label(infoframe, text="Weight (kg)", padx=15, pady=10)
  weight.grid(row=0, column=0)
  #add the box name
  enterweight = Entry(infoframe, width=25)
  enterweight.grid(row=0, column=2, padx=20)
  enterweight.config(bg='white')

  #add the label age
  height = Label(infoframe, text="Height (cm)", padx=20, pady=5)
  height.grid(row=3, column=0)
  #add the box age
  enterheight = Entry(infoframe, width=25)
  enterheight.grid(row=3, column=2, padx=20)
  enterheight.config(bg='white')

  """This secction is for the radiobuttons in the footer"""
  #This frame is for the buttons
  buttonframe = LabelFrame(mainwindow, text="Radiobutton frame", padx=20, pady=5)
  buttonframe.grid(rowspan=10, columnspan=10)
  buttonframe.config(bg="green")

  #add the label male
  male = Label(buttonframe, text="Male")
  male.grid(row=0, column=0)
  #add the label male
  female = Label(buttonframe, text="Female")
  female.grid(row=2, column=0)

  #add the radio button 
  maleb = Radiobutton(buttonframe, text="*", bg="black", fg="yellow")
  maleb.grid(row=0, column=2,padx=10)
  #add the radio button
  femaleb = Radiobutton(buttonframe, text="*", bg="black", fg="yellow")
  femaleb.grid(row=2, column=2, padx=10)

  """This secction is for the buttons calculate, and over/under weight and regular"""

  #This frame is fort the 3 buttons
  lastframe= LabelFrame(mainwindow, text="Calculate buttons frame")
  lastframe.grid(rowspan=40, columnspan=40)
  lastframe.config(bg="aqua")

  #Button to calculate de BMI
  calcbutton= Button(lastframe, text="Calculate your BMI")
  calcbutton.grid(row=0, column=0, pady=20)
  calcbutton.config(bg="white")

  #this Botton will tell you if you're overweight
  overbutton= Button(lastframe, text="Am I overweight?")
  overbutton.grid(row=2, column=0, pady=5)
  overbutton.config(bg="white")
  #this Botton will tell you if you're regular
  regularbutton= Button(lastframe, text="Am I regular?")
  regularbutton.grid(row=4, column=0, pady=5)
  regularbutton.config(bg="white")
  #this Botton will tell you if you're underweight
  underbutton= Button(lastframe, text="Am I underweight?")
  underbutton.grid(row=6, column=0, pady=5)
  underbutton.config(bg="white")

#add the button for kg and cm
kgcm = Button(buttonframe, text="Kg/cm", bg="black", fg="yellow", command=kgcmwin)
kgcm.grid(row=0, column=0, padx=30)

#add the button for lb  and ft
lbft = Button(buttonframe, text="lb/ft", bg="black", fg="yellow")
lbft.grid(row=0, column=2, padx=30)

indexwindow.mainloop()  #continous looping of main window

import tkinter as tk
import pyodbc
import tkinter as tk 
import subprocess
from tkinter import *
import time
from PIL import Image, ImageTk
from tkinter import ttk
import random
from random import shuffle
import pyttsx3
from tkinter import messagebox
from tkcalendar import DateEntry
import tkinter.messagebox as messagebox
import random
import pygame
import pyodbc
from connection import con_fetch
from project import username



window = tk.Tk()

# Set the background color to white
window.configure(bg="#E6E6E6") #background color
window.title("OTSIMO")         #window tittle  
window.iconbitmap("LOGO.png")  #window logo
window.geometry("800x570")     #window size
window.resizable(False, False)

progress_label = tk.Label(window, text="Progress: 0%", font=("Arial", 12))
progress_label.place(x=200,y=300)

# Create a canvas to hold the progress bar
canvas = tk.Canvas(window, width=300, height=30, bg="white", borderwidth=2, relief=tk.SUNKEN)
canvas.place(x=200,y=370)

# Create rectangles to represent the progress bar
progress_rect = canvas.create_rectangle(0, 0, 0, 30, fill="green")
def update_progress(score):
    # Calculate the progress percentage
    progress_percentage = (score / 100) * 100

    # Update the progress label
    progress_label.config(text=f"Progress: {progress_percentage:.2f}%")

    # Update the width of the progress rectangle
    canvas.coords(progress_rect, (0, 0, progress_percentage * 3, 30))
    

# Example usage: Update progress with a score of 10 out of 100


a=con_fetch(username)
update_progress(a)

image02 = tk.PhotoImage(file="LOGO.png")
label02 = tk.Label(window, image=image02 ,bg="#E6E6E6") # Create a label to display the image
label02.place(x=50,y=17) # PLACE the label into the window
mybutton10=Button(window,text='HOME',bg="#E6E6E6",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",)
mybutton10.place(x=480,y=38)
mybutton10=Button(window,text='PAINTS',bg="#E6E6E6",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",)
mybutton10.place(x=600,y=38)

frame5=Frame(window,height=60,width=800,bg="#2DF0DB",bd=1,relief=FLAT)
frame5.place(x=0,y=110)
label1_task = tk.Label(window, text="STUDENT PROGRESS",bg="#2DF0DB",font=("arial", 21,"bold" ))
label1_task.place(x=250,y=120)
def showscore():
    a=con_fetch(username)
    for row in a:

       label11_task = tk.Label(window, text=a,bg="#2DF0DB",font=("arial", 21,"bold" ))
       label11_task.place(x=250,y=120)

start_button = tk.Button(window, text="SEE PROGRESS",command=a )
start_button.place(x=120,y=180)



window.mainloop()
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
import connection
import Progress



username=' '
password=' '

vocabulary = [
    {"image": "cat.png", "options": ["DOG", "Cat", "Bird"], "answer": "Cat"},
    {"image": "apple.png", "options": ["Apple", "Banana", "Orange"], "answer": "Apple"},
    {"image": "car.png", "options": ["Car", "Bicycle", "Motorcycle"], "answer": "Car"},
    {"image": "tree.png", "options": ["Grass", "Flower", "Tree"], "answer": "Tree"},
    {"image": "book.png", "options": ["pen", "Book", "Pencil"], "answer": "Book"},
    {"image": "moon.png", "options": ["moon", "sun", "mars"], "answer": "moon"},
    {"image": "house.png", "options": ["sky", "building", "house"], "answer": "house"},
    {"image": "chair.png", "options": ["table", "chair", "cupboard"], "answer": "chair"},
    {"image": "shoes.png", "options": ["shirt", "jeans", "shoes"], "answer": "shoes"},
    {"image": "ronaldo.png", "options": ["messi", "neymar", "ronaldo"], "answer": "ronaldo"},
    {"image": "netflix.png", "options": ["neso", "netflix", "nike"], "answer": "netflix"}
    
]
vocabulary1 = {
    "EMPATHY": "The ability to understand and share the feelings of another person.",
    "ADAPTIBILITY": "The quality of being able to adjust to new conditions or changes.",
    "RESOURCEFUL": "Having the ability to find quick and clever ways to solve problems.",
    "CONFIDENCE": "A feeling or belief in one's abilities, qualities, or judgments.",
    "SUPPORTIVE": "Providing encouragement, help, or assistance to others.",
    "STRENGTH": "The quality or state of being physically or mentally strong.",
    "HOUSE": "A place to live.",
    "OVERCOME": "To successfully deal with or defeat a difficulty or challenge.",
    "INSPIRE": "To fill someone with the urge or ability to do or feel something.",
    "COURAGE": "The ability to do something that frightens or challenges you.",
    "PROGRESS": "Forward or onward movement towards a destination or goal.",
    "POTENTIAL": "Having or showing the capacity to develop or become something.",
    "INDIVIDUAL": "A single human being as opposed to a group or collective.",
    "SUCESS": "The accomplishment of an aim or purpose.",
    "ACCOMODATE": "To fit in with the needs or wishes of others.",
    "RESILIENCE": "The capacity to recover quickly from difficulties or setbacks.",
    "COLLABORATION": "The action of working with others to achieve a common goal.",
    "CONSISTENCY": "The quality of always behaving or performing in the same way.",
    "RONALDO": "The best player ever in the history of football.",
}
'''
a=check_answer(score)
'''
# Global variables
current_question = 0
score = 0 
#TAP SYMBOL GAME
current_image_index = 0
score1 = 0

images = [
    {"file": "BUS.png", "options": ["B", "A", "U", "C", "S"], "answer": "BUS"},
    {"file": "HAT.png", "options": ["Y", "H", "T", "A", "X"], "answer": "HAT"},
    {"file": "KEY.png", "options": ["Y", "H", "K", "S", "E"], "answer": "KEY"},
    {"file": "SUN.png", "options": ["T", "N", "E", "U", "S"], "answer": "SUN"},
    {"file": "CUP.png", "options": ["B", "P", "U", "C", "S"], "answer": "CUP"},
    {"file": "JAM.png", "options": ["A", "J", "A", "C", "M"], "answer": "JAM"},
    {"file": "RUG.png", "options": ["B", "U", "G", "R", "X"], "answer": "RUG"},
    {"file": "AXE.png", "options": ["A", "R", "E", "E", "X"], "answer": "AXE"},
    {"file": "TOM.png", "options": ["L", "M", "O", "Z", "T"], "answer": "TOM"},
    {"file": "PYX.png", "options": ["P", "R", "E", "X", "Y"], "answer": "PYX"},
    # Add more images with options and answers here
]
total_score = 0

current_color = "black"
brush_size = 2
drawing = False
last_x = 0
last_y = 0
stories = [
    '''Once upon a time, in a small town, there was a magical library. It was filled with books that came to life and spoke to anyone who opened them. Sarah, a dyslexic girl, loved to visit the library. Every time she opened a book, the words danced and transformed into colorful illustrations, making it easier for her to understand the stories.\n One day, Sarah discovered a special book hidden in the corner of the library. It had a golden cover and glowed with a gentle light. When she opened it, she was amazed to find that the words in this book stayed still, making it much easier for her to read. As she flipped through the pages, she learned about different magical creatures and their adventures.\n Sarah spent hours reading in the magical library, and with each visit, she grew more confident in her reading abilities. The magical books taught her that dyslexia didn't limit her imagination or her love for stories. They showed her that everyone learns in their own unique way and that her dyslexia was just a small part of who she was.''',
    '''In a bustling school, there were three friends: Alex, Maya, and Ben. Alex had dyslexia and often found it challenging to read and write. Maya was kind and patient, and she always helped Alex with his schoolwork. Ben, on the other hand, was a great storyteller and loved to read aloud. \n One day, the friends decided to participate in a school-wide puzzle contest. They knew that solving puzzles required reading instructions and working together. Alex was worried he would slow them down, but Maya assured him that they would figure it out together.\nAs they began working on the puzzle, Maya read the instructions aloud while Alex carefully listened. Ben used his storytelling skills to imagine the clues and piece them together. Alex shared his unique perspective, noticing details that others missed.'''
]
current_story_index = 0
engine = None

questions = [
    {
        "question": "Question 1: What is the capital of France?",
        "options": ["Paris", "London", "Madrid", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Question 2: How many sides does a triangle have?",
        "options": ["2", "3", "4", "5"],
        "answer": "3"
    },
    {
        "question": "Question 3: Which is the largest mountain range in the world?",
        "options": ["Himalayas", "Alps", "Andes", "Rockies"],
        "answer": "Himalayas"
    },
    {
        "question": "Question 4: How many players are there in a cricket team?",
        "options": ["10", "11", "9", "7"],
        "answer": "11"
    },{
        "question": "Question 5: What is the largest planet in our solar system?",
        "options": ["Mars", "Jupiter", "Saturn", "Neptune"],
        "answer": "Jupiter"
    },{
        "question": "Question 6: How many colors are there in a rainbow?",
        "options": ["4", "8", "6", "7"],
        "answer": "7"
    },{
        "question": "Question 7: Which is the largest land animal?",
        "options": ["Lion", "Elephant", "Rhino", "Tiger"],
        "answer": "Elephant"
    },{
        "question": "Question 8: How many days are there in a leap year?",
        "options": ["636", "365", "366", "367"],
        "answer": "366"
    },{
        "question": "Question 9: What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Pacific Ocean", "India Ocean", "None of these"],
        "answer": "Pacific Ocean"
    },{
        "question": "Question 10: Which animal is known for its black and white stripes?",
        "options": ["Tiger", "Cheetah", "lion", "Zebra"],
        "answer": "Zebra"
    }
    # Add more questions here...
]
current_question_index = 0
scores = [0] * len(questions)  # Initialize scores for all questions as 0
answer_var1 = None
answer_var2 = None
answer_buttons1 = []
answer_buttons2 = []

'''

# Establish a connection to the Access database
conn = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=PROJECT.accdb;'
)
# Create a cursor
cursor = conn.cursor()
'''










#games page
def open_test_window15():
     window.withdraw()  # Hide the main window
     window15 = tk.Toplevel(window)  # Create a new window
     window15.title("OSTISMO")  # Set the title of the new window
     window15.geometry("800x620")  # Set the size of the new window
     window15.resizable(False,False)
     window15.configure(bg="#BFCCB5")

     def close_test_window15():
        window15.destroy()  # Destroy the new window
       
     
     image02 = tk.PhotoImage(file="LOGO.png")
     label02 = tk.Label(window15, image=image ,bg="#BFCCB5") # Create a label to display the image
     label02.place(x=50,y=17) # PLACE the label into the window

     mybutton10=Button(window15,text='HOME',bg="#BFCCB5",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window2)
     mybutton10.place(x=400,y=38)
     mybutton9=Button(window15,text='PAINTS',bg="#BFCCB5",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2")
     mybutton9.place(x=520,y=38)
    

     frame5=Frame(window15,height=50,width=800,bg="#808080",bd=1,relief=FLAT)
     frame5.place(x=0,y=125)
     heading_label =Label(window15, text="CHOSE ANY ONE OF GAME",bg="#808080",fg="black" , font=("Helvetica", 23, "bold"),)
     heading_label.place(x=160,y=130)
     frame33 = ttk.Frame(window, padding=10)
     frame33.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
     # Create the first button
     style1 = ttk.Style()
     style1.configure("Custom.TButton", relief="flat", background="#9376E0", foreground="black", font=("Arial", 12,"bold"), borderwidth=0, focuscolor="none")
     style1.map("Custom.TButton", background=[("active", "#3c8af5")])
     style1.configure("Custom.TButton", padding=10)

     button1 = ttk.Button(window15, text="Bricks 'n' Busters", style="Custom.TButton", command=open_page_match51,width=15)
     button1.place(x=300,y=240)
     
     style2 = ttk.Style()
     style2.configure("Custom.TButton", relief="flat", background="#e74c3c", foreground="black", font=("Arial", 12,"bold"), borderwidth=0, focuscolor="none",)
     style2.map("Custom.TButton", background=[("active", "#c0392b")])
     style2.configure("Custom.TButton", padding=10)

     button2 = ttk.Button(window15, text="Match Masters", style="Custom.TButton", command=open_page_match50,width=15)
     button2.place(x=300,y=320)

     style3 = ttk.Style()
     style3.configure("Custom.TButton", relief="flat", background="#e74c3c", foreground="black", font=("Arial", 12,"bold"), borderwidth=0, focuscolor="none",)
     style3.map("Custom.TButton", background=[("active", "#c0392b")])
     style3.configure("Custom.TButton", padding=10)

     button3 = ttk.Button(window15, text="Word Search", style="Custom.TButton", command=open_page_match52,width=15)
     button3.place(x=300,y=400)

     button4 = ttk.Button(window15, text="HANG-MAN", style="Custom.TButton", command=open_page_match53,width=15)
     button4.place(x=300,y=480)



     window15.protocol("WM_DELETE_WINDOW", close_test_window15)
def open_page_match50():
     subprocess.Popen(["python","match.py"])

def open_page_match51():
     subprocess.Popen(["python","bricks.py"])  

def open_page_match52():
     subprocess.Popen(["python","main.py"])   

def open_page_match53():
     subprocess.Popen(["python","hangman.py"])    
     
   
def reminder():
     window.withdraw()  # Hide the main window
     window14 = tk.Toplevel(window)  # Create a new window
     window14.title("OSTISMO")  # Set the title of the new window
     window14.geometry("800x620")  # Set the size of the new window
     window14.resizable(False,False)
     window14.configure(bg="#BFCCB5")

     def close_test_window11():
        window14.destroy()  # Destroy the new window
       
     image02 = tk.PhotoImage(file="LOGO.png")
     label02 = tk.Label(window14, image=image ,bg="#BFCCB5") # Create a label to display the image
     label02.place(x=50,y=17) # PLACE the label into the window

     mybutton10=Button(window14,text='HOME',bg="#BFCCB5",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window2)
     mybutton10.place(x=480,y=38)
     mybutton10=Button(window14,text='PAINTS',bg="#BFCCB5",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window2)
     mybutton10.place(x=600,y=38)

     def add_task():
       task = entry_task.get()
       date = entry_date.get_date()
       if task and date:
         task_with_date = f"{task} - {date.strftime('%Y-%m-%d')}"
         listbox_tasks.insert(tk.END, task_with_date)
         entry_task.delete(0, tk.END)
         entry_date.delete(0, tk.END)
       else:
         messagebox.showwarning("Warning", "Please enter a task and select a date.")

     def delete_task():
         try:
            index = listbox_tasks.curselection()
            listbox_tasks.delete(index)
         except:
            messagebox.showwarning("Warning", "Please select a task.")


     frame5=Frame(window14,height=60,width=800,bg="#2DF0DB",bd=1,relief=FLAT)
     frame5.place(x=0,y=110)
     label1_task = tk.Label(window14, text="YOUR PERSONAL REMINDER HUB",bg="#2DF0DB",font=("arial", 21,"bold" ))
     label1_task.place(x=115,y=120)

          # Create a label and entry widget for task input
     label_task = tk.Label(window14, text="ENTER A TASK:",bg="#BFCCB5",font=("arial", 18,"bold" ))
     label_task.place(x=100,y=185)
     entry_task = tk.Entry(window14,width=50)
     entry_task.place(x=88,y=230)

# Create a calendar widget for selecting a date
     label_date = tk.Label(window14, text="Select a date:",bg="#BFCCB5",font=("arial", 15 ))
     label_date.place(x=420,y=192)
     entry_date = DateEntry(window14, date_pattern='yyyy-mm-dd')
     entry_date.place(x=435,y=225)


# Create a button to add a task
     button_add = tk.Button(window14, text="Add Task", command=add_task,width=14)
     button_add.place(x=140,y=262)

# Create a listbox to display tasks
     listbox_tasks = tk.Listbox(window14,width=110,height=13)
     listbox_tasks.place(x=72,y=300)

# Create a button to delete a task
     button_delete = tk.Button(window14, text="Delete Task", command=delete_task,width=14,height=2)
     button_delete.place(x=320,y=540)

     window14.protocol("WM_DELETE_WINDOW", close_test_window11)

#about dyslexia
def open_test_window11():
     window.withdraw()  # Hide the main window
     window13 = tk.Toplevel(window)  # Create a new window
     window13.title("OSTISMO")  # Set the title of the new window
     window13.geometry("800x620")  # Set the size of the new window
     window13.resizable(False,False)
     window13.configure(bg="white")

     def close_test_window10():
        window13.destroy() 
        window.deiconify() # Destroy the new window
       
     
     image02 = tk.PhotoImage(file="LOGO.png")
     label02 = tk.Label(window13, image=image ,bg="white") # Create a label to display the image
     label02.place(x=50,y=17) # PLACE the label into the window

     mybutton10=Button(window13,text='HOME',bg="white",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=window)
     mybutton10.place(x=500,y=38)
     frame5=Frame(window13,height=800,width=800,bg="#E6E6E6",bd=1,relief=FLAT)
     frame5.place(x=0,y=110)

     frame6=Frame(window13,height=400,width=450,bg="#C1D0B5",bd=1,relief=FLAT)
     frame6.place(x=50,y=150)
     text = "Having dyslexia does not mean one is stupid! In fact, dyslexics often have average to above-average intelligence with high verbal language skills. Individuals may show special talents in areas that involve visual and spatial tasks. Many successful and well-known people have dyslexia including inventor Thomas Edison, actress Whoopi Goldberg, film producer and entrepreneur Walt Disney, baseball pitcher Nolan Ryan, and businessman Charles Schwab."

     label = tk.Label(window13, text=text, wraplength=400,bg="#C1D0B5",font=("arial", 15, ))
     label.place(x=70,y=185)

     image99 = tk.PhotoImage(file="pic2.png")
     label99 = tk.Label(window13, image=image99,bg="#E6E6E6")
     label99.image = image99
     label99.place(x=500, y=180) 

    

     window13.protocol("WM_DELETE_WINDOW", close_test_window10)





#contact page
def open_test_window10():
     window.withdraw()  # Hide the main window
     window12 = tk.Toplevel(window)  # Create a new window
     window12.title("OSTISMO")  # Set the title of the new window
     window12.geometry("800x620")  # Set the size of the new window
     window12.resizable(False,False)
     window12.configure(bg="white")

     def close_test_window9():
        window12.destroy()
        window.deiconify()  # Destroy the new window
       
     
     image02 = tk.PhotoImage(file="LOGO.png")
     label02 = tk.Label(window12, image=image ,bg="white") # Create a label to display the image
     label02.place(x=50,y=17) # PLACE the label into the window

     mybutton10=Button(window12,text='HOME',bg="white",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=window)
     mybutton10.place(x=430,y=38)
     mybutton9=Button(window12,text='LOGIN',bg="white",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=login)
     mybutton9.place(x=550,y=38)
     frame5=Frame(window12,height=800,width=800,bg="#E6E6E6",bd=1,relief=FLAT)
     frame5.place(x=0,y=110)
     heading_label =Label(window12, text="CONTACT US",bg="#E6E6E6",fg="black" , font=("Helvetica", 22, "bold"),)
     heading_label.place(x=280,y=150)

     frame6=Frame(window12,height=300,width=260,bg="#99A799",bd=1,relief=FLAT)
     frame6.place(x=434,y=225)

     image99 = tk.PhotoImage(file="mail.png")
     label99 = tk.Label(window12, image=image99,bg="#99A799")
     label99.image = image99
     label99.place(x=520, y=250) 

     heading_label1=Label(window12, text="BY MAIL",bg="#99A799",fg="black" , font=("arial", 16,"bold"),)
     heading_label1.place(x=505,y=310)

     heading_label2=Label(window12, text="Just send your question on",bg="#99A799",fg="black" , font=("arial", 13, ))
     heading_label2.place(x=458,y=345)
     heading_label3=Label(window12, text="otismo123@gmail.com",bg="#99A799",fg="black" , font=("arial", 13, ))
     heading_label3.place(x=467,y=378)

     frame6=Frame(window12,height=300,width=260,bg="#99A799",bd=1,relief=FLAT)
     frame6.place(x=104,y=225)

     image99 = tk.PhotoImage(file="phone.png")
     label99 = tk.Label(window12, image=image99,bg="#99A799")
     label99.image = image99
     label99.place(x=190, y=250) 

     heading_label4=Label(window12, text="BY PHONE",bg="#99A799",fg="black" , font=("arial", 16,"bold"),)
     heading_label4.place(x=175,y=310)

     heading_label5=Label(window12, text="Monday to Friday ",bg="#99A799",fg="black" , font=("arial", 13, ))
     heading_label5.place(x=166,y=345)
     heading_label6=Label(window12, text="+92-3xz-yyyyyy",bg="#99A799",fg="black" , font=("arial", 13, ))
     heading_label6.place(x=170,y=377)

    



     window12.protocol("WM_DELETE_WINDOW", close_test_window9)

#our mission
def open_test_window9():
     window.withdraw()  # Hide the main window
     window11 = tk.Toplevel(window)  # Create a new window
     window11.title("OSTISMO")  # Set the title of the new window
     window11.geometry("800x620")  # Set the size of the new window
     window11.resizable(False,False)
     window11.configure(bg="white")

     def close_test_window8():
        window11.destroy()
        window.deiconify  # Destroy the new window
               
     
     image02 = tk.PhotoImage(file="LOGO.png")
     label02 = tk.Label(window11, image=image ,bg="white") # Create a label to display the image
     label02.place(x=50,y=17) # PLACE the label into the window

     mybutton10=Button(window11,text='HOME',bg="white",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=window)
     mybutton10.place(x=430,y=38)
     mybutton9=Button(window11,text='LOGIN',bg="white",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=login)
     mybutton9.place(x=550,y=38)
     frame5=Frame(window11,height=800,width=800,bg="#E6E6E6",bd=1,relief=FLAT)
     frame5.place(x=0,y=110)
     heading_label =Label(window11, text="OUR MISSION",bg="#E6E6E6",fg="black" , font=("Helvetica", 22, "bold"),)
     heading_label.place(x=125,y=150)
     text="At OTSIMO our mission is to empower dyslexic student \n and support their educational journey through innovative \n software solutions. we are commited to creating a \n positive and inclusive learning enviroment where students \n with dyslexia can thrive,overcome challenges and \n reach their full potential"
     text2="Through our software , we strive to foster independence , boost confidence and instill a love for learning among"
     text3= "dyslexic students. by tailoring our features to meet their unique needs, we seek to remove barriers to education"
     text4="and unlock their inherent talents"
     heading_label1 =Label(window11, text=text,bg="#E6E6E6",fg="black" , font=("arial", 12),)
     heading_label1.place(x=40,y=240)
     image99 = tk.PhotoImage(file="dyslexia.png")
     label99 = tk.Label(window11, image=image99,bg="#E6E6E6")
     label99.image = image99
     label99.place(x=470, y=180) 
     heading_label2 =Label(window11, text=text2,bg="#E6E6E6",fg="black" , font=("arial", 12),)
     heading_label2.place(x=30,y=390)
     heading_label3 =Label(window11, text=text3,bg="#E6E6E6",fg="black" , font=("arial", 12),)
     heading_label3.place(x=30,y=413)
     heading_label4 =Label(window11, text=text4,bg="#E6E6E6",fg="black" , font=("arial", 12),)
     heading_label4.place(x=30,y=436)

     window11.protocol("WM_DELETE_WINDOW", close_test_window8)
     



#sentence activity
def open_test_window8():
     window.withdraw()  # Hide the main window
     window10 = tk.Toplevel(window)  # Create a new window
     window10.title("OSTISMO")  # Set the title of the new window
     window10.geometry("800x620")  # Set the size of the new window
     window10.resizable(False,False)
     window10.configure(bg="#BFCCB5")

     def close_test_window7():
        window10.destroy()  # Destroy the new window
      
     
     image02 = tk.PhotoImage(file="LOGO.png")
     label02 = tk.Label(window10, image=image ,bg="#BFCCB5") # Create a label to display the image
     label02.place(x=50,y=17) # PLACE the label into the window

     mybutton10=Button(window10,text='HOME',bg="#BFCCB5",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window2)
     mybutton10.place(x=400,y=38)
     mybutton9=Button(window10,text='PAINTS',bg="#BFCCB5",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=paint)
     mybutton9.place(x=520,y=38)
    

     frame5=Frame(window10,height=50,width=800,bg="#808080",bd=1,relief=FLAT)
     frame5.place(x=0,y=95)
     heading_label =Label(window10, text="PREFECT YOUR SENTENCE",bg="#808080",fg="black" , font=("Helvetica", 23, "bold"),)
     heading_label.place(x=105,y=100)


     def evaluate_answers():
      answers = ['Appreciate', 'Seventeen', 'Make', '?', 'Backpack']
      user_answers = [entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get()]
    
      score = 0
      for i in range(5):
        if user_answers[i].strip().lower() == answers[i].lower():
            score += 1
    
      messagebox.showinfo("Result", f"Your score: {score}/5")
      connection.con_insert(username,"Perfect Your Sentence",score)
    
     question1 = tk.Label(window10, text="1: Which of the following words is spelled correctly?",font=("arial", 12),bg="#BFCCB5")
     question1.place(x=30,y=155)
     entry1 = tk.Entry(window10)
     entry1.place(x=60,y=185)

     options1 = tk.Label(window10, text="a) Aprecciate b) Appriciate c) Appreciate",font=("arial", 12),bg="#BFCCB5")
     options1.place(x=50,y=208)

     question2 = tk.Label(window10, text="2: Which of the following numbers is written correctly in words?",font=("arial", 12),bg="#BFCCB5")
     question2.place(x=30,y=240)
     entry2 = tk.Entry(window10)
     entry2.place(x=60,y=270)

     options2 = tk.Label(window10, text="a) Seventeeen b) Seventeen c) Seventen ",font=("arial", 12),bg="#BFCCB5")
     options2.place(x=50,y=293)

     question3 = tk.Label(window10, text='''3:  Which of the following words rhymes with "cake"?''',font=("arial", 12),bg="#BFCCB5")
     question3.place(x=30,y=325)
     entry3 = tk.Entry(window10)
     entry3.place(x=60,y=355)

     options3 = tk.Label(window10, text="a) Make b) late c) sad ",font=("arial", 12),bg="#BFCCB5")
     options3.place(x=50,y=378)

     question4 = tk.Label(window10,font=("arial", 12),bg="#BFCCB5", text="4: Which punctuation mark is used at the end of a question?")
     question4.place(x=30,y=410)
     entry4 = tk.Entry(window10)
     entry4.place(x=60,y=440)

     options4 = tk.Label(window10, text="a) ! b) ? c) / ",font=("arial", 12),bg="#BFCCB5")
     options4.place(x=50,y=463)

     question5 = tk.Label(window10, text="5: Which of the following is a compound word?",font=("arial", 12),bg="#BFCCB5")
     question5.place(x=30,y=500)
     entry5 = tk.Entry(window10)
     entry5.place(x=60,y=530)

     options5 = tk.Label(window10, text="a) Apple b) Tree c) Back-pack",font=("arial", 12),bg="#BFCCB5")
     options5.place(x=50,y=555)

# Create the submit button
     submit_button = tk.Button(window10, text="SUBMIT", command=evaluate_answers,width=13)
     submit_button.place(x=130,y=585)


     window10.protocol("WM_DELETE_WINDOW", close_test_window7) 

#stroy narration
def open_test_window7():
     window.withdraw()  # Hide the main window
     window9 = tk.Toplevel(window)  # Create a new window
     window9.title("OSTISMO")  # Set the title of the new window
     window9.geometry("800x570")  # Set the size of the new window
     window9.resizable(False,False)
     window9.configure(bg="#BFCCB5")

     def close_test_window6():
        window9.destroy()  # Destroy the new window
       
 
     def speak_text():
       global engine
       text = story_label.cget("text")
       engine = pyttsx3.init()
       engine.setProperty("rate", 150)  # Adjust the speaking rate (words per minute)
       engine.say(text)
       engine.runAndWait()

     def stop_speaking():
       global engine
       if engine:
         engine.stop()


     def next_story():
      global current_story_index
      current_story_index = (current_story_index + 1) % len(stories)
      story_label.config(text=stories[current_story_index])

     story_label = tk.Label(window9, text=stories[current_story_index], wraplength=780, justify="center", font=("Arial", 12),bg="#BFCCB5")
     story_label.place(x=20,y=170)

       # Create speak button
     speak_button = tk.Button(window9, text="SPEAK", command=speak_text,width=12)
     speak_button.place(x=230,y=415)

       # Create stop button
     stop_button = tk.Button(window9, text="STOP", command=stop_speaking,width=12)
     stop_button.place(x=370,y=415)


       # Create next button
     next_button = tk.Button(window9, text="NEXT", command=next_story,width=12)
     next_button.place(x=500,y=415)


     image02 = tk.PhotoImage(file="LOGO.png")
     label02 = tk.Label(window9, image=image ,bg="#BFCCB5") # Create a label to display the image
     label02.place(x=50,y=17) # PLACE the label into the window

     mybutton10=Button(window9,text='HOME',bg="#BFCCB5",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window2)
     mybutton10.place(x=370,y=38)
     mybutton9=Button(window9,text='NEXT',bg="#BFCCB5",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window8)
     mybutton9.place(x=490,y=38)
     mybutton10=Button(window9,text='PAINTS',bg="#BFCCB5",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=paint)
     mybutton10.place(x=590,y=38)

     frame5=Frame(window9,height=50,width=800,bg="#808080",bd=1,relief=FLAT)
     frame5.place(x=0,y=95)
     heading_label =Label(window9, text="Explore through Engaging Audio Narratives",bg="#808080",fg="black" , font=("Helvetica", 23, "bold"),)
     heading_label.place(x=105,y=100)

     image99 = tk.PhotoImage(file="listen.png")
     label99 = tk.Label(window9, image=image99,bg="#BFCCB5")
     label99.image = image99
     label99.place(x=310, y=460) 

     


     window9.protocol("WM_DELETE_WINDOW", close_test_window6) 



#paint
def paint():
     window.withdraw()  # Hide the main window
     window8 = tk.Toplevel(window)  # Create a new window
     window8.title("OSTISMO")  # Set the title of the new window
     window8.geometry("800x570")  # Set the size of the new window
     window8.resizable(False,False)
     window8.configure(bg="white")

     def close_paint():
        window8.destroy()  # Destroy the new window
       

     # Function to handle mouse click
     def start_drawing(event):
       global drawing, last_x, last_y
       drawing = True
       last_x = event.x
       last_y = event.y
     
     # Function to handle mouse movement
     def draw(event):
       global drawing, last_x, last_y
       if drawing:
         canvas.create_line(last_x, last_y, event.x, event.y, fill=current_color, width=brush_size)
         last_x = event.x
         last_y = event.y
    
     # Function to change the color to the eraser
     def use_eraser():
      global current_color
      current_color = "white"

     # Function to change the color
     def change_color(new_color):
      global current_color
      current_color = new_color

      # Function to change the brush size
     def change_brush_size(new_size):
      global brush_size
      brush_size = new_size

# Function to clear the canvas
     def clear_canvas():
      canvas.delete("all")
     

     canvas = tk.Canvas(window8, width=800, height=550, bg="white")
     canvas.place(x=0,y=0)

# Bind mouse events
     canvas.bind("<Button-1>", start_drawing)
     canvas.bind("<B1-Motion>", draw)

# Create color palette buttons
     colors = ["black", "red", "blue", "green", "yellow"]
     color_btn_x = 10  # Initial x-coordinate for the color buttons
     color_btn_y = 510
     for i, color in enumerate(colors):
        button = tk.Button(window8, bg=color, width=3, command=lambda c=color: change_color(c))
        button.place(x=color_btn_x, y=color_btn_y)
        color_btn_x += 40  # Increment x-coordinate for the next color button


     frame5=Frame(window8,height=50,width=800,bg="#808080",bd=1,relief=FLAT)
     frame5.place(x=0,y=0)
     heading_label =Label(window8, text="UNLEASH YOUR CREATIVITY BY DARWING",bg="#808080",fg="black" , font=("Helvetica", 20, "bold"),)
     heading_label.place(x=80,y=10)
     button1 = tk.Button(window8, text="HOME", command=open_test_window2,width=12)
     button1.place(x=690,y=12)
# Create eraser button
     eraser_button = tk.Button(window8, text="Eraser", command=use_eraser,width=12)
     eraser_button.place(x=20,y=400)

# Create brush size buttons
     brush_sizes = [2, 4, 6, 8, 10]
     brush_btn_x = 250  # Initial x-coordinate for the brush size buttons
     brush_btn_y = 510
     for size in brush_sizes:
      button = tk.Button(window8, text=str(size), width=2, command=lambda s=size: change_brush_size(s))
      button.place(x=brush_btn_x, y=brush_btn_y)
      brush_btn_x += 40

# Create clear button
     clear_button = tk.Button(window8, text="Clear", command=clear_canvas,width=12)
     clear_button.place(x=20,y=450)







     window8.protocol("WM_DELETE_WINDOW", close_paint)




#text to speech
def open_test_window6():
     global current_index
     window.withdraw()  # Hide the main window
     window7 = tk.Toplevel(window)  # Create a new window
     window7.title("OSTISMO")  # Set the title of the new window
     window7.geometry("800x570")  # Set the size of the new window
     window7.resizable(False,False)
     window7.configure(bg="#BFCCB5")

     def close_test_window5():
        window7.destroy()  # Destroy the new window


     image02 = tk.PhotoImage(file="LOGO.png")
     label02 = tk.Label(window7, image=image ,bg="#BFCCB5") # Create a label to display the image
     label02.place(x=50,y=17) # PLACE the label into the window

     mybutton10=Button(window7,text='HOME',bg="#BFCCB5",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window2)
     mybutton10.place(x=370,y=38)
     mybutton9=Button(window7,text='NEXT',bg="#BFCCB5",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window7)
     mybutton9.place(x=490,y=38)
     mybutton10=Button(window7,text='PAINTS',bg="#BFCCB5",fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=paint)
     mybutton10.place(x=590,y=38)

     frame5=Frame(window7,height=50,width=800,bg="#808080",bd=1,relief=FLAT)
     frame5.place(x=0,y=95)
     heading_label =Label(window7, text="ENHANCE YOUR VOCABS!",bg="#808080",fg="black" , font=("Helvetica", 23, "bold"),)
     heading_label.place(x=210,y=100)

     # Check if the number of words to sample is greater than the vocabulary size
     num_words_to_sample = min(20, len(vocabulary1))

      # Randomly select words from the vocabulary
     words = random.sample(list(vocabulary1.items()), k=num_words_to_sample)

     engine = pyttsx3.init()

     def speak(text):
        engine.setProperty("rate", 150)  # Adjust the speech rate as needed
        engine.say(text)
        engine.runAndWait()

     def speak_word(word):
        speak(word)

     def display_words(index):
    # Clear previous buttons
       for widget in word_frame.winfo_children():
         widget.destroy()

    # Display 5 words on the page
       for i in range(index, min(index + 5, len(words))):
         word, definition = words[i]
         button = tk.Button(word_frame, text=word, font=("Arial", 14), width=15, height=2,
                           command=lambda word=word: speak_word(word))
         button.pack(pady=5)

     def next_page():
        global current_index
        current_index += 5

        if current_index >= len(words):
           current_index = 0

        display_words(current_index)
      
     current_index = 0

     # Create word frame
     word_frame = tk.Frame(window7,bg="#BFCCB5")
     word_frame.place(x=180,y=185)

# Display the initial words

     display_words(current_index)

# Create next button
     next_button = tk.Button(window7, text="Next", font=("Arial", 14), command=next_page,width=16) 
     next_button.place(x=400,y=310)

     image99 = tk.PhotoImage(file="vocab.png")
     label99 = tk.Label(window7, image=image99,bg="#BFCCB5")
     label99.image = image99
     label99.place(x=425, y=390) 

 
     window7.protocol("WM_DELETE_WINDOW", close_test_window5)   






stored_colors = []

#color shuffle 
def open_test_window5():
     window.withdraw()  # Hide the main window
     window6 = tk.Toplevel(window)  # Create a new window
     window6.title("OSTISMO")  # Set the title of the new window
     window6.geometry("800x570")  # Set the size of the new window
     window6.resizable(False,False)
     window6.configure(bg="#3F4E4F")

     def close_test_window5():
        window6.destroy()  # Destroy the new window
       
     image02 = tk.PhotoImage(file="LOGO.png")
     label02 = tk.Label(window6, image=image ,bg="#3F4E4F") # Create a label to display the image
     label02.place(x=50,y=20) # PLACE the label into the window

     mybutton10=Button(window6,text='HOME',bg="#3F4E4F",fg="white",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window2)
     mybutton10.place(x=370,y=38)
     mybutton9=Button(window6,text='BLOG',bg="#3F4E4F",fg="white",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window11)
     mybutton9.place(x=490,y=38)
     heading_label =Label(window6, text="REMEBER AND RECALL",bg="#3F4E4F",fg="black" , font=("Helvetica", 23, "bold"),)
     heading_label.place(x=260,y=95)

     # Function to shuffle the colors
     def shuffle_colors():
       colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
       shuffle(colors)
       for i in range(6):
        color_buttons[i].config(bg=colors[i])
       global stored_colors
       stored_colors = colors

# Function to check the positions of colors
     def check_positions():
      user_positions = [entry.get() for entry in entry_fields]
      colors = [color_buttons[i].cget('bg') for i in range(6)]
      correct_count = sum([1 for user_color, actual_color in zip(user_positions, stored_colors) if user_color == actual_color])
      global total_score
      total_score += correct_count
      result_label.config(text=str(correct_count) + " correct!")
      score_label.config(text='Total Score: ' + str(total_score))
      connection.con_insert(username,"Remember and Recall",total_score)

# Function to hide the colors
     def hide_colors():
       global stored_colors
       stored_colors = [color_buttons[i].cget('bg') for i in range(6)]
       for i in range(6):
         color_buttons[i].config(bg='white')
      


     color_buttons = []
     for i in range(6):
       button = tk.Button(window6, width=10, height=5)
       button.pack(side=tk.LEFT, padx=10, pady=10)
       color_buttons.append(button)

# Entry fields for user input
     entry_fields = []
     for i in range(6):
      entry = tk.Entry(window6, width=10,bg="#9BABB8")
      entry.place(x=650, y=160 + i * 40)
      entry_fields.append(entry) 
    
     check_button = tk.Button(window6,padx=25,pady=5, text='Check', command=check_positions,font=("Arial", 14, "bold"),bg="#7e57c2")
     check_button.place(x=640,y=410)

# Result label
     result_label = tk.Label(window6, text='', font=('Arial', 14))
     result_label.place(x=640,y=470)

# Shuffle button
     shuffle_button = tk.Button(window6,padx=25,pady=5, text='SHUFFLE',bg="#7e57c2", command=shuffle_colors,font=("Arial", 14, "bold"))
     shuffle_button.place(x=310,y=360)

# Hide button
     hide_button = tk.Button(window6,padx=25,pady=5 ,text='HIDE',bg="#7e57c2", command=hide_colors,font=("Arial", 14, "bold"))
     hide_button.place(x=180,y=360)

# Score label
     score_label = tk.Label(window6, text='Total Score: 0', font=('Arial', 14))
     score_label.place(x=150,y=500)

     image99 = tk.PhotoImage(file="memory1.png")

# Create a Label widget and set the image as its content
     label99 = tk.Label(window6, image=image99,bg="#3F4E4F")
     label99.image = image99


     label99.place(x=300, y=415) 


     window6.protocol("WM_DELETE_WINDOW", close_test_window5)




#Vocabulary
def open_test_window4():
     window.withdraw()  # Hide the main window
     window5 = tk.Toplevel(window)  # Create a new window
     window5.title("OSTISMO")  # Set the title of the new window
     window5.geometry("800x570")  # Set the size of the new window
     window5.resizable(False,False)
     window5.configure(bg="#3F4E4F")

     def close_test_window4():
        window5.destroy()  # Destroy the new window
        
     image02 = tk.PhotoImage(file="LOGO.png")
     label02 = tk.Label(window5, image=image ,bg="#3F4E4F") # Create a label to display the image
     label02.place(x=50,y=20) # PLACE the label into the window

     mybutton9=Button(window5,text='BLOG',bg="#3F4E4F",fg="white",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window11)
     mybutton9.place(x=380,y=38)
     mybutton10=Button(window5,text='NEXT',bg="#3F4E4F",fg="white",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window5)
     mybutton10.place(x=480,y=38)
     mybutton11=Button(window5,text='HOME',bg="#3F4E4F",fg="white",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window2)
     mybutton11.place(x=575,y=38)

     heading_label =Label(window5, text="WORD SCRIBE",bg="#3F4E4F",fg="black" , font=("Helvetica", 23, "bold"),)
     heading_label.place(x=275,y=82)

     def check_answer():
      answer = answer_entry.get().upper()
      correct_answer = images[current_image_index]["answer"]
      if answer == correct_answer:
        result_label.config(text="Correct!", fg="green")
        increase_score()
      else:
        result_label.config(text="Wrong!", fg="red")
        submit_button.config(state="disabled")
        next_button.config(state="normal")

     def increase_score():
      global score1
      score1 += 1
      score_label.config(text="Score: {}".format(score1))

     def next_image():
      global current_image_index
      current_image_index += 1
      if current_image_index < len(images):
        show_image()
        submit_button.config(state="normal")
       # next_button.config(state="disabled")
        result_label.config(text="")
        answer_entry.delete(0, tk.END)
      else:
        display_total_score()

     def show_image():
      image_info = images[current_image_index]
      file_name = image_info["file"]
      options = image_info["options"]

      image = tk.PhotoImage(file=file_name)
      image_label.config(image=image)
      image_label.image = image

      for frame in option_frames:
        frame.destroy()

      option_frames.clear()

      for option in options:
        frame = tk.Frame(options_container, width=60, height=60, bd=2, relief="solid", bg="#C1D0B5")
        frame.pack(side=tk.LEFT, padx=10)
        label = tk.Label(frame, text=option, font=("Arial", 24), bg="#C1D0B5", fg="red")
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        option_frames.append(frame)

     def display_total_score():
        total_score_label.config(text="Total Score: {}".format(score1), font=("Arial", 16, "bold"), fg="black",bg="#3F4E4F")
        total_score_label.place(x=300,y=530)
        connection.con_insert(username,"Vocabulary",score1)
     

     
     image_label = tk.Label(window5,bg="#3F4E4F")
     image_label.place(x=320,y=125)

     options_container = tk.Frame(window5, bg="#3F4E4F")
     options_container.place(x=200,y=265)

     option_frames = []

     answer_entry = tk.Entry(window5, font=("Arial", 16))
     answer_entry.place(x=280,y=337)

     submit_button = tk.Button(window5,padx=20, text="Submit", font=("Arial", 14, "bold"), bg="#7e57c2", fg="white", command=check_answer)
     submit_button.place(x=265,y=379)

     next_button = tk.Button(window5,padx=23, text="Next", font=("Arial", 14, "bold"), bg="#7e57c2", fg="black", command=next_image, )
     next_button.place(x=415,y=379)

     result_label = tk.Label(window5, font=("Arial", 20))
     result_label.place(x=328,y=432)

     score_label = tk.Label(window5, text="Score: 0", font=("Arial", 18))
     score_label.place(x=326,y=480)

     total_score_label = tk.Label(window5, font=("Arial", 16, "bold"))

# Start the game
     show_image()


     window5.protocol("WM_DELETE_WINDOW", close_test_window4)





#word scribe
def open_test_window3():
    window.withdraw()  # Hide the main window
    window4 = tk.Toplevel(window)  # Create a new window
    window4.title("OSTISMO")  # Set the title of the new window
    window4.geometry("800x570")  # Set the size of the new window
    window4.resizable(False,False)
    window4.configure(bg="#3F4E4F")

    def close_test_window3():
          window4.destroy()  # Destroy the new window
          
          
                 
    image02 = tk.PhotoImage(file="LOGO.png")
    label02 = tk.Label(window4, image=image ,bg="#3F4E4F") # Create a label to display the image
    label02.place(x=50,y=20) # PLACE the label into the window
     
    canvas12 = tk.Canvas(window4, width=400, height=400, bg="#3F4E4F",highlightthickness=2, highlightbackground="red")
    canvas12.place(x=430,y=120)
    canvas12.config(highlightthickness=0)

   

    
     # Create a list of alphabets
    alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# Create a list to store the alphabet objects
    alphabet_objects = []


    for i in range(len(alphabets)):
         x = random.randint(50, 350)
         y = random.randint(-200, -50)
         alphabet = canvas12.create_text(x, y, text=alphabets[i], font=("Helvetica", 22))
         alphabet_objects.append(alphabet)
    


   

    def animate():
         for alphabet in alphabet_objects:
        # Move the alphabet downwards or upwards based on its current direction
             x, y = canvas12.coords(alphabet)
        
             if y >= 400:
            # Reached the bottom, change direction to move upwards
               canvas12.directions[alphabet] = -2
             elif y <= 0:
            # Reached the top, change direction to move downwards
               canvas12.directions[alphabet] = 2
        
             canvas12.move(alphabet, 0, canvas12.directions[alphabet])
         window.after(10, animate)
    
    canvas12.directions = {}
    for alphabet in alphabet_objects:
       canvas12.directions[alphabet] = random.choice([-2, 2])

        
    def check_answer(answer):
        global current_question, score

        if answer == vocabulary[current_question]["answer"]:
           score += 1

        current_question += 1

        if current_question >= len(vocabulary):
              show_result()
        else:
             show_next_question()
        return score
# Function to show the next question
    def show_next_question():
           canvas.delete("all")
           question_label.config(text="Question {}: CLICK ON RIGHT OPTION".format(current_question + 1))

           image = tk.PhotoImage(file=vocabulary[current_question]["image"])
           canvas.create_image(150, 150, image=image)
           canvas.image = image

           options = vocabulary[current_question]["options"]
           for i, option in enumerate(options):
               button = Button(frame, text=option, width=20, command=lambda ans=option: check_answer(ans))
               button.grid(row=i, column=0, padx=10, pady=5)

             # Function to show the result
    def show_result():
            result_label.config(text="Your Vocabulary Total Score: {}".format(score))
            result_label.place(x=270,y=520)
            submit_button.config(state="disabled")
            connection.con_insert(username,"Word Scribe",score)


    animate()
    
    heading_label =Label(window4, text="TAP VOCABULARY",bg="#3F4E4F",fg="black" , font=("Helvetica", 23, "bold"),)
    heading_label.place(x=260,y=90)

    question_label =Label(window4, text="CLICK ON RIGHT OPTION?",bg="#3F4E4F")
    question_label.place(x=300,y=135)

    canvas =Canvas(window4, width=250, height=300,bg="#3F4E4F",highlightthickness=2, highlightbackground="red")
    canvas.place(x=220,y=150)
    canvas.config(highlightthickness=0)

    frame =Frame(window4,bg="#3F4E4F")
    frame.place(x=270,y=400)

    show_next_question()

    submit_button =Button(window4, text="Submit", width=10, command=show_result)
    submit_button.place(x=180,y=450)

    mybutton9=Button(window4,text='BLOG',bg="#3F4E4F",fg="white",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window11)
    mybutton9.place(x=380,y=38)
    mybutton10=Button(window4,text='NEXT',bg="#3F4E4F",fg="white",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window4)
    mybutton10.place(x=480,y=38)
    mybutton11=Button(window4,text='HOME',bg="#3F4E4F",fg="white",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window2)
    mybutton11.place(x=575,y=38)

# Create label for result
    result_label = Label(window4, text="")
       
    window4.protocol("WM_DELETE_WINDOW", close_test_window3)


#DASHBOARD

def open_test_window2():
       window.withdraw()  # Hide the main window
       window3 = tk.Toplevel(window)  # Create a new window
       window3.title("OSTISMO")  # Set the title of the new window
       window3.geometry("800x570")  # Set the size of the new window
       window3.resizable(False,False)
       window3.configure(bg="#080202")

       def close_test_window2():
          window3.destroy()  # Destroy the new window
           # Show the main window again

       image02 = tk.PhotoImage(file="LOGO.png")
       label02 = tk.Label(window3, image=image ,bg="#080202") # Create a label to display the image
       label02.place(x=50,y=0) # PLACE the label into the window
       def open_page_match54():
         subprocess.Popen(["python","progress.py"]) 
       mybutton9=Button(window3,text='BLOG',bg="#080202",fg="white",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window11)
       mybutton9.place(x=350,y=38)
       mybutton10=Button(window3,text='REMINDER',bg="#080202",fg="white",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=reminder)
       mybutton10.place(x=448,y=38)
       mybutton11=Button(window3,text='PROGRESS',bg="#080202",fg="white",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_page_match54)
       mybutton11.place(x=555,y=38)
       mybutton12=Button(window3,text='SIGN OUT',bg="#080202",fg="white",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=login)
       mybutton12.place(x=680,y=38)
       
       
       frame5=Frame(window3,height=135,width=530,bg="#070A52",bd=1,relief=FLAT)
       frame5.place(x=120,y=95)
       image20 = tk.PhotoImage(file="3.png")
       label20 = tk.Label(window3, image=image20,bg="#070A52")
       label20.image = image20
       label20.place(x=420, y=95) 


       frame6=Frame(window3,height=135,width=530,bg="#8B1874",bd=1,relief=FLAT)
       frame6.place(x=120,y=250)
       image21 = tk.PhotoImage(file="2.png")
       label21 = tk.Label(window3, image=image21,bg="#8B1874")
       label21.image = image21
       label21.place(x=160, y=250)

       frame7=Frame(window3,height=135,width=530,bg="#DA0063",bd=1,relief=FLAT)
       frame7.place(x=120,y=405)
       image22 = tk.PhotoImage(file="1.png")
       label22 = tk.Label(window3, image=image22,bg="#DA0063")
       label22.image = image22
       label22.place(x=460, y=405)







       heading3 = Label(window3, text=" PLAY GAMES AND ", font=("Geologica", 17, "bold"),bg="#070A52",fg="white")
       heading3.place(x=148 ,y=107)
       heading4 = Label(window3, text=" EARN REWARDS ", font=("Geologica", 17, "bold"),bg="#070A52",fg="white")
       heading4.place(x=148 ,y=135 )


       mybutton9=Button(window3,text='TAP HERE',padx=23,pady=7,bg='#FFBF00',fg="white",relief=tk.RIDGE,cursor="hand2",command=open_test_window15)
       mybutton9.place(x=193,y=175)

       heading5 = Label(window3, text=" BOOST YOUR KIDDO'S ", font=("Geologica", 17, "bold"),bg="#8B1874",fg="white")
       heading5.place(x=340 ,y=272)
       heading6 = Label(window3, text=" SPEECH SKILLS ", font=("Geologica", 17, "bold"),bg="#8B1874",fg="white")
       heading6.place(x=380,y=300 )

       mybutton10=Button(window3,text='TAP HERE',padx=23,pady=7,bg='#FFBF00',fg="white",relief=tk.RIDGE,cursor="hand2",command=open_test_window6)
       mybutton10.place(x=425,y=335)

       heading7 = Label(window3, text=" TAP SYMBOLS,TYPE WORDS ", font=("Geologica", 17, "bold"),bg="#DA0063",fg="white")
       heading7.place(x=143 ,y=418)
       heading8 = Label(window3, text=" TO LEARN FAST ", font=("Geologica", 17, "bold"),bg="#DA0063",fg="white")
       heading8.place(x=143,y=445 )

       mybutton11=Button(window3,text='TAP HERE',padx=23,pady=7,bg='#FFBF00',fg="white",relief=tk.RIDGE,cursor="hand2",command=open_test_window3)
       mybutton11.place(x=193,y=485)

       



       window3.protocol("WM_DELETE_WINDOW", close_test_window2)
   
# Establish a connection to the Access database
#conn = pyodbc.connect(
   # r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
   # r'DBQ=C:\\Users\hp\Downloads\SE/PROJECT.accdb;'
#)

#  conn=pyodbc.connect(conn_str)

# Create a cursor
#cursor = conn.cursor()
 #   ----------------------------------------------LOGIN---------------------------------------------------------

def login():
    window.withdraw()  # Hide the main window
    window22 = tk.Toplevel(window)  # Create a new window
    window22.title("OSTISMO")  # Set the title of the new window
    window22.geometry("925x500+300+200")  # Set the size of the new window
    window22.resizable(True,True)
    window22.configure(bg="#fff")

    def close_test_window22():
        window22.destroy()  # Destroy the new window
          # Show the main window again
     
    


    image1 = tk.PhotoImage(file="login.png")
    label02 = tk.Label(window22, image=image1 ,bg="white") # Create a label to display the image
    label02.place(x=50,y=50)
    

    frame11 = Frame(window22, width=350, height=350, bg="white")
    frame11.place(x=550, y=120)
    heading1 = Label(window22, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading1.place(x=550, y=55)


    def on_enter(e):
       user1.delete(0, 'end')


    def on_leave(e):
       name = user1.get()
       username=name
       if name == '':
          user1.insert(0, 'username')


    user1 = Entry(window22, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11)) 
    user1.place(x=550, y=130)
    user1.insert(0, 'Username')
    user1.bind('<FocusIn>', on_enter)
    user1.bind('<FocusOut>', on_leave)
    

    Frame(window22, width=295, height=2, bg='black').place(x=550, y=157)


    def on_enter(e):
      print(password)
      code.delete(0, 'end')


    def on_leave(e):
      name = user1.get()
      if name == '':
         code.insert(0, 'password')


    code = Entry(window22, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    code.place(x=550, y=200)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
    
    def ok():
          global username
          username=user1.get()
          password=code.get()
          print(username,password)
          a=connection.con_login(username,password)
          print(a)
          if a==True:
               messagebox.showinfo("","LOGIN SUCCESFUL")
               open_test_window()
               return True
          else:
            messagebox.showinfo("","INCOREECT USERNAME AND PASSWORD")
            return False   
    


    Frame(window22, width=295, height=2, bg='black').place(x=550, y=227)

    Button(window22, width=39, pady=7, text="sign in", bg="#57a1f8", fg="white", border=0,command=ok).place(x=550, y=254)


    Label11 = Label(window22, text="Don't have an account?", fg="black", bg="white", font=('Microsoft YaHei UI Light', 9))
    Label11.place(x=550, y=320)

    sign_up11 = Button(window22, width=6, text="sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8")
    sign_up11.place(x=700, y=320)
    
    window22.mainloop()
    
    window22.protocol("WM_DELETE_WINDOW", close_test_window22)


#Dyslexia Test 
def open_test_window():
    window.withdraw()  # Hide the main window
    window2 = tk.Toplevel(window)  # Create a new window
    window2.title("OSTISMO")  # Set the title of the new window
    window2.geometry("800x600")  # Set the size of the new window
    window2.resizable(True,True)
    window2.configure(bg="white")

    def close_test_window():
        window2.destroy()  # Destroy the new window
         # Show the main window again

    def show_questions():
      global current_question_index
    
      question_info1 = questions[current_question_index]
      question_info2 = questions[current_question_index + 1]
      question_label1.config(text=question_info1["question"])
      question_label2.config(text=question_info2["question"])
    
    # Clear previous options
      for button in answer_buttons1:
        button.place_forget()
      for button in answer_buttons2:
        button.place_forget()
    
    # Create new options
      for i, option in enumerate(question_info1["options"]):
        answer_var1.set(-1)  # Deselect any previously selected option
        button = tk.Radiobutton(window2, text=option, variable=answer_var1, value=i,font=("arial", 12, ),bg=bg_color)
        button.place(x=75, y=265 + i * 40)
        answer_buttons1.append(button)
    
      for i, option in enumerate(question_info2["options"]):
        answer_var2.set(-1)  # Deselect any previously selected option
        button = tk.Radiobutton(window2, text=option, variable=answer_var2, value=i,font=("arial", 12,),bg=bg_color)
        button.place(x=382, y=265 + i * 40)
        answer_buttons2.append(button)
    
      current_question_index += 2

    def submit_answers():
      global scores
    
      selected_option1 = answer_var1.get()
      selected_option2 = answer_var2.get()
    
      if selected_option1 == -1 or selected_option2 == -1:
        messagebox.showwarning("No Answer Selected", "Please select an answer for both questions.")
        return
    
      question_info1 = questions[current_question_index - 2]
      question_info2 = questions[current_question_index - 1]
    
      selected_answer1 = question_info1["options"][selected_option1]
      selected_answer2 = question_info2["options"][selected_option2]
    
      score = 0
    
      if selected_answer1.lower() == question_info1["answer"].lower():
        score += 1
      if selected_answer2.lower() == question_info2["answer"].lower():
        score += 1
    
      scores[current_question_index - 2] = score  # Update the score for the first question
      scores[current_question_index - 1] = score  # Update the score for the second question
    
      if current_question_index >= len(questions):
        total_score = sum(scores)
        print(username)
        connection.con_insert(username,"Dyslexia Test",total_score)
        result_label.config(text="Your total score: {}/{}".format(total_score, len(questions)))
        
        if total_score >= 7:
            level_label.config(text="Level 1 dyslexia")
        elif total_score >= 4:
            level_label.config(text="Level 2 dyslexia")
        else:
            level_label.config(text="Level 3 dyslexia")
        
        next_button.config(state=tk.DISABLED)
        submit_button.config(state=tk.DISABLED)
      else:
         show_questions() 



    # Add content to the new window
    image01 = tk.PhotoImage(file="LOGO.png")
    label01 = tk.Label(window2, image=image ,bg="white") # Create a label to display the image
    label01.place(x=80,y=0) # PLACE the label into the window

    # Add a clock to the new window
    def update_clock():
        current_time = time.strftime("%I:%M:%S %p")  # Get the current time in 12-hour format
        clock_label.config(text=current_time)
        clock_label.after(1000, update_clock)



    clock_label = Label(window2, text="", font=("Arial", 15),bg="white")
    clock_label.place(x=670,y=5)
    
        
    

    update_clock()  # Start the clock

    # Add a button to go back to the main window

    frame2=Frame(window2,height=50,width=800,bg=color1,bd=1,relief=FLAT)
    frame2.place(x=0,y=100)

    heading2 = Label(window2, text=" DO I HAVE DYSLEXIA ", font=("Helvetica", 16, "bold"),bg=color1,fg="black",)
    heading2.place(x=290 ,y=108 )
    
    heading3 = Label(window2, text=" TAKE THE DYSLEXIC SCREEING TEXT", font=("arial", 14, "bold"),bg="white",fg="black",)
    heading3.place(x=240 ,y=160 )
    
    frame3=Frame(window2,height=770,width=800,bg=bg_color,bd=1,relief=FLAT)
    frame3.place(x=0,y=200)

    mybutton8=Button(window2,text='NEXT',padx=20,pady=5,bg='grey',fg="black",relief=tk.RIDGE,cursor="hand2",command=open_test_window2)
    mybutton8.place(x=540,y=45)

    answer_var1 = tk.IntVar()
    answer_var2 = tk.IntVar()

    question_label1 = tk.Label(window2, text="",bg=bg_color,font=("arial", 10, "bold"))
    question_label1.place(x=30, y=230)

    question_label2 = tk.Label(window2, text="",bg=bg_color,font=("arial", 10, "bold"))
    question_label2.place(x=370, y=230)

    next_button = tk.Button(window2, text="Next", command=show_questions,bg=bg_color,width=14)
    next_button.place(x=200, y=450)

    submit_button = tk.Button(window2, text="Submit", command=submit_answers, bg=bg_color,width=14)
    submit_button.place(x=350, y=450)

    result_label = tk.Label(window2, text="",bg=bg_color,font=("arial", 14, "bold"))
    result_label.place(x=270, y=480)

    level_label = tk.Label(window2, text="",bg=bg_color,font=("arial", 14, "bold"))
    level_label.place(x=270, y=510)

    show_questions()

    

    
   



    window2.protocol("WM_DELETE_WINDOW", close_test_window)


# Create the main window                                  #MAIN
window = tk.Tk()

# Set the background color to white
window.configure(bg="#E6E6E6") #background color
window.title("OTSIMO")         #window tittle  
window.iconbitmap("LOGO.png")  #window logo
window.geometry("800x570")     #window size
window.resizable(False, False)

color1="#B2A4FF"    #purple 
bg_color="#E6E6E6"  #bg color of window 


mybutton=Button(window,text='LOG IN ',bg=bg_color,fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=login)
mybutton.place(x=35,y=42)  

mybutton1=Button(window,text='DYSLEXIA TEST',padx=20,pady=5,bg='grey',fg="black",relief=tk.RIDGE,cursor="hand2",command=login)
mybutton1.place(x=540,y=45)

mybutton2=Button(window,text='SHOP',padx=20,pady=5,bg='grey',fg="black",relief=tk.RIDGE,cursor="watch",state=DISABLED)
mybutton2.place(x=690,y=45)

frame=Frame(window,height=50,width=800,bg=color1,bd=1,relief=FLAT)
frame.place(x=0,y=100)

mybutton3=Button(window,text='ABOUT US  ',bg=color1,fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window9)
mybutton3.place(x=46,y=108)

mybutton4=Button(window,text='CONTACT US  ',bg=color1,fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window10)
mybutton4.place(x=245,y=108)

mybutton5=Button(window,text='ABOUT DYSLEXIA  ',bg=color1,fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window11)
mybutton5.place(x=444,y=108) 

mybutton6=Button(window,text='BLOGS ',bg=color1,fg="black",relief=tk.FLAT, borderwidth=0,font=("Georgia", 12, "underline"), underline=0,cursor="hand2",command=open_test_window11)
mybutton6.place(x=660,y=108) 

frame1=Frame(window,height=120,width=800,bg=color1,bd=1,relief=FLAT)
frame1.place(x=0,y=200)

heading1 = Label(window, text=" WHAT ARE DYSLEXIC ADVANTAGES ", font=("Helvetica", 16, "bold"),bg="#E6E6E6",fg="black",)
heading1.place(x=240 ,y=335 )

image2 = tk.PhotoImage(file="IPHONE.png")
label1 = tk.Label(window, image=image2 ,bg=bg_color)
label1.place(x=390,y=368)

canvas = tk.Canvas(window, width=image2.width(), height=image2.height(),bg="#E6E6E6",highlightthickness=0)
canvas.place(x=400,y=380)
canvas.create_image(0, 0, anchor="nw", image=image2)

text = "Scientific research shows that dyslexic children \n and adults process information differently from non-\ndyslexics and some of these changes may account\n for strengths in creative problem solving, entrepre\n -neurial thinking, and certain types of learning\nand memory.\nEmbrace your unique mind and see beyond the\n challenges"
position = (53, 30)
font = ("Arial", 9, )
fill_color = "BLACK"

canvas.create_text(position, text=text, fill=fill_color, font=font, anchor="nw")


image = tk.PhotoImage(file="LOGO.png")
label = tk.Label(window, image=image ,bg=bg_color) # Create a label to display the image
label.place(x=260,y=0) # PLACE the label into the window

image1 = tk.PhotoImage(file="pic1.png")
label2 = tk.Label(window, image=image1 ,bg=bg_color)
label2.place(x=70,y=370)

heading1 = Label(window, text=" DO YOU THINK YOU MAY BE DYSLEXIC ", font=("Helvetica", 12, "bold"),bg=color1,fg="black",)
heading1.place(x=255,y=208)

mybutton7=Button(window,text='TAKE THE TEST NOW ',padx=50,pady=15,bg='#7DB9B6',fg="black",relief=tk.RIDGE,cursor="hand2",command=login)
mybutton7.place(x=290,y=243)

#defining a function to get clock 
def update_clock():
    current_time = time.strftime("%I:%M:%S %p")  # Get the current time in 12-hour format  strftime from time lib
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock) 

clock_label = tk.Label(window, text="", font=("Arial", 15),bg="#E6E6E6") #label that shows a clock
clock_label.place(x=670,y=5)

update_clock() # Start the clock


# Run the main event loop
window.mainloop()

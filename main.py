BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random
#--------------------------------------------CSV File-----------------------------------------------#

def cards():
    global french_word
    global english_word
    global data

    data=pandas.read_csv("words_to_learn.csv")
    french_word=random.choice(data["French"])
    # print(french_word)
    english_word=data.loc[(data.French==french_word),"English"].item()

cards()


#------------------------------------------UI Setup------------------------------------------#

window=Tk()
window.title("  Flashy")
window.config(padx=50,pady=50,background="#B1DDC6")



canvas=Canvas(width=800,height=526,bg="#B1DDC6",highlightthickness=0)
card=PhotoImage(file="card_front.png")
img=canvas.create_image(400,263,image=card)
canvas.grid(row=0,column=0,columnspan=2)
title=canvas.create_text(400,150,text="French",font=("Arial",40,"italic"))
french=canvas.create_text(400,263,text=french_word,font=("Arial",60,"bold"))


def change_french():
    canvas.itemconfig(french, text=french_word)

def flip_card():
    flip=PhotoImage("image/card_back.png")
    canvas.itemconfig(img,image=flip)
    canvas.itemconfig(french,text=english_word,fill="white")
    canvas.itemconfig(title,text="English",fill="white")



def next_french():
    canvas.itemconfig(french, text=french_word,fill="black")
    # flip = PhotoImage("image/card_front.png")
    canvas.itemconfig(img, image=card)
    canvas.itemconfig(title, text="French", fill="black")
    window.after(3000, flip_card)

def remove_words():

    data.drop(data.index[(data.French == french_word)], axis=0, inplace=True)

    data.to_csv("words_to_learn.csv")



wrong_img=PhotoImage(file="C:\\Users\\shrey\\PycharmProjects\\Day 31 Flash Card App\\flash-card-project-start\\images\\wrong.png")
wrong=Button(image=wrong_img,highlightthickness=0,command=lambda:[cards(), change_french(),next_french()])
wrong.grid(row=1,column=0)

check_img = PhotoImage(file="C:\\Users\\shrey\\PycharmProjects\\Day 31 Flash Card App\\flash-card-project-start\\images\\right.png")
check=Button(image=check_img,highlightthickness=0,command=lambda:[cards(), change_french(),next_french(),remove_words()])
check.grid(row=1,column=1)


window.after(3000,flip_card)

window.mainloop()


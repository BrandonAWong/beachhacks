from Emotion import Emotion
from tkinter import *
from PIL import ImageTk, Image
from time import sleep
import os

def tki():
    # Create an instance of tkinter window
    win = Tk()
    # Define the geometry of the window
    win.geometry("700x500")

    frame = Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    wd = f'{os.getcwd()}\\catt'
    print(emotion.emotion)
    match emotion.emotion:
        case('happy'):
            file_name = f"{wd}\\happy_cat.bmp"
        case('sad'):
            file_name = f"{wd}\\sad_cat.bmp"
        case('angry'):
            file_name = f"{wd}\\angry_cat.bmp"
        case('neutral'):
            file_name = f"{wd}\\neutral_cat.bmp"
        case('disgusted'):
            file_name = f"{wd}\\disgusted_cat.bmp"
    print(file_name)
    img = ImageTk.PhotoImage(Image.open(file_name))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image = img)
    label.pack()

    win.mainloop()

emotion = Emotion()
emotion.capture_emotion()
tki()



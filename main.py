# from Emotion import Emotion
from tkinter import *
import PySimpleGUI as sg
from PIL import ImageTk, Image
from os import getcwd
from time import sleep
# from google.cloud import dialogflow_v2 as dialogflow
# from google.api_core.exceptions import InvalidArgument

# DIALOGFLOW_PROJECT_ID = 'beachhacks-378923'
# DIALOGFLOW_LANGUAGE = "en-US"
# SESSION_ID = "123456789"
# sessionClient = dialogflow.SessionsClient()
# session = sessionClient.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

def start():


#__________________________________________________________________________________________________________________________________________
    wd = f'{getcwd()}/catt'
    win = Tk()
    win.configure(background='#D3D3D3')
    win.title('🐈 Bot')
    win.geometry("1920x1080")
    win.iconbitmap(f'{wd}cat_icon.ico')

    frame = Frame(win, width=600, height=400, background="#D3D3D3")
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    
    file_name = f'{wd}/loading_cat.bmp'
    img = ImageTk.PhotoImage(Image.open(file_name))
    imgLabel = Label(frame, image = img, background="#D3D3D3")
    imgLabel.pack()

    t = Text(frame, width = 50, height = 10,  background="#D3D3D3")
    t.propagate(False)
    t.pack()
    textLabel = Label(t, font=('Yu Gothic UI', 13), text="", background="#D3D3D3", fg='#702963')
    textLabel.pack()  
    textScrollbar = Scrollbar(t, orient='vertical')
    textScrollbar.config(command=t.yview)
    textScrollbar.pack(side='right', fill=Y)
    text = "stand still I'm capturing your emotions!"
    global userLabel
    userLabel = Label(t, text='', fg='#008000',font=('Yu Gothic UI', 13), background="#D3D3D3")
    print_text(text, textLabel, win)

    # emotion.capture_emotion()
    
    img = ImageTk.PhotoImage(Image.open('img.png'))
    imgLabel['image'] = img
    textLabel['text'] = ''
    text = 'picking the perfect emotion...'
    print_text(text, textLabel, win)
    sleep(3)

    # match emotion.emotion:
    #     case('happy'):
    #         file_name = f"{wd}\\happy_cat.bmp"
    #     case('sad'):
    #         file_name = f"{wd}\\sad_cat.bmp"
    #     case('angry'):
    #         file_name = f"{wd}\\angry_cat.bmp"
    #     case('neutral'):
    #         file_name = f"{wd}\\neutral_cat.bmp"
    #     case('disgusted'):
    #         file_name = f"{wd}\\disgusted_cat.bmp"
    #     case('fear'):
    #         file_name = f"{wd}\\fear_cat.bmp"
    #     case('surprise'):
    #         file_name = f"{wd}\\suprise_cat.bmp"
    file_name = f"{wd}/happy_cat.bmp"

    img = ImageTk.PhotoImage(Image.open(file_name))
    imgLabel['image'] = img
    # text = f"i'm {emotion.emotion}"
    win.update()
    textLabel['text'] = ''
    dialog = get_dialog(text)
    print(print_text(dialog, textLabel, win))
    
    inputFrame = Frame(frame)
    inputFrame.pack()
    userInputBox = Entry(inputFrame, font=('Yu Gothic UI', 10))
    userInputBox.pack(pady=10, ipadx=300, ipady=5, side='left')
    submitButton = Button(inputFrame, text='🐈‍', command=lambda: submit_input(userInputBox, textLabel, win))
    submitButton.pack(side='right', padx=5)

    win.mainloop()

def get_dialog(text):
    # textInput = dialogflow.types.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE)
    # query = dialogflow.types.QueryInput(text=textInput)
    # try:
    #     response = sessionClient.detect_intent(session=session, query_input=query)
    # except InvalidArgument:
    #     raise 
    # return response.query_result.fulfillment_text
    return ("fuck you\n")

def submit_input(userInputBox, textLabel, win):
     userInput = userInputBox.get()
     userInputBox.delete(0, END)
     print_text(userInput, userLabel, win)
     dialog = get_dialog(userInput)
     print_text(dialog, textLabel, win)

def print_text(text, label, win):
    label.pack()
    for letter in text:
        label['text'] += letter
        win.update()
        sleep(0.05)


if __name__ == "__main__":
    # emotion = Emotion()
    #add button make text nicer and stuff and make a go go button at very beginning
    start()

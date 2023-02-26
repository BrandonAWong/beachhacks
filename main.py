from Emotion import Emotion
from tkinter import *
from PIL import ImageTk, Image
from os import getcwd
from time import sleep
from google.cloud import dialogflow_v2 as dialogflow
from google.api_core.exceptions import InvalidArgument

DIALOGFLOW_PROJECT_ID = 'beachhacks-378923'
DIALOGFLOW_LANGUAGE = "en-US"
SESSION_ID = "123456789"
sessionClient = dialogflow.SessionsClient()
session = sessionClient.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

def start():
    wd = f'{getcwd()}\\catt'
    win = Tk()
    win.configure(background='#D3D3D3')
    win.title('🐈 Bot')
    win.geometry("1920x1080")
    win.iconbitmap(f'{wd}\\cat_icon.ico')

    frame = Frame(win, width=600, height=400, background="#D3D3D3")
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    
    file_name = f'{wd}\\loading_cat.bmp'
    img = ImageTk.PhotoImage(Image.open(file_name))
    imgLabel = Label(frame, image = img, background="#D3D3D3")
    imgLabel.pack()

    global t
    t = Text(frame, width = 100, height = 10,  background="#D3D3D3")
    t.propagate(False)
    t.pack()
    
    #textLabel = Label(t, font=('Yu Gothic UI', 13), text="", background="#D3D3D3", fg='#702963')
    #textLabel.pack(side='left')  
    textScrollbar = Scrollbar(t, orient='vertical')
    textScrollbar.config(command=t.yview)
    textScrollbar.pack(side='right', fill=Y)
    text = "stand still I'm capturing your emotions!"
    #userLabel = Label(t, text='', fg='#008000',font=('Yu Gothic UI', 13), background="#D3D3D3")
    thing = print_text(text, win, '#702963', 'left')

    emotion.capture_emotion()
    thing.pack_forget()
    img = ImageTk.PhotoImage(Image.open('img.png'))
    imgLabel['image'] = img
    #textLabel['text'] = ''
    text = 'picking the perfect emotion...'
    otherThing = print_text(text, win,'#702963', 'left')
    sleep(3)

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
        case('fear'):
            file_name = f"{wd}\\fear_cat.bmp"
        case('surprise'):
            file_name = f"{wd}\\suprise_cat.bmp"

    img = ImageTk.PhotoImage(Image.open(file_name))
    imgLabel['image'] = img
    text = f"i'm {emotion.emotion}"
    otherThing.pack_forget()
    win.update()
    #textLabel['text'] = ''
    dialog = get_dialog(text)
    print_text(dialog, win, '#702963')
    
    inputFrame = Frame(frame)
    inputFrame.pack()
    userInputBox = Entry(inputFrame, font=('Yu Gothic UI', 10))
    userInputBox.pack(pady=10, ipadx=300, ipady=5, side='left')
    submitButton = Button(inputFrame, text='🐈‍', command=lambda: submit_input(userInputBox, win))
    submitButton.pack(side='right', padx=5)
    resetButton = Button(inputFrame,text="RESET", command=lambda: reset(win))
    resetButton.pack()

    win.mainloop()

def get_dialog(text):
    textInput = dialogflow.types.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE)
    query = dialogflow.types.QueryInput(text=textInput)
    try:
        response = sessionClient.detect_intent(session=session, query_input=query)
    except InvalidArgument:
        raise 
    return response.query_result.fulfillment_text

def submit_input(userInputBox, win):
     userInput = userInputBox.get()
     userInputBox.delete(0, END)
     print_text(userInput, win, '#008000')
     dialog = get_dialog(userInput)
     print_text(dialog, win, '#702963')

def print_text(text, win, color, ore=None):
    label = Label(t, font=('Yu Gothic UI', 13), text="", background="#D3D3D3", fg=color)
    label.pack(side=ore)
    for letter in text:
        label['text'] += letter
        win.update()
        sleep(0.05)
    return label

def reset(win):
    win.destroy()
    start()

if __name__ == "__main__":
    emotion = Emotion()
    #add button make text nicer and stuff and make a go go button at very beginning
    start()

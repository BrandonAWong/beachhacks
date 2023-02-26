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
    win = Tk()
    win.title('Cat Therapy')
    win.geometry("1000x700")

    frame = Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    wd = f'{getcwd()}\\catt'
    file_name = f'{wd}\\loading_cat.bmp'
    img = ImageTk.PhotoImage(Image.open(file_name))
    imgLabel = Label(frame, image = img)
    imgLabel.pack()
    textLabel = Label(frame, text="stand still I'm capturing your emotions!")
    textLabel.pack()  
    win.update()

    emotion.capture_emotion()
    textLabel['text'] = 'picking the perfect emotion...'
    img = ImageTk.PhotoImage(Image.open('img.png'))
    imgLabel['image'] = img
    win.update()
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
    win.update()
    dialog = start_dialog(text)
    textLabel['text'] = ''
    for letter in dialog:
        textLabel['text'] += letter
        win.update()
        sleep(0.05)
    userInputBox = Entry(frame)
    userInputBox.pack()
    userInput = userInputBox.get()
    #LEFT OFF HERE NEED A BUTTON TO SUBMIT TEXT
    win.mainloop()

def start_dialog(text):
    textInput = dialogflow.types.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE)
    query = dialogflow.types.QueryInput(text=textInput)
    try:
        response = sessionClient.detect_intent(session=session, query_input=query)
    except InvalidArgument:
        raise 
    print("query:", response.query_result.query_text)
    print("Detected intent:", response.query_result.intent.display_name)
    print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    print("Fulfillment text:", response.query_result.fulfillment_text)
    return response.query_result.fulfillment_text


if __name__ == "__main__":
    emotion = Emotion()
    #add button make text nicer and stuff and make a go go button at very beginning
    start()

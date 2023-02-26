# from deepface import DeepFace
import cv2
from tkinter import *
from PIL import ImageTk, Image
from threading import *
from time import sleep


def vid():

    # define a video capture object
    vid = cv2.VideoCapture(0)
    
    while(True):
        
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
    
        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

def threading():
    t1 = Thread(target=vid)
    t1.start()

global file_name 
file_name="catt/cat0.jpeg"

threading()


# Create an instance of tkinter window
win = Tk()
# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk

img = ImageTk.PhotoImage(Image.open(file_name))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

win.mainloop()










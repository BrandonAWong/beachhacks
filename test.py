import tkinter as tk
from PIL import ImageTk, Image


root = tk.Tk()

img = ImageTk.PhotoImage(Image.open("catt/cat1.jpeg"))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

def callback(e):
    img2 = ImageTk.PhotoImage(Image.open("catt/cat2.jpeg"))
    panel.configure(image=img2)
    panel.image = img2

root.bind("<Return>", callback)
root.mainloop()
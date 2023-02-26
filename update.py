import PySimpleGUI as sg
import cv2
from PIL import ImageTk, Image

import numpy as np

def main():
    sg.theme("LightGreen")

    layout = [
        [sg.Text("OpenCV Demo", size=(225, 1), justification="center")],
        [sg.Image(filename="", key="-IMAGE-")],
        [
            sg.Radio("cat number", "Radio", True, size=(10, 1), key="-THRESH-"),
            sg.Slider(
                (0, 3),
                0,
                1,
                orientation="v",
                size=(4, 15),
                key="-THRESH SLIDER-",
            ),
        ],
        [sg.Button("Exit", size=(10, 1))],
    ]
        # window = sg.Window("OpenCV Integration", layout, location=(1, 1))
    # event, values = window.read(timeout=20)
    # while True:
    #         if event == "Exit" or event == sg.WIN_CLOSED:
    #             break

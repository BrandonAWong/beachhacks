import cv2
from deepface import DeepFace

class Emotion():
    def __init__(self):
        self.emotion = None
    
    def capture_emotion(self):
        vid = cv2.VideoCapture(0)
        while(True):
            ret, frame = vid.read()
            cv2.imwrite('img.png', frame)
            try:
                face_analysis = DeepFace.analyze(img_path = "img.png")
                self.emotion = str((face_analysis[0]['dominant_emotion']))
            except ValueError as e:
                pass
            if self.emotion:
                break
        vid.release()

    def get_emotion(self):
        return self.emotion
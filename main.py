from deepface import DeepFace
import cv2

vid = cv2.VideoCapture(0)

while(True):
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    image = vid.read()
    cv2.imwrite('img.png', frame)
    try:
        face_analysis = DeepFace.analyze(img_path = "img.png")
    except:
        pass
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
vid.release()
cv2.destroyAllWindows()



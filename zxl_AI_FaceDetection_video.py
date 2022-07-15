#Face decetion
import cv2
from random import randrange
trained_face_data=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

webcam=cv2.VideoCapture(0) #(0)default camera
# webcam=cv2.VideoCapture("2.mp4")

while True:
    successful_frame_read, frame=webcam.read()

    grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(0, 128), randrange(0, 128), randrange(0, 128)), 5)
        # cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0,256), 5)
    cv2.imshow("Face Detector in video",frame)
    key=cv2.waitKey(1)
    if key==81 or key==113:
        break
#release the memory
webcam.release()

print("zxl ! bravo!")

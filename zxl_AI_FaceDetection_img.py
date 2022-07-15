#Face decetion
import cv2
from random import randrange
trained_face_data=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("4.jpg")

grayscaled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)

for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (randrange(128,256), randrange(128,256), randrange(128,256)), 10)

# print(face_coordinates)


cv2.imshow("Face Detector", img)
cv2.waitKey()

print("zxl ! bravo!")

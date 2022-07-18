#pip install qrcode[pi].Decode QRcode
import cv2
detector=cv2.QRCodeDetector()

content,point,matrix=detector.detectAndDecode(cv2.imread("BravoXL.png"))
print(content)
print(point)
print(matrix)

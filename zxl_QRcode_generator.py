#pip install qrcode[pi]
import qrcode
img=qrcode.make("https://github.com/BravoXL")
img.save("BravoXL.png")
# advanced method
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_M,
                 box_size=10,border=4)
qr.add_data("https://github.com/BravoXL")
qr.make(fit=True)
img2=qr.make_image(fill_color=(0,256,0),back_color=(128,128,128))
img2.save("BravoXL_green.png")
import qrcode

img = qrcode.make("https://www.sigzen.com/")
img.save("sigzen.jpg")
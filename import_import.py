import qrcode
image = qrcode.make("Engineering in kannada")
image.save("eik_qr.png")

print("QR code generation successfull")
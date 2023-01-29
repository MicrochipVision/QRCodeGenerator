import qrcode

def url_to_qr(url, size, correction):
    qr = qrcode.QRCode(
        version=None,
        error_correction=correction,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white", size=(size, size))
    return img

url = input("Enter the URL to be converted to QR code: ")
size = int(input("Enter the size of the image (in pixels): "))
correction_level = input("Enter the error correction level (L, M, Q, H): ")
correction = getattr(qrcode.constants, "ERROR_CORRECT_" + correction_level.upper(), qrcode.constants.ERROR_CORRECT_L)
img = url_to_qr(url, size, correction)
img.save("qr_code.png")

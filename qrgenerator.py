#install all libraries needed
#create a function that collect a text and convert it is to qr code
# save the qrcode as an image 
# run the function


import qrcode 

def gegnerate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_clolor="black",back_clolor="white")
    img.save('qrcode.png')
gegnerate_qrcode("www.youtube.com")    
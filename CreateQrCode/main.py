import pyqrcode

input_url = input("Enter url: ")
url = pyqrcode.create(input_url)
url.svg('qrcode.svg', scale=8)

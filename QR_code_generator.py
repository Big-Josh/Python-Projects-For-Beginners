import qrcode

data = input('Enter the text or URL: ').strip()

filename = input('Enter file name: ').strip()

img = qrcode.make(data)

type(img)

img.save(f'{}.png')
import qrcode

website = 'https://github.com/krishnaik06'

img = qrcode.make(website)

type(img)

img.save('KrishNaikGit.png')
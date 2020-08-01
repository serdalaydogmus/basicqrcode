# -*- coding: utf-8 -*-



import qrcode

qr = qrcode.QRCode(
	version=1,
	box_size=15,
	border=5
)

data = 'https://www.ntv.com.tr'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('testtest110x.png')

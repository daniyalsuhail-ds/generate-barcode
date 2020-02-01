# install package
# type pip install python-barcode in command prompt/terminal

from barcode.writer import ImageWriter
import barcode
# there are many barcode types
# select what you need
# check it on pypi.org/project/python-barcode
hr = barcode.get_barcode_class('ean13')
Hr = hr('0234564257425')
# svg file will be created using ean13
qr = Hr.save('barcode')


# image file or png file
# import pillow library to use code39
gr = barcode.get_barcode_class('code39',)
Gr = gr('1234567891011', writer=ImageWriter())
qr = Gr.save('pngbarcode')


# QR codes are used to encode and decode the data into a machine-readable form.
# The use of camera phones to read two-dimensional barcodes for various purposes

import pyqrcode
from pyqrcode import QRCode
s = "www.google.com"
URL = pyqrcode.create(s)
URL.svg("google.svg", scale=8, background="grey")

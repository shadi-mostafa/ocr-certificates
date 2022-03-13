import re
import cv2
import pytesseract
from pytesseract import Output

# read image file
img = cv2.imread('sample.jpg')
d = pytesseract.image_to_data(img, output_type=Output.DICT)
keys = list(d.keys())

date_pattern = '(1|2)(\d{9})'

n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
    	if re.match(date_pattern, d['text'][i]):
            print(d['text'][i])
#	        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#	        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imwrite('img1.jpg', img)

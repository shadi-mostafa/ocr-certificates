import os
import re
import cv2
import pytesseract
from pytesseract import Output
from PIL import Image

path_of_the_directory = r'./images/'
ext = ('.jpeg', 'jpg')
for file in os.scandir(path_of_the_directory):
    if file.path.endswith(ext):
        #print(file)
        # PIL open image
        #image = Image.open(path_of_the_directory + os.path.basename(file))
        #image_text = pytesseract.image_to_string(image)
        # CV2 open image
        image = cv2.imread(path_of_the_directory + os.path.basename(file))
        enlarged_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        # working with enlarged_image
        enhanced_image = cv2.GaussianBlur(enlarged_image, (5, 5), 0)
        #enhanced_image = cv2.bilateralFilter(image, 9,75,75)
        image_text = pytesseract.image_to_string(enhanced_image)
        #id_num = re.search(r'[1|2]\d{9}',image_text)
        id_num = re.findall(r'[1|2]\d{9}',image_text)
        print(os.path.basename(file) + ": ",*id_num)
        #converted = image.convert('RGB')
        #converted.save(os.path.splitext(file)[0]+'.pdf')
        #converted.save(path_of_the_directory + id_num.group()+'.pdf')


#img = cv2.imread(r'sample.jpg')
#d = pytesseract.image_to_data(img, output_type=Output.DICT)
#keys = list(d.keys())
#
#iqama_pattern = r'(1|2)(\d{9})'
#
#n_boxes = len(d['text'])
#for i in range(n_boxes):
    #if int(d['conf'][i]) > 60:
    	#if re.match(iqama_pattern, d['text'][i]):
            #print("data output",d['text'][i])
            #with open(d['text'][i]+'.pdf', 'w+b') as f:
                #f.write(img)
##	        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#	        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

#cv2.imwrite('img1.jpg', img)

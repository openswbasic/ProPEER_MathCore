# -*- coding: utf-8 -*-
"""
Created on Sun May 30 00:01:44 2021

@author: HY Park
"""

import pytesseract
import re
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

image = cv2.imread('sample2.jpg', cv2.IMREAD_COLOR)
text =pytesseract.image_to_string(image, lang='kor+eng', config='-c preserve_interword_spaces=1 --oem 3 --psm 1')  
t = text.replace(" ","")
size_table = re.split('\n',text)

with open("sample2.txt", "w", encoding="utf8") as f:
    f.write(text)
    f.write("\n\n\n")
    f.write(text.replace("  ", ""))
    
print(size_table)
from PIL import Image
import pytesseract
import re
import numpy as np
import os

os.chdir("Desktop\\Week 1\\Small Projects\\OCR\\")
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
text = str(((pytesseract.image_to_string(Image.open("invoice from ClearOne (1).png")))))
text = text.replace(',', '')
print(text)
num_lst = re.findall('[-+]?([0-9]+\.[0-9]*)[^%]', text)
num_lst = np.array([float(i) for i in num_lst])
print(num_lst)
print(num_lst.max())
        
        


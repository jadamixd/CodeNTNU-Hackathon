#import Pillow
from PIL import Image
import pytesseract as pyt
import numpy as np

#OBS: KUN BRUK KOK

def image_prossesing():

    filename = r'C:\Users\Jakob\Scripts\Python\StartNTNU_Hackathon\image_01.jpg' 
    img1 = np.array(Image.open(filename)) 
    text = pyt.image_to_string(img1)

    print(text)



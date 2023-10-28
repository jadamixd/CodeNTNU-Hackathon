# Library imports
from PIL import Image
import pytesseract as pyt
import numpy as np

# Other file imports
from camera.imagetext_extraction import extract_text_from_image, extracting_relevant_text

# -------------------------------- #

# Code to take and automatically crop image

# -------------------------------- #

# Path to the Tesseract executable (update this with your installation path)
pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Provide the path to the image of the receipt
# Change path to the processed image
image_path = r'mockdata\kvitto.jpg'

# Call the OCR function
extracted_text = extract_text_from_image(image_path)

# Checks if extraction was successfull
if extracted_text:
    # Print the extracted text
    print("Extracted Text:")
    print(extracted_text)
else:
    print("Text extraction failed.")

print(extracted_text)
# extracted_text is now a string containing all words in the picture

# -------------------------------- #

# Data handling code
extracting_relevant_text(extracted_text)

# -------------------------------- #

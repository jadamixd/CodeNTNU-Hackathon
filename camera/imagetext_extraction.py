import pytesseract as pyt
from PIL import Image

# Path to the Tesseract executable (update this with your installation path)
pyt.pytesseract.tesseract_cmd = r'C:\Users\Jakob\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Function to extract text from an image using OCR
def extract_text_from_image(image_path):
    try:
        # Open the image using Pillow (PIL)
        image = Image.open(image_path)

        # Perform OCR on the image
        text = pyt.image_to_string(image, lang="nor")   

        return text
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Function to extract the relevant parts from the extracted string
def extracting_relevant_text(extracted_text):
    
    # do something

    return extracted_text

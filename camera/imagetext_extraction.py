import pytesseract as pyt
from PIL import Image
import openai

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

    openai.organization = "org-9OoTo5Wv0pe2EQPsMF29hS2M"
    openai.api_key = "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"

    openai.Model.list()

    response = openai.Completion.create(
        model="gpt-3.5-turbo-0613",
        prompt=str(
            f"Kan du filtrere ut matvarene i teksten og sette det inn i en python liste?: {extracted_text}"),
        max_tokens=200,
        temperature=20
    )

    print(response)

    return extracted_text

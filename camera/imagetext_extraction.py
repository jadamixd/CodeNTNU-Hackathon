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
    try:
        # insert organization and api key

        # openai.Model.list()

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=str(
                f"Kan du filtrere ut matvarene fra kvitteringen under og gi det som en komma separert streng?: {extracted_text}"),
            max_tokens=2000,
            temperature=0
        )

        extracted_text_list = response['choices'][0]['text'].split(",")

        print(extracted_text_list)

        return extracted_text_list

    except:
        print("total failure!")
        return []

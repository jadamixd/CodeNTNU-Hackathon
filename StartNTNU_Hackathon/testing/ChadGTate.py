import pytesseract
from PIL import Image

# Path to the Tesseract executable (update this with your installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Jakob\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Function to extract text from an image using OCR
def extract_text_from_image(image_path):
    try:
        # Open the image using Pillow (PIL)
        image = Image.open(image_path)

        # Perform OCR on the image
        text = pytesseract.image_to_string(image)   

        return text
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    # Provide the path to the image of the receipt
    image_path = r'C:\Users\Jakob\Scripts\Python\StartNTNU_Hackathon\mockdata\dank_meme.png'  # Change this to your image file

    # Call the OCR function
    extracted_text = extract_text_from_image(image_path)

    if extracted_text:
        # Print the extracted text
        print("Extracted Text:")
        print(extracted_text)
    else:
        print("Text extraction failed.")



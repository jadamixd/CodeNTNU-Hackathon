import pytesseract as pyt
from PIL import Image
import openai
import cv2
import numpy as np

# Path to the Tesseract executable (update this with your installation path)
pyt.pytesseract.tesseract_cmd = r'C:\Users\Jakob\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Function to extract text from an image using OCR


def extract_text_from_image(image_path):
    try:
        # Load the image
        image = cv2.imread(image_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to create a binary image
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

        # Find contours in the binary image
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Initialize variables to track the largest white rectangle
        largest_area = 0
        largest_contour = None

        # Process each contour
        for contour in contours:
            # Calculate the area of the contour
            area = cv2.contourArea(contour)

            # Check if the area is larger than the current largest
            if area > largest_area:
                largest_area = area
                largest_contour = contour

        # Get the coordinates of the bounding box around the largest white contour
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Crop the region containing the largest white contour
        largest_white_contour = image[y:y+h, x:x+w]

        # Save the resized image as a single image
        cv2.imwrite("static\image_new.jpg", largest_white_contour)

        kernel = np.array([[0, -1, 0],
                        [-1, 5,-1],
                        [0, -1, 0]])
        image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

        # img = cv2.imread("static\image_new.jpg", 1)
        # converting to LAB color space
        lab= cv2.cvtColor(image_sharp, cv2.COLOR_BGR2LAB)
        l_channel, a, b = cv2.split(lab)

        # Applying CLAHE to L-channel
        # feel free to try different values for the limit and grid size:
        clahe = cv2.createCLAHE(clipLimit=0.5, tileGridSize=(3,3))
        cl = clahe.apply(l_channel)

        # merge the CLAHE enhanced L-channel with the a and b channel
        limg = cv2.merge((cl,a,b))

        # Converting image from LAB Color model to BGR color spcae
        enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

        # Stacking the original image with the enhanced image
        cv2.imwrite("static\image_new.jpg",enhanced_img)

        # Open the image using Pillow (PIL)
        image = Image.open("static\image_new.jpg")

        # Perform OCR on the image
        text = pyt.image_to_string(image)#, lang="nor")

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
                f"Kan du filtrere ut matvarer fra kvitteringen under og gi det som en komma separert streng? Rett opp i skrivefeil, og ignorer tall og ord som ikke er mat: {extracted_text}"),
            max_tokens=2000,
            temperature=0
        )

        extracted_text_list = response['choices'][0]['text'].split(",")

        print(extracted_text_list)

        return extracted_text_list

    except:
        print("total failure!")
        return []

import cv2
import numpy as np

# Load the image
image = cv2.imread("/Users/magnusgogstad/Desktop/ImageCroppingInputs/image.jpg")

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
cv2.imwrite("/Users/magnusgogstad/Desktop/ImageCroppingOutputs/image_new.jpg", largest_white_contour)

kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

img = cv2.imread('/Users/magnusgogstad/Desktop/ImageCroppingOutputs/image_new.jpg', 1)
# converting to LAB color space
lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l_channel, a, b = cv2.split(lab)

# Applying CLAHE to L-channel
# feel free to try different values for the limit and grid size:
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(12,12))
cl = clahe.apply(l_channel)

# merge the CLAHE enhanced L-channel with the a and b channel
limg = cv2.merge((cl,a,b))

# Converting image from LAB Color model to BGR color spcae
enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

# Stacking the original image with the enhanced image
result = np.hstack((img, enhanced_img))
cv2.imwrite('/Users/magnusgogstad/Desktop/ImageCroppingOutputs/output_Image1.jpg',result)
cv2.imshow('Result', result)
cv2.waitKey()
cv2.destroyAllWindows()


#cv2.imshow('/Users/magnusgogstad/Desktop/outpiin.jpg', image_sharp)
#cv2.waitKey()
#cv2.destroyAllWindows()

import cv2
import numpy as np
# Initialize the camera
cap = cv2.VideoCapture(0)  # 0 represents the default camera (usually the built-in webcam)

# Initialize the movable border coordinates
x1, y1, x2, y2 = 100, 100, 300, 200

# Variables for handling mouse events
dragging = False
start_x, start_y = None, None

def draw_border(frame):
    # Draw the border on the frame
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green border

def mouse_callback(event, x, y, flags, param):
    global x1, y1, x2, y2, dragging, start_x, start_y

    if event == cv2.EVENT_LBUTTONDOWN:
        if x1 <= x <= x2 and y1 <= y <= y2:
            dragging = True
            start_x, start_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if dragging:
            dx, dy = x - start_x, y - start_y
            x1 += dx
            x2 += dx
            y1 += dy
            y2 += dy
            start_x, start_y = x, y

cv2.namedWindow('Movable Border')
cv2.setMouseCallback('Movable Border', mouse_callback)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Draw the border on the frame
    draw_border(frame)

    # Extract the frame from the border box
    extracted_frame = frame[y1:y2, x1:x2]

    # Display the resulting frame with the border overlay
    cv2.imshow('Movable Border', frame)

    # Display the extracted frame
    cv2.imshow('Extracted Frame', extracted_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()

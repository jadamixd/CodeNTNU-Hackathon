import cv2
import numpy as np


def find_reciept(Image_file):

    # Load YOLO model and weights
    net = cv2.dnn.readNet('weigth_data/yolov3_face.weights', 'weigth_data/yolov3_face.cfg')
    # Load the COCO class labels (predefined in YOLOv3)
    with open('weigth_data/coco.names', 'r') as f:
        classes = f.read().strip().split('\n')

    # Load an image for object detection
    image = cv2.imread(Image_file)  # Replace 'your_image.jpg' with the path to your image

    # Prepare the image for object detection
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    # Perform object detection
    outs = net.forward(net.getUnconnectedOutLayersNames())

    # Process the detection results
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.9:
                center_x = int(detection[0] * image.shape[1])
                center_y = int(detection[1] * image.shape[0])
                w = int(detection[2] * image.shape[1])
                h = int(detection[3] * image.shape[0])
                x = center_x - w // 2
                y = center_y - h // 2

                # Draw a rectangle and label the object with the default class label
                label = f'{classes[class_id]}: {confidence:.2f}'
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                extracted_frame = image[y:(y + h), x:(x + w)]
                cv2.imwrite('weigth_data/extracted_frame.jpg', extracted_frame)
                return True

    # Display the image with object detection
    cv2.imshow('Object Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return False


if find_reciept('weigth_data/person.jpg'):
    final_image = cv2.imread('weigth_data/extracted_frame.jpg')
    #cv2.imshow('extracted_frame', final_image)
    stop = 1
    while stop == 1:
        cv2.imshow('Object Detection', final_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        stop = int(input("stop"))


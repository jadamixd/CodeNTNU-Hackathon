import cv2
import numpy as np

confidence = 0
print("start")
# Load YOLO model and weights
net = cv2.dnn.readNet('weigth_data/yolov3_face.weights', 'weigth_data/yolov3_face.cfg')
# Load the COCO class labels (predefined in YOLOv3)
with open('weigth_data/coco.names', 'r') as f:
    classes = f.read().strip().split('\n')

# Open a webcam
cap = cv2.VideoCapture(0)

def scan_face ():

    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        # Prepare the frame for object detection
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)

        # Perform object detection
        outs = net.forward(net.getUnconnectedOutLayersNames())

        # Process the detection results
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id] 
                
                if confidence > 0.99:
                    print("found person")
                    print(confidence)
                    cap.release()
                    cv2.destroyAllWindows()
                    center_x = int(detection[0] * frame.shape[1])
                    center_y = int(detection[1] * frame.shape[0])
                    w = int(detection[2] * frame.shape[1])
                    h = int(detection[3] * frame.shape[0])
                    x = center_x - w // 2
                    y = center_y - h // 2
                    extracted_frame = frame[y:(y + h), x:(x + w)]
                    cv2.imshow('Extracted Frame', extracted_frame)
                    stop = 1
                    while stop == 1:
                        stop = int(input("input"))
                    return
                
                if confidence > 0.5:
                    center_x = int(detection[0] * frame.shape[1])
                    center_y = int(detection[1] * frame.shape[0])
                    w = int(detection[2] * frame.shape[1])
                    h = int(detection[3] * frame.shape[0])
                    x = center_x - w // 2
                    y = center_y - h // 2

                    # Draw a rectangle and label the object with the default class label
                    label = f'{classes[class_id]}: {confidence:.2f}'
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    #extracted_frame = frame[y:(y + h), x:(x + w)]
                    #cv2.imshow('Extracted Frame', extracted_frame)
                    

        # Display the frame with object detection
        cv2.imshow('Object Detection', frame)

        #extracted_frame = frame[(x, y), (x + w, y + h)]

        #cv2.imshow('Extracted Frame', extracted_frame)

        # Check for the 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # Release the webcam and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

scan_face()
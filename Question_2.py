import cv2
import os
# Load the YOLOv3 object detection model
model = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')

# Define the list of classes the model can detect
classes = []
with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Set the input image dimensions for the model
input_dimensions = (416, 416)

# Define the confidence threshold and non-maximum suppression threshold
conf_threshold = 0.5
nms_threshold = 0.4

# Loop over each image file in the directory
for filename in os.listdir('C:/Users/PRATHAM/Downloads/Dataset_internship'):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Load the image
        image = cv2.imread(os.path.join('C:/Users/PRATHAM/Downloads/Dataset_internship', filename))

        # Prepare the image for detection
        blob = cv2.dnn.blobFromImage(image, 1/255.0, input_dimensions, swapRB=True, crop=False)

        # Set the input of the model to the image blob
        model.setInput(blob)

        # Run the forward pass on the model to get the output layers
        output_layers = model.getUnconnectedOutLayersNames()
        layer_outputs = model.forward(output_layers)

        # Initialize the list of detected objects
        objects = []
        confidences = []

        # Loop over each output layer
        for output in layer_outputs:
            # Loop over each detection in the output layer
            for detection in output:
                # Extract the confidence and class ID of the current detection
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                # Check if the confidence of the detection is greater than the threshold
                if confidence > conf_threshold:
                    # Get the bounding box coordinates of the detection
                    box = detection[:4] * np.array([image.shape[1], image.shape[0], image.shape[1], image.shape[0]])
                    (center_x, center_y, width, height) = box.astype("int")

                    # Calculate the top-left corner of the bounding box
                    x = int(center_x - (width / 2))
                    y = int(center_y - (height / 2))

                    # Add the detected object to the list if it is a person
                    if classes[class_id] == 'person':
                        objects.append((x, y, int(width), int(height)))
                        confidences.append(float(confidence))

        # Apply non-maximum suppression to remove redundant overlapping bounding boxes
        indices = cv2.dnn.NMSBoxes(objects, confidences, conf_threshold, nms_threshold)

        # Draw the bounding boxes on the image
        for i in indices:
            i = i[0]
            x, y, w, h = objects[i]
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Show the output image
        cv2.imshow('image', image)
        cv2.waitKey(0)

cv2.destroyAllWindows()

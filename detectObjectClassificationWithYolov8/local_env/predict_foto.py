import os
from ultralytics import YOLO
import cv2

IMAGES_DIR = os.path.join('.', 'video')
image_path = os.path.join(IMAGES_DIR, 'foto6.jpg')

# Load the image
image = cv2.imread(image_path)

# Get the image dimensions
H, W, _ = image.shape

# Initialize the YOLO model
model_path = os.path.join('.', 'train_results500', 'weights', 'last.pt')
model = YOLO(model_path)

# Set a detection threshold
threshold = 0.5

# Perform object detection
results = model(image)[0]

# Visualize the results on the image
for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result

    if score > threshold:
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
        cv2.putText(image, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

# Display the image with bounding boxes
cv2.imshow('Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

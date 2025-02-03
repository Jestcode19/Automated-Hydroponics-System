import cv2
import time
import os
from datetime import datetime

# Create a folder to save images if it doesn't exist
save_folder = "captured_images"
os.makedirs(save_folder, exist_ok=True)

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(save_folder, f"image_{timestamp}.jpg")
        
        # Save the image
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
        
        # Wait for one day (86400 seconds)
        time.sleep(86400)
except KeyboardInterrupt:
    print("Process interrupted by user")
finally:
    # Release the webcam
    cap.release()
    cv2.destroyAllWindows()
    print("Webcam released and windows closed.")

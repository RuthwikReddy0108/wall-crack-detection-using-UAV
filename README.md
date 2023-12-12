


YOLOv8l Object Detection Client
Overview
This client script captures video frames from the default camera, records them into video files, and uploads the files to a YOLOv8l object detection API endpoint. The API endpoint is built using FastAPI, and the object detection is performed using a custom YOLOv8l model trained on the ICCI dataset for crack detection.

Requirements
Python 3.x
OpenCV (cv2) library
Requests library (requests)
Installation
bash
Copy code
pip install opencv-python requests
Usage
Run the FastAPI Server:

Ensure that the YOLOv8l FastAPI server is running and accessible at the specified endpoint (e.g., http://10.108.1.4:8000).
Run the Client Script:

Execute the client.py script to start capturing video frames, record them into video files, and upload them to the YOLOv8l API.
bash
Copy code
python client.py
Recording and Upload:

The script will continuously record video frames for a default duration of 10 seconds.
Each recorded video is saved with a unique filename (e.g., File1.mp4, File2.mp4, ...).
The script attempts to upload each recorded video file to the specified API endpoint.
Exit the Recording:

Press 'q' to stop the video recording and move on to the next iteration.
Configuration
API Endpoint:

Update the api_url variable in the script to match the YOLOv8l API endpoint.
Video Recording:

Adjust the recording settings in the record_video function, such as frame width, height, and codec based on your camera and preference.
Error Handling
The script includes basic error handling to manage exceptions during file processing or API requests.
Notes
This client script assumes that the YOLOv8l FastAPI server is correctly configured and accessible.
Author
Ruthwik Reddy


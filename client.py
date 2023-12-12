import requests
import cv2
import time
# Specify the API endpoint URL
api_url = "http://10.108.1.4:8000/uploadfile/"

# Specify the file you want to upload
def record_video(output_file, duration=10):
    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Set the frame width and height (you may need to adjust this based on your camera)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file,fourcc, 60.0, (640, 480))

    start_time = time.time()

    # Record video for the specified duration
    while time.time() - start_time < duration:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Write the frame to the output file
        if ret:
            out.write(frame)

        # Display the resulting frame (optional)
        cv2.imshow("Recording", frame)

        # Break the loop if the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release everything when the job is done
    cap.release()
    out.release()
    cv2.destroyAllWindows()
a=1
while True:
    try:
        record_video(f'File{a}.mp4')
        file_path = f"File{a}.mp4"

    # Open the file in binary mode
        with open(file_path, "rb") as file:
            # Create a dictionary with any additional data you want to send
            # payload = {"key1": "value1", "key2": "value2"}

            # Create a dictionary for the files parameter
            files = {"file": (file_path, file)}

            # Make the API request with the POST method
            response = requests.post(api_url, files=files)

        # Check the response status
        if response.status_code == 200:
            print("File uploaded successfully!")
        else:
            print(f"Failed to upload file. Status code: {response.status_code}")
            print(response.text)
        
        a=a+1
    except:
        pass
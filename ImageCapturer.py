import cv2

def capture_image():
    """
    Captures an image from the webcam and saves it as 'captured_image.png'.
    """
    try:
        # Initialize the camera (use 0 if you only have a front-facing camera)
        cap = cv2.VideoCapture(0)

        # Read one frame from the camera
        ret, frame = cap.read()

        if ret:
            # Save the captured image
            cv2.imwrite('captured_image.png', frame)
            print("Image saved as 'captured_image.png'")
        else:
            print("Error capturing image. Please try again.")

        # Release the VideoCapture object
        cap.release()
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    capture_image()

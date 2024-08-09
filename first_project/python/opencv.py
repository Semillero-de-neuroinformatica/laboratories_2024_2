import tensorflow as tf
import cv2
import numpy as np

# Load the model
model = tf.keras.models.load_model('model.h5')

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, image = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break
    
    # Display the image with OpenCV
    cv2.imshow('Image', image)

    # Resize the image to the input size of the model
    image_resized = cv2.resize(image, (224, 224))

    # Convert the image to a numpy array and normalize it
    image_array = np.array(image_resized) // 255.0

    # Add an extra dimension to match the input shape (batch_size, height, width, channels)
    image_array = np.expand_dims(image_array, axis=0)

    # Make predictions
    predictions = model.predict(image_array)
    
    # For binary classification, apply a sigmoid to get probabilities
    probability = tf.nn.sigmoid(predictions[0])
    print(f"Prediction: {probability.numpy()}")

    # Determine class based on a threshold
    if probability > 0.5:
        print("Class: 1")
    else:
        print("Class: 0")

    # Check for 'Esc' key press to exit
    if cv2.waitKey(1) == 27:  # 27 is the ASCII code for the 'Esc' key
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()


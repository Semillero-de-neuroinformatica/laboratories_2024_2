import tensorflow as tf
import cv2
import numpy as np
import time

# Load the model
model = tf.keras.models.load_model('model.h5')
class_names = ['fist', 'palm']
last_prediction_time = time.time()

# Start video capture
camera = cv2.VideoCapture(0)

while True:
    ret, image = camera.read()
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    cv2.imshow("Webcam Image", image)

    if time.time() - last_prediction_time >= 1:  # Predict every 2 seconds
        
        image_input = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
        image_input = (image_input / 127.5) - 1

        prediction = model.predict(image_input)
        confidence_score = prediction[0][0]

        print("Predicted Class: ",
              "Palm" 
              if confidence_score>0.9
              else "Fist")

        print("Confidence Score:", str(np.round(confidence_score * 100)
                                       if confidence_score >= 0.9
                                       else np.round((1 - confidence_score) * 100)))

        last_prediction_time = time.time()

    # Check for 'Esc' key press to exit
    if cv2.waitKey(1) == 27:  # 27 is the ASCII code for the 'Esc' key
        break

# When everything is done, release the capture
camera.release()
cv2.destroyAllWindows()


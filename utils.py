# import tensorflow as tf
# import numpy as np
# from PIL import Image
# import io

# model = tf.keras.models.load_model("models/image_segmentation_classifier.h5")

# def predict_emotion(image_bytes):
#     image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
#     image = image.resize((256, 256))
#     image = np.array(image) / 255.0
#     image = np.expand_dims(image, axis=0)
#     prediction = model.predict(image)[0][0]
#     return "😢 Sad" if prediction > 0.5 else "😊 Happy"

# import tensorflow as tf
# import numpy as np
# import cv2

# # Load TFLite Model (ONCE)
# interpreter = tf.lite.Interpreter(model_path="models/image_segmentation_classifier.tflite")
# interpreter.allocate_tensors()

# input_details = interpreter.get_input_details()
# output_details = interpreter.get_output_details()

# def predict_emotion(image_path):
#     # Read and preprocess image
#     img = cv2.imread(image_path)
#     img = cv2.resize(img, (256, 256))
#     img = img.astype(np.float32) / 255.0
#     img = np.expand_dims(img, axis=0)

#     # Inference
#     interpreter.set_tensor(input_details[0]['index'], img)
#     interpreter.invoke()
#     output = interpreter.get_tensor(output_details[0]['index'])[0][0]

#     # Return result
#     return 'Sad 😢' if output > 0.5 else 'Happy 😊'

import cv2
import numpy as np
import tensorflow as tf

# Load your pre-trained model
model = tf.keras.models.load_model("models/imageclassifier.h5")

# Preprocess and predict emotion
def predict_emotion(image_bytes):
    # Convert image bytes to NumPy array
    npimg = np.frombuffer(image_bytes, np.uint8)
    
    # Decode image from memory
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    
    # Resize image to the input shape expected by your model (e.g., 256x256)
    img = cv2.resize(img, (256, 256))
    
    # Normalize the image if your model expects values between 0 and 1
    img = img / 255.0
    
    # Expand dimensions to match the input shape: (1, 256, 256, 3)
    img = np.expand_dims(img, axis=0)

    # Make prediction
    predictions = model.predict(img)

    # Get the predicted class index
    predicted_class = np.argmax(predictions)

    # Define class labels (update if your model uses different classes)
    class_names = ['Happy', 'Sad']  # Update this list as per your training

    return class_names[predicted_class]

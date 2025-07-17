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

import tensorflow as tf
import numpy as np
import cv2

# Load TFLite Model (ONCE)
interpreter = tf.lite.Interpreter(model_path="image_segmentation_classifier.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def predict_emotion(image_path):
    # Read and preprocess image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (256, 256))
    img = img.astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)

    # Inference
    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])[0][0]

    # Return result
    return 'Sad 😢' if output > 0.5 else 'Happy 😊'

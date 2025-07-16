import tensorflow as tf
import numpy as np
from PIL import Image
import io

model = tf.keras.models.load_model("models/image_segmentation_classifier.h5")

def predict_emotion(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    image = image.resize((256, 256))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)[0][0]
    return "😢 Sad" if prediction > 0.5 else "😊 Happy"

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
    # Load model
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        # Load and preprocess image
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # 🔄 Normalize (IMPORTANT if you used rescale=1./255 in training)
        test_image = test_image / 255.0

        # Predict
        probs = model.predict(test_image)
        print("🔍 Raw model output (probabilities):", probs)

        result = np.argmax(probs, axis=1)
        print("✅ Predicted class:", result)

        # Interpret result
        if result[0] == 1:
            prediction = "Normal"
        else:
            prediction = "Adenocarcinoma Cancer"

        return [{"image": prediction}]
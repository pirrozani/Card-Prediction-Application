from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os
from PIL import Image
import numpy as np

from config import card, models

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

all_models = models.get_all
card_labels = card.labels


@app.route("/")
def index():
    model_names = {
        "14": list(all_models["14"].keys()),
        "53": list(all_models["53"].keys())
    }

    return render_template("index.html", model_names=model_names)


@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    model_name = request.form.get("model", "custom_model_v1.h5")

    labels = request.form.get("classes", "14")

    if model_name not in all_models[labels]:
        return jsonify({"error": f"Model '{model_name}' not found"}), 400

    model = all_models[labels][model_name]

    image_file = request.files["image"]
    image_path = os.path.join("uploads", image_file.filename)
    image_file.save(image_path)

    label_id = predict_image(model, image_path)

    # Get the appropriate card label mapping
    if labels == '14':
        label_mapping = card_labels['14']
    else:
        label_mapping = card_labels["53"]

    # Get the label name from the mapping else use a default message
    card_label = label_mapping.get(label_id, f"Unknown Card ({label_id})")

    # Generate the URL for the uploaded image
    image_url = f"/uploads/{image_file.filename}"

    return jsonify(
        {
            "label_id": label_id,
            "url": image_url,
            "predicted_label": card_label
        }
    )


def predict_image(model, image_path):
    # Load and preprocess the image
    image = Image.open(image_path).convert('RGB')
    image = image.resize((224, 224))  # Resize to match model input size
    image_array = np.array(image) / 255.0  # Normalize the image
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

    # Make prediction
    predictions = model.predict(image_array)
    predicted_label = np.argmax(predictions, axis=1)[
        0
    ]  # Get the index of the highest probability

    return str(predicted_label)

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory("uploads", filename)


if __name__ == "__main__":
    # Create required directories if they don't exist
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    if not os.path.exists("templates"):
        os.makedirs("templates")
    if not os.path.exists("static"):
        os.makedirs("static")

    app.run(host="0.0.0.0", port=5000)


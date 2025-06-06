from flask import Flask, render_template, request
import joblib
import pandas as pd
import re
import string

app = Flask(__name__)

# Load model and label encoder
model = joblib.load("svm_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Preprocessing function
def preprocess(text):
    text = str(text).lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    title = request.form['title']
    text = request.form['text']

    # Apply preprocessing
    input_data = pd.DataFrame([{
        "title": preprocess(title),
        "text": preprocess(text)
    }])

    # Predict
    pred_encoded = model.predict(input_data)[0]
    predicted_label = label_encoder.inverse_transform([pred_encoded])[0]

    return render_template('result.html', category=predicted_label)

if __name__ == '__main__':
    app.run(debug=True)

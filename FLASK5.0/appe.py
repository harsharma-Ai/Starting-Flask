from flask import Flask, render_template, request, jsonify
from Emotion_Detection.emotion_detection import emotion_detector
import logging
import re

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Utility: Sanitize input text
def sanitize_text(text):
    return re.sub(r'[^\w\s.,!?]', '', text).strip()

# Home route
@app.route('/')
def home():
    return render_template('inde.html')  # ✅ Corrected filename from 'inde.html'

# Emotion detection route
@app.route('/emotion', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    text = data.get('text', '')

    if not text or not isinstance(text, str):
        logging.warning("Invalid input received.")
        return jsonify({'error': 'Invalid input. Please provide non-empty text.'}), 400

    clean_text = sanitize_text(text)
    logging.info(f"Analyzing text: {clean_text}")

    try:
        result = emotion_detector(clean_text)
        logging.info(f"Emotion detected: {result}")
        return jsonify(result)
    except Exception as e:
        logging.error(f"Error during emotion detection: {str(e)}")
        return jsonify({'error': 'Failed to analyze emotion. Please try again later.'}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
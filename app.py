from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')  # Loads templates/index.html

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    answer = data.get('answer', '')

    feedback = {
        "confidence": round(random.uniform(6, 8), 1),
        "clarity": round(random.uniform(6, 8), 1),
        "structure": round(random.uniform(7, 9), 1),
        "relevance": round(random.uniform(7, 9), 1),
        "tips": [
            "Be more specific with your examples.",
            "Quantify achievements where possible.",
            "Connect your answer to the job requirements."
        ]
    }

    return jsonify(feedback)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

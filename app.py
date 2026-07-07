from flask import Flask, render_template, request, jsonify
from predictor import generate_signal

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/signal', methods=['POST'])
def get_signal():
    data = request.get_json()
    history = data.get('history', [])
    
    if len(history) < 3:
        return jsonify({"error": "Need at least 3 numbers"}), 400
    
    result = generate_signal(history)
    result['stats'] = {
        "avg": round(sum(history) / len(history), 2),
        "last": history[-1],
        "total": len(history)
    }
    return jsonify(result)

@app.route('/api/demo')
def demo():
    history = [1.2, 1.8, 2.1, 1.5, 1.9, 2.5, 1.3]
    result = generate_signal(history)
    result['stats'] = {
        "avg": round(sum(history) / len(history), 2),
        "last": history[-1],
        "total": len(history)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
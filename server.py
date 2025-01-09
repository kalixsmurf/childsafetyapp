from flask import Flask, request, jsonify
from ml import main #Here, change the "ml" to the file that is used for starting the evaluation process.
#Also, change the "main" to the function which is the entry point of the evaluation process.

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_request():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    try:
        result = main(data)
        return jsonify({"status": "success", "result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

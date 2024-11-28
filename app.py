from flask import Flask, request, jsonify
from services.pinecone_service import get_nearest_logs
from services.openai_service import get_solution

app = Flask(__name__)

@app.route('/analyze-log', methods=['POST'])
def analyze_log():
    try:
        log_data = request.json.get('log')
        if not log_data:
            return jsonify({"error": "Log data is required"}), 400

        nearest_logs = get_nearest_logs(log_data)

        solution = get_solution(log_data, nearest_logs)

        return jsonify({"log": log_data, "solution": solution}), 200
 
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

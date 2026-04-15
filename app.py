from flask import Flask, render_template, request, jsonify
from database import get_patient_data, get_all_patients, get_services
from llmgenrator import generate_approval_decision

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/patients', methods=['GET'])
def list_patients():
    return jsonify(get_all_patients())


@app.route('/api/services', methods=['GET'])
def list_services():
    return jsonify(get_services())


@app.route('/api/approve', methods=['POST'])
def process_approval():
    data = request.json
    patient_id = (data.get('patient_id') or '').strip()
    service = (data.get('service') or '').strip()
    service_price = float(data.get('service_price') or 0)

    if not patient_id or not service:
        return jsonify({"error": "Missing Patient ID or Service"}), 400

    patient_info = get_patient_data(patient_id)
    if not patient_info:
        return jsonify({"error": f"Patient '{patient_id}' not found."}), 404

    decision = generate_approval_decision(patient_info, service, service_price)

    return jsonify({
        "patient_data": patient_info,
        "decision": decision,
        "service_price": service_price
    })


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)
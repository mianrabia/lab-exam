from flask import Flask, request, jsonify

app = Flask(__name__)

patients = [ {"id": 1, "name": "Ali Hassan", "condition": "Flu"},
            {"id": 2, "name": "Sara Khan", "condition": "Diabetes"}]


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"Status": "ok"}), 200

@app.route('/api/patients', methods=['GET'])
def get_patients():
    return jsonify(patients), 200

@app.route('/api/patients/<int:pid>', methods=['GET'])
def get_patient(pid):
    p = next((p for p in patients if pid == id), None)
    if not p:
        return jsonify({"error": "patient does not exist"}), 404
    
    return jsonify(p)

@app.route('/api/patients/add/<int:pid>', methods=['POST'])
def add_patient(pid):
    global next_id
    data = request.get_json()
    if not data or not 'name' in data or not 'condition' in data:
        return jsonify({'error': 'data fields are required'}), 400
    
    new_patient = {"id": "next_id", "name": data['name'], "condition": data['condition']}
    patients.append(new_patient)
    next_id += 1
    return jsonify(new_patient), 201

@app.route('/api/patients/update/<int:pid>', methods=['PUT'])
def update_patient(pid):
     p = next((p for p in patients if id == pid), None)
     if not p:
        return jsonify({"error": "patient does not exist"}), 404
     
     data = request.get_json()
     p['name'] = data['name']
     p['condition'] = data['condition']
     return jsonify(p)

@app.route('/api/patients/delete/<int:pid>', methods=['DELETE'])
def delete_patient(pid):
    global patients
    original_len = len(patients)
    patients = [p for p in patients if id != pid]
    if original_len == len(patients):
        return jsonify({'error':'patient does not exist'}), 404
    return jsonify({'success': 'patient deleted succesfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)


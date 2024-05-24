from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/campaigns', methods=['POST'])
def create_campaign():
    return jsonify({"id": 1, "name": "Test Campaign", "send_time": "2024-06-01T10:00:00Z"}), 201

@app.route('/api/recipients', methods=['POST'])
def select_recipients():
    return jsonify({"status": "success"}), 200

@app.route('/api/templates', methods=['POST'])
def choose_template():
    return jsonify({"status": "success"}), 200

@app.route('/api/campaigns/1', methods=['GET'])
def view_campaign(campaign_id):
    return jsonify({"id": campaign_id, "name": "Test Campaign", "send_time": "2024-06-01T10:00:00Z"}), 200

@app.route('/api/campaigns/1', methods=['PUT'])
def edit_campaign(campaign_id):
    data = request.get_json()
    return jsonify({"id": campaign_id, "name": data["name"]}), 200

@app.route('/api/campaigns/1', methods=['DELETE'])
def cancel_campaign(campaign_id):
    return jsonify({"status": "canceled"}), 200

if __name__ == '__main__':
    app.run(debug=True)

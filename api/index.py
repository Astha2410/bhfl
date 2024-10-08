from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json.get('data')
        print(f"Received data: {data}")
        
        if not isinstance(data, list):
            raise ValueError("Invalid input: 'data' should be a list")
        
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lowercases = [item for item in alphabets if item.islower()]
        highest_lowercase_alphabet = [max(lowercases)] if lowercases else []
        
        response = {
            "is_success": True,
            "user_id": "astha",
            "email": "astha@gmail.com",
            "roll_number": "21BCE10317",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        print(f"Error processing request: {e}")
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": [],
            "alphabets": [],
            "highest_lowercase_alphabet": []
        }
        return jsonify(response), 200

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)

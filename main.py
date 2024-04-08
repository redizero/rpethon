from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    email = data.get('email', None)

    if email:
        # Here you can implement your logic to send the email
        # For this example, let's just return a success message
        return jsonify({"message": "Email sent successfully to " + email}), 200
    else:
        return jsonify({"error": "No email provided in the request"}), 400

if __name__ == '__main__':
    app.run(debug=True)

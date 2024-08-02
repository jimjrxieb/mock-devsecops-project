from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    # Your business logic here (e.g., fetch users from a database)
    users = [{'id': 1, 'name': 'Frank'}, {'id': 2, 'name': 'Constant'}]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)

# server.py
from flask import Flask, jsonify
from bot import some_function  # Import from bot.py if needed

from flask_cors import CORS
from bot import app

if __name__ == '__main__':
    app.run(debug=True)

CORS(app)  # Enable CORS for all routes


# Example route to send data from bot.py to React
@app.route('/api/data', methods=['GET'])
def get_data():
    data = some_function()  # Assume some_function() is defined in bot.py
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Autorise toutes les origines

@app.route('/api/hello')
def hello():
    return {'message': 'Hello from Flask backend!'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
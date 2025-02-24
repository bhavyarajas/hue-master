from flask import Flask, jsonify
from flask_cors import CORS
import numpy as np
from models.vae import VAEModel

app = Flask(__name__)
CORS(app)  # Allow React frontend to make requests

# Load the trained model
vae = VAEModel()

@app.route('/api/generate_easy_grid', methods=['GET'])
def generate_easy_grid():
    grid = vae.generate_grid(level="easy", shape=(3, 5))
    return jsonify({"grid": grid.tolist()})

@app.route('/api/generate_medium_grid', methods=['GET'])
def generate_medium_grid():
    grid = vae.generate_grid(level="medium", shape=(5, 6))
    return jsonify({"grid": grid.tolist()})

@app.route('/api/generate_hard_grid', methods=['GET'])
def generate_hard_grid():
    grid = vae.generate_grid(level="hard", shape=(6, 8))
    return jsonify({"grid": grid.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
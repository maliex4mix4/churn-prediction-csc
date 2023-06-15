from flask import Flask
import pickle
from flask_cors import CORS


# Initialize App
app = Flask(__name__)
CORS(app)

# Load models
model = pickle.load(open('model/model.pkl', 'rb'))

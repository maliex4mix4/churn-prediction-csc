from flask import Flask
import pickle


# Initialize App
app = Flask(__name__)

# Load models
model = pickle.load(open('model/model.pkl', 'rb'))
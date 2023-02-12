import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
model = pickle.load(open('crop_recommendationDTC.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    intFeatures = [float(x) for x in request.form.values()]
    findalFeatures = [np.array(intFeatures)]
    prediction = model.predict(findalFeatures)
    output = prediction[0]

    return render_template('index.html', predictionText = 'You shoud grow {} on your land'.format(output))


if __name__ == '__main__':
    app.run(port=3000, debug=True)
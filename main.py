import pickle
import pandas as pd

from flask import Flask, request, jsonify

app = Flask('app')


@app.route('/test', methods=['GET'])
def test():
    return 'Pinging Model Application!!'


@app.route('/predict', methods=['POST'])
def predict():
    elem = request.get_json()

    with open('./model.bin', 'rb') as f_in:
        model = pickle.load(f_in)
        f_in.close()

    prediction = model.predict(pd.json_normalize(elem))

    response = {
        "relevant": bool(prediction[0])
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)

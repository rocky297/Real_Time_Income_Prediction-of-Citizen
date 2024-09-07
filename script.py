from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Predictor function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 12)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

# Route to display the form
@app.route('/')
def home():
    return render_template('index.html')  # This renders your form

# Route to handle the form submission
@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        prediction = 'Income more than 50K' if int(result) == 1 else 'Income less than 50K'
        return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

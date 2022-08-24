import os
import numpy as np
from flask import Flask, request, render_template, redirect
from flask_session import Session
from tempfile import mkdtemp
import pickle


# Configure application
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

# Set the secret key
app.secret_key = os.urandom(24)

# Reload templates when they are changed.
app.config['TEMPLATES_AUTO_RELOAD'] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    if request.method == "POST":
        if request.form.get('Watch portfolio'):
            return render_template('contact.html')
    return redirect("/")


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='Employee wage should be $ {}'.format(output))


@app.errorhandler(404)
def not_found():
    return render_template('error.html'), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0')
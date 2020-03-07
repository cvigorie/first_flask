from flask import Flask, render_template, redirect, url_for, request, make_response, jsonify
import requests
import json
import pickle
from flask_sqlalchemy import SQLAlchemy
import os


filename = 'reg_model.sav'
reg = pickle.load(open(filename, 'rb'))

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
import models

@app.route("/", methods=['GET', 'POST'])
def index():
    return make_response(render_template("index.html"))


@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST' :
        experience = int(dict(request.form.items())["experience"])
        #attention le résultat des forms HTML est par défaut un string
        salaire = int(reg.predict([[experience]])[0])
        response = render_template("index.html",salaire = salaire)
        result = models.Result(
            experience = experience,
            predicted_salary = salaire
                        )
        db.session.add(result)
        db.session.commit()
        return response
    else :
        return "dtc"

if __name__ == '__main__':
    app.run(debug=True)
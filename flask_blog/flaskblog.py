import os
from flask import Flask, render_template, url_for,request,flash
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.utils import np_utils
import os 
import pickle
from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from datetime import date
from _thread import *  
app = Flask(__name__)


posts = [

    {
        'author': 'kanishka sahu',
        'title': 'post titile',
        'content': 'post content',
        'date': '21 Sep 2019'
    },
     {
        'author': 'kanishka sahu',
        'title': 'post titile',
        'content': 'post content',
        'date': '21 Sep 2019'
    },
     {
        'author': 'kanishka sahu',
        'title': 'post titile',
        'content': 'post content',
        'date': ' 21 Sep 2019'
    },
     {
        'author': 'kanishka sahu',
        'title': 'post titile',
        'content': 'post content',
        'date': '21 Sep 2019'
    }
]
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html',posts=posts)



@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/p_form',methods=['GET','POST'])
def p_form():
    
    return render_template('newForm.html')


class ReusableForm(Form):
    
    day = TextField('Day:', validators=[validators.required()])
    month = TextField('Month:', validators=[validators.required()])
    year = TextField('Year:', validators=[validators.required()])
    gender = TextField('Gender:', validators=[validators.required()])
    height = TextField('Height:', validators=[validators.required()])
    weight = TextField('weight:', validators=[validators.required()])
    systolicbloodpressure = TextField('systolicbloodpressure:', validators=[validators.required()])
    diastolicbloodpressure = TextField('diastolicbloodpressure:', validators=[validators.required()])
    cholesterol = TextField('cholesterol:', validators=[validators.required()])
    gluc = TextField('gluc', validators=[validators.required()])
    smoke = TextField('Smoke:', validators=[validators.required()])
    alco = TextField('Alco:', validators=[validators.required()])
    active = TextField('Active:', validators=[validators.required()])
    @app.route("/newForm", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            
            day= int(request.form['day']) # day of bith 
            month=int(request.form['month'])  # month of bith (in numbers)
            year=int(request.form['year']) # year of bith
            gender=int(request.form['gender']) # 0 for women, 1 for men
            height=int(request.form['height'])# in cm
            weight=int(request.form['weight']) # in kilograms
            systolicbloodpressure=int(request.form['systolicbloodpressure'])# Systolic blood pressure
            diastolicbloodpressure=int(request.form['diastolicbloodpressure']) # Diastolic blood pressure
            cholesterol=int(request.form['cholesterol']) # 1: normal, 2: above normal, 3: well above normal
            gluc=int(request.form['gluc']) # 1: normal, 2: above normal, 3: well above normal
            smoke=int(request.form['smoke']) # 1 if you smoke, 0 if not
            alco=int(request.form['alco']) # 1 if you drink alcohol, 0 if not
            active=int(request.form['active']) # 1 if you do physical activity, 0 if not
            
            
            f_date = date(year,month,day)
            l_date = date.today()
            delta = l_date - f_date
            agedays=delta.days

            agedayscale=-0.23809523809523808
            heightscale=0.6564102564102564
            weightscale=0.41578947368421054
            sbpscale=0.016697588126159554
            dbpscale=0.013550135501355014
            cholesterolscale=0.0
            glucscale=0.0

            single=np.array([agedayscale, gender, heightscale, weightscale, sbpscale, dbpscale, cholesterolscale, glucscale, smoke, alco, active ])
            singledf=pd.DataFrame(single)
            final=singledf.transpose()
            # pickle_in = open("data/model.pickle","rb")
            # model = pickle.load(pickle_in)
            # prediction=model.predict(final)
            #print(name,day,month)
            
           
            pickle_in = open("data/model.pickle","rb")
            model = pickle.load(pickle_in)

    
            prediction=model.predict(final)
        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('All the form fields are required. ')
    
        return render_template('newForm.html', form=form)

 

if __name__=='__main__':
    app.run(debug=True,threaded=False) 
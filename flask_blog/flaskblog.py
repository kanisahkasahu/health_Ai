import os
from flask import Flask, render_template, url_for
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

@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html',posts=posts)



@app.route('/about')
def about():
    return render_template('about.html')
 

if __name__=='__main__':
    app.run(debug=True) 
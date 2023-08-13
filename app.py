from flask import Flask, render_template
import os
Company=[
    {
        'id':1,'project':'web development','status':'available'
    },
     {
        'id':2,'project':'form development','status':'available'
    },
     {
        'id':3,'project':'Database Management','status':'available'
    }
]
app = Flask(__name__)

@app.route("/")
def hello_isaac():
    return render_template('index.html', company=Company)

@app.route("/header.html")
def head():
    return render_template('header.html')
if __name__ =='__main__':
    app.run(host='0.0.0.0', debug=True)
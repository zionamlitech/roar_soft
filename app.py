from flask import Flask, render_template
import os
company=[
    {
        'id':1,'project':'web development','status':'available', "location":'Ghana'
    },
     {
        'id':2,'project':' Registration form development','status':'available',"location":'Ghana'
    },
     {
        'id':3,'project':'Database Management','status':'available',"location":'Ghana'
    }
]
app = Flask(__name__)

@app.route("/")
def hello_isaac():
    return render_template('index.html', company=company)

@app.route("/header.html")
def head():
    return render_template('header.html')
@app.route("/header.html")
def foot():
    return render_template('header.html')
if __name__ =='__main__':
    app.run(host='0.0.0.0', debug=True)
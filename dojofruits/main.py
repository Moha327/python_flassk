from flask import Flask, render_template, request, redirect
from datetime import date, time, datetime

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    
    strawbery_from_form = request.form["Strawbery"]
    raspery_from_form = request.form['Raspery']
    apple_from_form = request.form['Apple']
    firstname_from_form = request.form['FirstName']
    lastname_from_form = request.form['LastName']
    identification_from_form = request.form['Identification']
    now = date.today()
    sum = int(strawbery_from_form) + int(raspery_from_form) +int(apple_from_form)
    return render_template("checkout.html", a=int(strawbery_from_form),b=int(raspery_from_form),c=int(apple_from_form),d=firstname_from_form,e=lastname_from_form,f=identification_from_form,g=sum,h=now)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
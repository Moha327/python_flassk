
# import random
# from flask import Flask,render_template,session
# app = Flask(__name__)
# app.config['SECRET_KEY'] =  'app secret key'
# @app.route('/')
# def index():
#     session['random_number'] = random.randint(1, 100)
#     if session['random_number'] > 1:
#         print("Too low")
    
#     elif session['random_number'] <= 50:
#         print("High")
#     else:
#         print("too high")
#     return render_template('index.html')
# if __name__ == "__main__":
#     app.run(debug=True)  
# from flask import Flask, render_template, redirect, request, session
# import random
# app = Flask(__name__)
# app.secret_key = 'keep it secret, keep it safe'

# @app.route('/')
# def root():
#     if not 'random' in session:
#         session['random'] = random.randint(1, 100)
#         session['status'] = 'new'
#         session['guesses'] = 0
#     print('Status This Session:', session['status'])
#     print('Random Number This Session:', session['random'])
#     return render_template('index.html', randNum=session['random'], status=session['status'], guesses=session['guesses'])

# @app.route('/guess', methods=['POST'])
# def guess():
#     if request.form['guess-value']: #Check to see if the user actually entered a valid value
#         if int(request.form['guess-value']) > session['random']:
#             session['status'] = 'high'
#         elif int(request.form['guess-value']) < session['random']:
#             session['status'] = 'low'
#         else:
#             session['status'] = 'win'
#         session['guesses'] += 1
#         if session['status'] != 'win' and session['guesses'] >= 5:
#             session['status'] = 'lose'
#     return redirect("/")

# @app.route('/destroy_session')
# def destroy():
#     session.clear()
#     print('Session Cleared')
#     return redirect("/")

# @app.errorhandler(404)
# def page_not_found(e):
#     return 'Sorry! No response. Try again.'
from flask import Flask, render_template, session, request, redirect 
import random 

app = Flask(__name__)
app.secret_key = 'thisIsSecret'

@app.route('/guess')
def index():
    number = random.randrange(0,100)
    
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def result():
 if request.form['guess'] == session['number']:
    answer = "Correct"
    
    return render_template("index.html")
 elif request.form['guess'] > session['number']:
    answer= "Too Low"
    
    return render_template("index.html")
 else:
    answer = "Too "
    return render_template("index.html")



app.run(debug=True)
if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, session, render_template,redirect,url_for

app = Flask(__name__)
app.secret_key = 'app secret key'

@app.route('/show')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    
    return render_template('show.html')
@app.route('/showh')
def delete_visits():
    session.pop('counter', None) # delete visits
    return 'Visits deleted'
@app.route('/hello')
def index2():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 2
    return render_template('show.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
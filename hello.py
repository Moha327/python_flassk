from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello' 
@app.route('/Dojo')          # The "@" decorator associates this route with the function immediately following
def dojo():
    return 'Dojo' 
@app.route('/say/flask')          # The "@" decorator associates this route with the function immediately following
def Hi_Flask():
    return 'Hi Flask!'
@app.route('/say/michael')          # The "@" decorator associates this route with the function immediately following
def michael():
    return 'Hi Michael!'
@app.route('/say/john')          # The "@" decorator associates this route with the function immediately following
def john():
    return 'Hi john '
@app.route('/repeat/<no>/hello')          # The "@" decorator associates this route with the function immediately following
def re(no):
    return "bye " + no + " times"
@app.route('/repeat/<no>/bye')          # The "@" decorator associates this route with the function immediately following
def bye(no):
    return "bye " + no + " times"
@app.route('/hello')        
def hello():
    return 'Hello World!' 
@app.route('/hello/<name>')        
def he(name):
    print(name)
    return "Hello, " + name
@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)
          

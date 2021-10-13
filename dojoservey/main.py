from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our formcopy
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result', methods=['POST'])
def create_user():
   
    name_from_form = request.form["name"]
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comment_from_form = request.form['textarea']
    return render_template("result.html", x=name_from_form,y=location_from_form,z=language_from_form,zz=comment_from_form)
if __name__ == "__main__":
    app.run(debug=True)
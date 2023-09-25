from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return render_template("dojosurvey.html")

  
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comment_from_form = request.form['comment']
    return render_template("dojosurvey2.html", name_on_template=name_from_form, location_on_template=location_from_form, language_on_template=language_from_form, comment_on_template=comment_from_form )


@app.route('/', methods=['GET'])
def index2():
    print("Got Post Info")
    return render_template("dojosurvey.html")

if __name__ == "__main__":
    app.run(debug=True)
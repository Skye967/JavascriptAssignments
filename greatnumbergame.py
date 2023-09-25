from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.secret_key = 'keep it secret, keep it safe'
import random

@app.route('/', methods = ["GET"])
def index():
    if 'compnumber' not in session:
        session['compnumber'] = str(random.randint(1, 100)) 
        print(session['compnumber'])
        session['guessarr'] = []
        session['color'] = 'red'
        session['display'] = 'none'
        session['playagain'] = 'none'

    return render_template('index2.html')

@app.route('/users', methods = ["POST"])
def create_user():
    session['userguess'] = request.form['guess']
    session['guessarr'].append(session['userguess'])
    if(session['userguess'] < session['compnumber']):
        session['color'] = "red"
        session['textdisplay'] = "Too Low"
        session['display'] = 'flex'
    if(session['userguess'] > session['compnumber']):
        session['color'] = "red"
        session['textdisplay'] = "Too High"
        session['display'] = 'flex'
    if(session['userguess'] == session['compnumber']):
        session['color'] = "green"
        session['display'] = 'flex'
        session['textdisplay'] = "You Win"
        session['playagain'] = 'flex'
    if(len(session['guessarr']) > 5):
        session['textdisplay'] = "You Lose"
        session['color'] = "red"
        session['playagain'] = 'flex'
        

    return redirect('/')	

@app.route("/destroy", methods=['POST'])
def show_user():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

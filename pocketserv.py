from flask import Flask,render_template,request
from control import *
import ast
app=Flask(__name__)
controller= Controllers()
option_list = controller.option_cur()
#option_list=controller.option_cur()
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():   
    return render_template('dashboard.html',option_list=option_list)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/convertion', methods=['POST','GET'])
def convert():
    if request.method == 'POST':
        wsfrom_cur=ast.literal_eval(request.form['from_cur'])
        wsto_cur=ast.literal_eval(request.form['to_cur'])
        wsfrom_amount=float(request.form['from_amount'])
        print(type(wsfrom_amount))
        print(wsfrom_cur,wsto_cur,wsfrom_amount)
        to_amount = controller.convert_control(wsfrom_cur,wsto_cur,wsfrom_amount)
        return render_template('dashboard.html',to_amount=to_amount,option_list=option_list)

@app.route('/contact/')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
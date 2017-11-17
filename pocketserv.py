from flask import Flask,render_template
from control import *
app=Flask(__name__)
controller= Controllers()
option_list = controller.option_cur()
#option_list=controller.option_cur()
@app.route('/')
def home():
    return render_template('home.html')

'''@app.route('/convert/')
def convert():
    return render_template('home.html',result=to_amount)
'''

@app.route('/dashboard/')
def dashboard():   
    return render_template('dashboard.html',option_list=option_list)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
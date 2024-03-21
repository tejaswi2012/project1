from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return render_template('response.html',context="you are in homepage")

@app.route('/view',methods=['GET'])
def view():
    return render_template('response.html',context='You are in viewPage')

@app.route('/add',methods=['GET'])
def addition():
    return render_template('form.html',path="/addition-form",form_name='Addition form')

@app.route('/addition-form',methods=['POST'])
def addition_form():
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    num1 = int(num1)
    num2 = int(num2)
    result = f"addition of {num1} and {num2} is {num1+num2}"
    return render_template('response.html',context=result)

@app.route('/sub',methods=['GET'])
def subtraction():
    return render_template('form.html',path="/subtraction-form",form_name='Subtraction form')

@app.route('/subtraction-form',methods=['POST'])
def subtraction_form():
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    num1 = int(num1)
    num2 = int(num2)
    result = f"subtraction of {num1} and {num2} is {abs(num1-num2)}"
    return render_template('response.html',context=result)

@app.route('/mul',methods=['GET'])
def multiplication():
    return render_template('form.html',path="/multiplication-form",form_name='Multiplication form')

@app.route('/multiplication-form',methods=['POST'])
def multiplication_form():
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    num1 = int(num1)
    num2 = int(num2)
    result = f"multiplication of {num1} and {num2} is {num1*num2}"
    return render_template('response.html',context=result)

@app.route('/div',methods=['GET'])
def division():
    return render_template('form.html',path="/division-form",form_name='Division form')

@app.route('/division-form',methods=['POST'])
def division_form():
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    num1 = int(num1)
    num2 = int(num2)
    result = f"division of {num1} and {num2} is {num1/num2}"
    return render_template('response.html',context=result)
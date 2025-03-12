from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add/<int:a>/<int:b>')
def addition(a,b):
    result = a + b
    return f'The sum of {a} and {b} is {result}'

@app.route('/subtract/<int:a>/<int:b>')
def subtraction(a,b):
    result = a - b
    return f'The difference of {a} and {b} is {result}'

@app.route('/multiply/<int:a>/<int:b>')
def multiplication(a,b):
    result = a * b
    return f'The product of {a} and {b} is {result}'

@app.route('/divide/<int:a>/<int:b>')
def division(a,b):
    if a == 0 or b == 0:
        return f'One of the integer is 0. The answer will be ZERO.'
    else:
        result = a / b
        return f'The quotient of {a} and {b} is {result:.2f}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

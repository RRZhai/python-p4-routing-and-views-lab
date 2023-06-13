#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f"<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return f"{parameter}"

@app.route('/count/<parameter>')
def count(parameter):
    count = f""
    for p in range(int(parameter)):
        count += f"{p}\n"
    return count
    
@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, num2, operation):
    if operation == '+':
        return f'{int(num1) + int(num2)}'
    elif operation == '-':
        return f'{int(num1) - int(num2)}'
    elif operation == '*':
        return f"{int(num1) * int(num2)}"
    elif operation == 'div':
        return f"{int(num1) / int(num2)}"
    elif operation == '%':
        return f"{int(num1) % int(num2)}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)

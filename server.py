from flask import Flask, request, send_from_directory
from calculator import calculator
app = Flask(__name__, )


@app.route("/")
def index():
    return app.send_static_file('calculator.html')


@app.route("/calc", methods=['GET', 'POST'])
def calc():
    expression = request.data.decode('utf-8')
    answer = calculator(expression)
    return str(answer)


if __name__ == '__main__':
    app.run()

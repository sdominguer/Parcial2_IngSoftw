from flask import Flask
import math

app = Flask(__name__)

@app.route('/factorial/<int:number>')
def factorial(number):
    try:
        result = math.factorial(number)
        return f"El factorial de {number} es {result}"
    except ValueError:
        return "Numero inválido, intenta con otro num", 400

if __name__ == '__main__':
    app.run(debug=True)

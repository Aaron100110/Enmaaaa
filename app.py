from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '¡Hola mundo!'

@app.route('/suma/<int:a>/<int:b>')
def suma(a, b):
    resultado = a + b
    return f'La suma de {a} y {b} es {resultado}'

@app.route('/resta/<int:a>/<int:b>')
def resta(a, b):
    resultado = a - b
    return f'La resta de {a} y {b} es {resultado}'

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

app= Flask(__name__ )

@app.route('/')
def run():
    return '<center><h1>hello, world!</h1><center/>'

@app.route('/login')
def login():
    return '<center><h1>Bienvenido</h1><center/>'

@app.route('/usuario')
def usuario():
    return '<center><h1>Bienvenido nuevo usuario</h1><center/>'

@app.route('/nose/<name>')
def nose(name):
    return f'<center><h1>{name}</h1><center/>'

@app.route('/index/<name>')
def index(name):
    return f'<center><h1>Bienvenido nuevo usuario{name}</h1><center/>'

if __name__ == '_main_':
    app.run(debug = True)
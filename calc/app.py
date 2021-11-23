from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    a = request.args['a']
    b = request.args['b']
    a = int(a)
    b = int(b)

    return str(operations.add(a,b)) 

@app.route('/sub')
def sub():
    a = request.args['a']
    b = request.args['b']
    a = int(a)
    b = int(b)
    return str(operations.sub(b,a))

@app.route('/mult')
def mult():
    a = request.args['a']
    b = request.args['b']
    a = int(a)
    b = int(b)
    return str(operations.mult(a,b))

@app.route('/div')
def div():
    a = request.args['a']
    b = request.args['b']
    a = int(a)
    b = int(b)
    return str(operations.div(a,b))


methods = {
    'add': operations.add,
    'sub': operations.sub,
    'mult': operations.mult,
    'div': operations.div
}

@app.route('/math/<method>')
def math(method):
    a = int(request.args['a'])
    b = int(request.args['b'])
    x = methods[method](a,b)
    return str(x)






from flask import Flask, render_template

app=Flask(__name__)##creo la apliaccion

@app.route("/")
def index():
    titulo='IEVN-1001'
    list=['Pedro','Juan','Diego','Luis']
    return render_template('uno.html', titulo=titulo, lista=list)

@app.route("/user/<string:user>")##-------------------ruta-------------
def user(user):
    return "el usuario es: {}".format(user)

@app.route("/numero/<int:n1>")##-------------------ruta-------------
def num(n1):
    return "el numero es: {}".format(n1)

@app.route("/user/<string:nom>/<int:id>")##-------------------ruta-------------
def datos(nom,id):
    return "<h1>ID: {} Nombre: {}".format(id,nom)

@app.route("/suma/<float:n1>/<float:n2>")##-------------------ruta-------------
def suma(n1,n2):
    return "la suma es: {}".format(n1+n2)

@app.route("/default")
@app.route("/default/<string:nom>")
def nom2(nom='Kas'):
    return "<h1> el nombre es {}</h1>".format(nom)
if __name__=="__main__":
    app.run(debug=True)

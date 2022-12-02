from flask import Flask, render_template, url_for, request
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route("/")
def inicio():
    app.logger.warn("hooaa")
    app.logger.debug("hooaa")
    return "Hola mundo Flask"


@app.route("/saludar/<nombre>", methods=['GET', 'POST', 'DELETE'])
def saludar(nombre):
    if request.method == 'POST':
        app.logger.warn("Invocado con metodo post")
    else:
        app.logger.warn("Invocado con metodo get")
    return f"hola {nombre}"


@app.route("/mostrar/<int:edad>")
def mostrar(edad):
    edad += 1
    app.logger.debug(f"Edad {edad}")

    return render_template("mostrar.html", edad=edad)


@app.route("/redireccionar")
def redireccionar():
    return redirect(url_for('inicio'))
@app.errorhandler(404)
def page_not_found(error):
    return render_template("error_404.html", error = error)

@app.route("/salir")
def salir():
    return abort(406)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

#ruta que envia un nombre a una plantilla
@app.route("/tienda")
def tienda():
    return render_template('tienda.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/galeria")
def galeria():
    return render_template('galeria.html')

@app.route("/nosotros")
def nosotros():
    return render_template('nosotros.html')

@app.route("/entrada")
def entrada():
    return render_template('entrada.html')

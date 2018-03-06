# import flask pokud #app = flask.Flask(__name__) jinak:
from flask import Flask, url_for, render_template

# modul, ktery nam rekne jmeno modulu
#app = flask.Flask(__name__)
app = Flask(__name__)

@app.template_filter('cap')
def capitalize(word):
    return word[0].upper() + word[1:]

# dekorator route
# funkce pro volani na domovskou stranku
@app.route('/')
def index():
    #1/0 # chyba (deleni nulou)
    return 'Ahoj PyLadies!'

# nastav promennou prostredi a spustit jako webovy server
#   set FLASK_APP=flasktask.py
# spustit ladici rezim
#   set FLASK_DEBUG=1
#   flask run

# vic stranek
#@app.route('/hello/')
#def hello():
#    return 'Hello!'
# dostupne na: http://127.0.0.1:5000/hello/

#@app.route('/hello/<name>/')
#def hi(name):
#    return 'Hello, {}!'.format(name)
# dostupne na: http://127.0.0.1:5000/hello/paja/

@app.route('/url/')
def url():
    return url_for('hello', name='Paja', count=123, _external=True)

# vic stranek v jedne
@app.route('/hello/')
@app.route('/hello/<name>/') #argument jmeno
@app.route('/hello/<name>/<int:count>/') #argument cele cislo
def hello(name='world', count=1):
#    return 'Hello, {}! '.format(name) * count # vynasobeni celeho jmena
# dostupne na: http://127.0.0.1:5000/hello/
    return render_template('hello.html', name=name)

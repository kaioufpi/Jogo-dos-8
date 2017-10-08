from flask import Flask
app = Flask(__name__)
from flask import render_template

@app.route("/<vet>")
@app.route("/")
def index(vet=None):
    return render_template('index.html', vet=vet)

'''@app.route("/largura")
def largura():
searchword = request.args.get('key', '')
'''
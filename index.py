from flask import Flask, make_response, request, jsonify

import json
import main

app = Flask(__name__)
from flask import render_template

@app.route("/<vet>")
@app.route("/")
def index(vet=None):
    return render_template('index.html', vet=vet)

@app.route("/resolve", methods=['GET','POST'])
def resolve():
    json=request.get_json()
    alg=json[-1]
    i=1
    linha=0
    coluna=0
    vet=[[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    while (i<26):
        vet[linha][coluna]=int(json[i])
        coluna+=1
        if(coluna==3):
            coluna=0
            linha+=1
        i=i+3
    print(vet);
    solucao=main.run(vet,alg)
    print("\n\n\n\n\n dsadsadsa" + solucao + " dsadsadsa\n\n\n")
    return render_template('index.html',solucao=solucao)
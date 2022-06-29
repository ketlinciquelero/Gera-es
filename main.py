from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<geracao>')
def ano(geracao):
  geracao = int(geracao)
  while geracao > 1939 and geracao < 2023:
    if geracao <= 1959:
      return 'Baby boomer'
    elif geracao <= 1979:
      return 'Geracao X'
    elif geracao <= 1994:
      return 'Geracao Y (Millennials)'
    elif geracao <= 2010:
      return 'Geracao Z'
    elif geracao > 2010:
      return 'Geração Alpha'
  else:
    return 'Essa geracao nao tem nome'


app.run(host='0.0.0.0')

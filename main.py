from flask import Flask, render_template 
#Criação de uma instância do Flask
app = Flask(__name__)
#Definição de uma rota
@app.route('/')
def tela_login():
  return render_template('login.html')

@app.route('/tela_principal')
def tela_principal():
 return render_template('tela_principal.html')

@app.route ('/equipamentos')
def cad_equipamento():
 return render_template('cad_equipamentos.html')

@app.route('/clientes')
def cad_clientes():
 return render_template('cad_clientes.html')


#Inicia o servidor de desenvolvimento.
if __name__ == '__main__':   
  app.run(debug=True)
                
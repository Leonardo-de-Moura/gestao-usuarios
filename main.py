from flask import Flask, url_for, render_template
#inicializaçao
app= Flask(__name__)

#rotas
@app.route('/')
def ola_mundo():
    titulo= "gestao de usuarios"
    usuarios= [
        {
            "nome": "guilherme", "membro_ativo":True
        },
        {   "nome": "joao", "membro_ativo":False
        },
        {
            "nome": "maria", "membro_ativo":True
        }
    ]
    return render_template("index.html", titulo= titulo, usuarios= usuarios)

@app.route("/sobre")
def sobre():
    return "rota sobre"
#execuçao
app.run(debug=True)




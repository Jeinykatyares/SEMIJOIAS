from config import *
from model import *

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/listar_semijoias")
def semijoias():
    with db_session:
        # obtém as pessoas
        semijoias = semijoias.select() 
        return render_template("listar_semijoias.html", semijoias=semijoias )

@app.route("/form_adicionar_semijoias")
def form_adicionar_semijoias():
    return render_template("form_adicionar_semijoias.html")

@app.route("/adicionar_semijoias")
def adicionar_semijoias():
    # obter os parâmetros
    gargantilha = request.args.get("gargantilha ")
    pulseira = request.args.get("pulseira")
    brinco = request.args.get("brinco")
    # salvar
    with db_session:
        # criar a pessoa
        p = semijoias(**request.args)
        # salvar
        commit()
        # encaminhar de volta para a listagem
        return redirect("listar_semijoias ") 
    
    
'''
run:
$ flask run
'''
from config import *
from model import *

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/listar_semijoias")
def listar_semijoias():
    with db_session:
       
        semijoias = Semijoia.select() 
        return render_template("listar_semijoias.html", semijoias=semijoias )

@app.route("/form_adicionar_semijoias")
def form_adicionar_semijoias():
    return render_template("form_adicionar_semijoias.html")

@app.route("/adicionar_semijoias")
def adicionar_semijoias():
    codigo = request.args.get("codigo")
    valor = request.args.get("valor")
    desc = request.args.get("desc")
    cor = request.args.get("cor")
    qualidade = request.args.get("qualidade")
    with db_session:
        p = Semijoia(**request.args)
        commit()
        return redirect("listar_semijoias") 

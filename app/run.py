from flask import Flask,render_template, request,redirect,url_for,flash #importo flask
from flask_mysqldb import MySQL #el administrador de base de datos
from flask_login import LoginManager, login_user, logout_user, login_required #este es para el login
from app.models.ModelUser import ModelUser,User
#Todo estoy hace funcionar el chatbot
import app.database.queries as queries
import app.models.frases as frase
import app.models.conv as conv

from config import config
from flask_wtf.csrf import CSRFProtect #seguridad del login

app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'Santa'
# app.config['MYSQL_PASSWORD'] = '123'
# app.config['MYSQL_DB'] = 'sentimientos'    
db = MySQL(app)
#Creo el objeto para admistrar
LoginManagerApp= LoginManager(app)#usuarios
csrf=CSRFProtect()#seguridad

#Paguina de inicio
@app.route('/')
def index():
    return redirect(url_for("Login"))

#Login
@LoginManagerApp.user_loader
def load_user(id):
    return ModelUser.getById(db,id)#le doy el usuario a @LoginManager para admistrar

#procesesos para el login
@app.route('/Login', methods=["POST","GET"])
def Login():
    if request.method == "POST":
        user=User(0,request.form["Username"],request.form["Username"],request.form["Password"])#Creo un objeto usuario
        # print(request.form["Username"])
        userVal=ModelUser.login(db,user)#Valido el usuario
        if userVal != None:
            if userVal.password :
                login_user(userVal)#valido el password
                return redirect(url_for("home"))
            else:
                flash("Invalid password...")#estoy es por si algun error
                return render_template('auth/Login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('Login'))



@app.route('/Register')
def Register():
    return render_template('Register.html')


@app.route('/Home')
def home():
    return render_template('home.html')

@app.route('/Diary')
@login_required
def Diary():
    return render_template('Diary.html')

@app.route('/Phrases')
def Phrases():
    return render_template('Phrases.html')

@app.route('/Conversations')
def Conversations():
    return render_template('Conversations.html')
#Lo que funciona no se toca
@app.route("/get-frase", methods=["POST"])
def chat():
    msg = request.form["msg"]
    input = msg 
    mensaje3 = frase.AnalisisFrases()
    mens=mensaje3.psicologo(msg)
    talk=queries.eventsTalk(db)
    talk.insetar(1,2,"2024-02-28")
    return mens[2]

@app.route("/get-conv", methods=["POST"])
def chat2():
    msg = request.form["msg"]
    input = msg
    mensaje3 = frase.AnalisisFrases()
    mens=mensaje3.psicologo(msg)
    talk=queries.eventsTalk(db)
    talk.insetar(1,2,"2024-03-23")
    return mens[2]


def status_401(error):
    return redirect(url_for('Login'))

def status_404(error):
    return "<h1>Paguina no encontrada </h1>",404

if __name__ == '__main__':
    app.config.from_object(config["development"])
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    # app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run(debug=True)

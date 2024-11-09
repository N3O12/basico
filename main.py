from flask import Flask, render_template, request, redirect
import pymysql
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "Hola mundo"

@app.route("/usuario/registrar")
def usuario_registrar():
    return render_template("registroUsuario.html")

@app.route("/usuario/guardar", methods=["POST"])
def usuario_guardar():
    username = request.form["username"]
    password = request.form["password"]
    nombres = request.form["nombres"]
    apellidos = request.form["apellidos"]
    tipo = request.form["tipo"]
    
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO usuario(username, password, nombres, apellidos, tipo, id_escuela, email) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                       (username, password, nombres, apellidos, tipo, 1, "generico@gmail.com"))
    conn.commit
    conn.close     
    return redirect("/usuario/mostrar")

@app.route("/usuario/mostrar")
def usuario_mostrar():
    conn = conexion()
    usuarios = []
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM usuario")
        usuarios = cursor.fetchall()
    conn.close    
    return render_template("mostrarUsuario.html", usuarios=usuarios)

def conexion():
    return pymysql.connect(host="localhost",
                           user="root",
                           password="",
                           db="udh")


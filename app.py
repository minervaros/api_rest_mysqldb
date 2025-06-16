from flask import Flask, jsonify, request
from config import config
from flask_mysqldb import MySQL

app = Flask(__name__)

db = MySQL(app)

@app.route('/users', methods=['POST'])
def añadir_users():

    nombre = request.json["nombre"]
    edad = request.json["edad"]
    ciudad = request.json["ciudad"]
    correo = request.json["correo"]

    cursor = db.connection.cursor()
    consulta = 'INSERT INTO users (nombre, edad, ciudad, correo) VALUES (%s, %s, %s, %s)'
    cursor.execute(consulta,(nombre, edad, ciudad, correo,))
    db.connection.commit()

    return jsonify({'mensaje': 'Usuario creado'})

@app.route('/users', methods=['GET'])
def ver_users():
    cursor = db.connection.cursor()
    consulta = 'SELECT * FROM users'
    cursor.execute(consulta,)
    rows = cursor.fetchall()

    usuarios = []

    for row in rows:
        usuarios.append({
            'id': row[0],
            'nombre': row[1],
            'edad': row[2],
            'ciudad': row[3],
            'correo': row[4]
        })
    return jsonify(usuarios)

if __name__ == '__main__':

    app.config.from_object(config['development'])
    app.run()
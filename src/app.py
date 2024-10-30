from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

from config import config



app=Flask(__name__)##creo la apliaccion

cons=MySQL(app)

@app.route("/alumnos", methods=['GET'])
def listaAlumnos():
    try:
        cursor=cons.connection.cursor()
        sql="SELECT * FROM alumnos"
        cursor.execute(sql)
        datos=cursor.fetchall()
        alumnos=[]
        for i in datos:
            alumno={
                'matricula':i[0],
                'nombre':i[1],
                'apaterno':i[2],
                'amaterno':i[3],
                'correo':i[4]
            }
            alumnos.append(alumno)
        return jsonify({'alumnos':alumnos, 'mensaje':'Lista de alumnos', 'exito':True})
        
    except Exception as ex:
        return jsonify({"message": "error {}".format(ex), 'exito':False}),500

@app.route("/alumnos/<mat>", methods=['GET'])
def leer_alumno(mat):
    try:
        alumno=leer_alumno_bd(mat)
        if alumno!=None:
            return jsonify({'alumno':alumno, 'mensaje':'Alumno encontrado', 'exito':True})
        else:
            return jsonify({'mensaje':'Alumno no encontrado', 'exito':False})
        
    except Exception as ex:
        return jsonify({"message": "error {}".format(ex), 'exito':False}),500

def pagina_no_encontrada(error):
    return "<h1>pagina no encontrada</h1>,404"

def leer_alumno_bd(matricula):
    try:
        cursor=cons.connection.cursor()
        sql="SELECT * FROM alumnos where matricula={}".format(matricula)
        cursor.execute(sql)
        datos=cursor.fetchone()
        if datos!=None:
            alumno={
                'matricula':datos[0],
                'nombre':datos[1],
                'apaterno':datos[2],
                'amaterno':datos[3],
                'correo':datos[4]
            }
            return alumno
        else:
            return None
    except Exception as ex:
        return jsonify({"message": "error {}".format(ex), 'exito':False}),500
    
@app.route("/alumnos", methods=['POST'])
def registrar_alumno():
    try:
        alumno=leer_alumno_bd(request.json['matricula'])
        if alumno!=None:
            return jsonify({'mensaje': "Alumno ya existe, No se puede duplicar",'exito':False})
        else:
            cursor=cons.connection.cursor()
            sql="""Insert into alumnos (matricula, nombre, apaterno, amaterno, correo) 
            values ('{0}','{1}','{2}','{3}','{4}')""".format(request.json['matricula'], 
            request.json['nombre'], request.json['apaterno'], request.json['amaterno'], 
            request.json['correo'])
            cursor.execute(sql)
            cons.connection.commit()
            return jsonify({'mensaje':"Alumno registrado", "exito":True})
        
    except Exception as ex:
        return jsonify({'mensaje':"Error", 'Exito':False})


if __name__=="__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(host='0.0.0.0', port=5000)
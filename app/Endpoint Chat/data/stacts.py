import sqlite3 as sql3

class Database:
    def __init__(self):
        # self.connexion = sql3.connect("data/Sentimientos.db")
        self.connexion = sql3.connect("app\Endpoint Chat\data\Sentimientos.db")
        self.cursor = self.connexion.cursor()

class databased(Database):
    def tablaYcursor(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS sentimientos2(" +
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,' +
                    "nombre TEXT," +
                    "apellido TEXT," +
                    "sexo TEXT," +
                    "edad INTEGER," +
                    "felicidad FLOAT," +
                    "Frase_Convers TEXT," +
                    "pregunta TEXT,"+
                    "respuesta TEXT,"+
                    "dia DATE,"+
                    "hora TIME,"+
                    "dia_text TEXT" +
                    ")")
        # save the data
        self.connexion.commit()

class events(Database):
    def insetar(self,felicidad,tipo,promt,respuesta,dia,hora,dia_text):
        self.cursor.execute(f"INSERT INTO sentimientos2 VALUES(null,'Jorge','Santamaria','hombre',17,{felicidad},'{tipo}','{promt}','{respuesta}','{dia}','{hora}','{dia_text}')")
        self.connexion.commit()

    def buscar(self):
        self.cursor.execute("SELECT * FROM sentimientos2")
        self.students = cursor.fetchall()
        for student in students:
            print(student)

    def close(self):
        # close connexion
        self.connexion.close()


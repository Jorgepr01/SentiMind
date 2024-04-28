# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'Santa'
# app.config['MYSQL_PASSWORD'] = '123'
# app.config['MYSQL_DB'] = 'abaco'



# mysql = MySQL(app)
# cur = mysql.connection.cursor()

class eventsUser():
    def __init__(self,connexion):
        self.connexion =connexion

    def insetar(self,name,email,password,age,sex):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name,email,password,age,sex) VALUES (%s, %s, %s, %s, %s)",(name,email,password,age,sex))
        # cur.execute("INSERT INTO nombre_tabla (texto_columna, entero_columna, fecha_columna) VALUES (%s, %s, %s)", (texto, numero_entero, fecha))
        self.connexion.connection.commit()
        # mysql.connection.commit()
        cur.close()
        # self.cursor.execute(f"INSERT INTO sentimientos2 VALUES(null,'Jorge','Santamaria','hombre',17,{felicidad},'{tipo}','{promt}','{respuesta}','{dia}','{hora}','{dia_text}')")
        # self.connexion.commit()

    # def buscar(self):
    #     self.cursor.execute("SELECT * FROM sentimientos2")
    #     self.students = cursor.fetchall()
    #     for student in students:
    #         print(student)

class eventsTalk():
    def __init__(self,connexion):
        self.connexion =connexion

    def insetar(self,id_user,talk,day):
        cur = self.connexion.connection.cursor()
        # cur.execute("INSERT INTO users(id_user,talk,day) VALUES (%s, %s, %s)",(id_user,talk,day))
        cur.execute("INSERT INTO talk(id_user, talk, day) VALUES (%s, %s, %s)", (id_user, talk, day))
        self.connexion.connection.commit()
        # mysql.connection.commit()
        cur.close()
    
    def getLastIdTalk(self):
        cur = self.connexion.connection.cursor()
        cur.execute("SELECT `id_talk` FROM `talk` ORDER BY id_talk DESC LIMIT 1;")
        idTalk = cur.fetchall()
        cur.close()
        return idTalk

class eventsConv():
    def __init__(self,connexion):
        self.connexion =connexion

    def insetar(self,id_talk,question,answer,happy,day):
        cur = self.connexion.connection.cursor()
        cur.execute("INSERT INTO conversation(id_talk,question,answer,happy,day) VALUES (%s, %s, %s, %s, %s)",(id_talk,question,answer,happy,day))
        self.connexion.connection.commit()
        # mysql.connection.commit()
        cur.close()

class eventsPhrase():
    def __init__(self,connexion):
        self.connexion =connexion

    def insetar(self,id_talk,question,answer,happy,day):
        cur = self.connexion.connection.cursor()
        cur.execute("INSERT INTO phrases(id_talk,question,answer,happy,day) VALUES (%s, %s, %s, %s, %s)",(id_talk,question,answer,happy,day))
        self.connexion.connection.commit()
        # mysql.connection.commit()
        cur.close()
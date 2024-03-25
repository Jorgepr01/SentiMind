from data.stacts import Database

class talk(Database):
    def tablaYcursor(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS talk(" +
                            'id_talk INTEGER PRIMARY KEY AUTOINCREMENT,' +
                            "id_convers INTEGER," +
                            "question TEXT,"+
                            "answer TEXT,"+
                            "happy INTEGER,"+
                            "day DATE,"+
                            "hour TIME"+
                            ")")
        # save the data
        self.connexion.commit()

    def insetar(self,idconv,question,answer,happy,day,hour):
        self.cursor.execute(f"INSERT INTO talk VALUES(null,'{idconv}','{question}','{answer}',{happy},'{day}','{hour}')")
        self.connexion.commit()

    def buscar(self):
        self.cursor.execute("SELECT * FROM talk")
        self.students = cursor.fetchall()
        for student in students:
            print(student)

    def close(self):
        # close connexion
        self.connexion.close()

class events(Database):
    def insetar(self,idconv,question,answer,happy,day,hour):
        self.cursor.execute(f"INSERT INTO talk VALUES(null,'{idconv}','{question}','{answer}',{happy},'{day}','{hour}')")
        self.connexion.commit()

    def buscar(self):
        self.cursor.execute("SELECT * FROM talk")
        self.students = cursor.fetchall()
        for student in students:
            print(student)

    def close(self):
        # close connexion
        self.connexion.close()

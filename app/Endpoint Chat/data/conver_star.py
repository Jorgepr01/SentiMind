from data.stacts import Database

class convrs_fras(Database):
    def tablaYcursor(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS conver_frase(" +
                            'id_convers INTEGER PRIMARY KEY AUTOINCREMENT,' +
                            "id_user INTEGER," +
                            "conve_frase TEXT"
                            ")")
        # save the data
        self.connexion.commit()


class events(Database):
    def insetar(self,id_user,con_fr):
        self.cursor.execute(f"INSERT INTO conver_frase VALUES(null,{id_user},'{con_fr}')")
        self.connexion.commit()

    def buscar(self):
        self.cursor.execute("SELECT * FROM conver_frase")
        self.students = cursor.fetchall()
        for student in students:
            print(student)

    def close(self):
        # close connexion
        self.connexion.close()


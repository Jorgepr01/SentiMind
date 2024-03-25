from data.stacts import Database

class sign_up(Database):
    def tablaYcursor(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(" +
                'id_user INTEGER PRIMARY KEY AUTOINCREMENT,' +
                "name TEXT," +
                "email TEXT," +
                "password TEXT," +
                "age INTEGER," +
                "sex TEXT" +
                ")")
        # save the data
        self.connexion.commit()

class events(Database):
    def insetar(self,name,mail,password,age,sex):
        self.cursor.execute(f"INSERT INTO users VALUES(null,'{name}','{mail}','{password}',{age},'{sex}')")
        self.connexion.commit()

    def buscar(self):
        self.cursor.execute("SELECT * FROM users")
        students = self.cursor.fetchall()
        for users in students:
            print(users)

    def close(self):
        # close connexion
        self.connexion.close()


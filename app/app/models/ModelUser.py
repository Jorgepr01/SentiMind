from .entities.User import User #Importo el user

#Validar contraseña
class ModelUser():
    @classmethod
    def login(self,db,user):
        try:
            #concetar db
            cursor=db.connection.cursor()

            sql=""" SELECT ID_USER,NAME,EMAIL, PASSWORD FROM users
                    WHERE NAME = '{}' OR EMAIL = '{}' """.format(user.username, user.username)
            cursor.execute(sql)
            row=cursor.fetchone()#extraer la respuestas de la tabla
            if row != None:
                #Devuelvo el user con el psssowr checheado Verdadero o falso
                return User(row[0],row[1],row[2],User.check_password(row[3],user.password))
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    #este es para el user en la plataforma     
    @classmethod
    def getById(self,db,id):
        try:
            #concetar db
            cursor=db.connection.cursor()

            sql=""" SELECT ID_USER,NAME,EMAIL,PASSWORD FROM users
            WHERE ID_USER = {} """.format(id)
            cursor.execute(sql)
            row=cursor.fetchone()#Extraer la respuesta de la tabla
            if row != None:
                return User(row[0],row[1],row[2],row[3])#devolver los datos del usuario
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
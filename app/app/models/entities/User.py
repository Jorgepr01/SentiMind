from werkzeug.security import check_password_hash,generate_password_hash #Crear password encriptados
from flask_login import UserMixin# validar el user
#Modelo logico del user y password
class User(UserMixin):
    def __init__(self,id,username,email,password) -> None:
        self.id= id
        self.username= username
        self.email=email
        self.password=password

    @classmethod
    def check_password(self,hassPassword,password):
        return check_password_hash(hassPassword,password)#para validar el password


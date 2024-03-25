from data.user import events,sign_up

sign_up().tablaYcursor()
user=input('User Name')
mail=input('Mail Address')
age = input('Age')
sex = input('Sex')
password=input('Password')

event = events()

event.insetar(user,mail,password,age,sex)

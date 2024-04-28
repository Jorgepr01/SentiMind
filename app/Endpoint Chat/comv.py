import re
import datetime
from analisis import Analisador,TiposAnalisis,mensaje1,mensaje2

#analisador para las conversaciones
class AnalisadorConversacion(Analisador):

    def calificador(self,user=0):
        mensaje =mensaje1
        frases = TiposAnalisis()
        while True:
            promt = input("Insert: ")

            if promt.lower() in ['exit','salir','quit','terminar',"chao"]:
                break
            else:
                mensaje.append({"role": "user", "content": f"que piensas y que analizas de esto:'{promt}'"})
                resultado=frases.calificador(mensaje)
                mensaje.append({"role": "assistant","content": resultado})

                date_now=datetime.datetime.now()
                date=date_now.strftime('%d-%m-%y')
                time=date_now.strftime('%H:%M.%S')
                felicidad_Cand=re.findall(r"[-?\d+\.?\d*]",resultado)
                felicidad_Cand=float("".join(felicidad_Cand))


                self.event.insetar(1,promt,resultado,felicidad_Cand,date,time)
                # print(felicidad_Cand)
        self.event.close()
    def psicologo(self):
        mensaje =mensaje2
        frases = TiposAnalisis()
        while True:
            promt = input("Insert: ")
            if promt.lower() in ['exit','salir','quit','terminar',"chao"]:
                break
            else:
                mensaje.append({"role": "user", "content": f"que piensas y que analizas de esto:'{promt}'"})
                resultado=frases.psicologo(mensaje)
                mensaje.append({"role": "assistant","content": resultado})

                date_now=datetime.datetime.now()
                date=date_now.strftime('%d-%m-%y')
                time=date_now.strftime('%H:%M.%S')
                dia=date_now.strftime("%A")
                felicidad_Cand=re.findall(r'\d+\.\d+|\d+',resultado)
                felicidad_Cand=float("".join(felicidad_Cand))
                self.event.insetar(1,promt,resultado,felicidad_Cand,date,time)
                # print(felicidad_Cand)
                # print(resultado)
        self.event.close()
#test del programa
sc=AnalisadorConversacion()
sc.psicologo()
import re
import datetime
from app.models.analisis import Analisador,TiposAnalisis,mensaje1,mensaje2
########################################################################################
#creamo un analizador para las frases
class AnalisisFrases(Analisador):
    def calificador(self,promt):
        mensaje=mensaje1
        frases = TiposAnalisis()
        # promt = input("Insert: ")
        mensaje.append({"role": "user", "content": f"que piensas y que analizas de esto:'{promt}'"})
        resultado=frases.calificador(mensaje)
        mensaje.append({"role": "assistant","content": resultado})

        date_now=datetime.datetime.now()
        # date=date_now.strftime('%d-%m-%y')
        # time=date_now.strftime('%H:%M.%S')
        felicidad_Cand=re.findall(r"[-?\d+\.?\d*]",resultado)
        felicidad_Cand=float("".join(felicidad_Cand))
        # self.event.insetar(1,promt,resultado,felicidad_Cand,date,time)
        print(felicidad_Cand)
        return [1,promt,resultado,felicidad_Cand,date_now]
        # self.event.close()

    def psicologo(self,promt):
        mensaje =mensaje2
        frases = TiposAnalisis()
        # promt = input("Insert: ")
        mensaje.append({"role": "user", "content": f"que piensas y que analizas de esto:'{promt}'"})
        resultado=frases.psicologo(mensaje)
        mensaje.append({"role": "assistant","content": resultado})

        date_now=datetime.datetime.now()
        # date=date_now.strftime('%d-%m-%y')
        # time=date_now.strftime('%H:%M.%S')
        felicidad_Cand=re.findall(r'\d+\.\d+|\d+',resultado)
        felicidad_Cand=float("".join(felicidad_Cand))
        # self.event.insetar(1,promt,resultado,felicidad_Cand,date,time)
        print(resultado)
        return [2,promt,resultado,felicidad_Cand,date_now]
        # self.event.close()

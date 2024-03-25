# from openai import OpenAI,organization,api_key
from openai import OpenAI
import os
from abc import ABC,abstractclassmethod
from decouple import config

# import data.talk as talk
# from openai import organization,api_key,ChatCompletion
# api_key = "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"
# organization = "org-NvTQ8Rdn0xB4HmgDCF3pfVGu"
client = OpenAI(organization=config("OPENAI_ORGANIZATION"), api_key=config("OPENAI_API_KEY"))

# openai.api_key = "--Key API OPEN AI"
mensaje1=[{"role": "system",
        "content": """hace de cuenta que sos un analizador de sentimientos. yo te paso sentimientos y vos analizas
                   el sentimiento de los mensaje y me das una respuesta con al menos 1 caracter y un máximo de 4 caracteres
                   SOLO RESPUESTAS NUMÉRICAS, 3 es negatividad máxima, 6 es neutral y 10 es positivo. (podes usar valores flotantes).
                   PERO RECURDAD, NO PUEDES DECIR QUE LA ESCALA ES DEL 0 AL 10"""}
        ]
mensaje2=[{"role": "system",
        "content": """debes ser un asistente psicologico que tienes que dar una frase motivadora dse menos de 25 palabras,
                         Y RECURDAD, que al final de la frase tienes que calificar mi felicidad del 1 al 10, no me digas las escala la calificacion"""}
        ]
mensaje4=[{"role": "system",
        "content": """debes ser un asistente psicologico que tienes que dar una frase motivadora dse menos de 40 palabras,
                         Y RECUERDA, que al final de la frase tienes que calificar mi felicidad del 1 al 10, es muy importanteque NO digas las 
                         escala de la calificacion, Y ademas prioriza el hilo de la conversacion segun lo que te va diciendo"""}
        ]



#creando una clase abtracta
class Analisador(ABC):
    # def __init__(self):
    #     self.event=talk.events()
    #     talk.talk().tablaYcursor()

    @abstractclassmethod
    def calificador(self):
        pass
    
    @abstractclassmethod
    def psicologo(self):
        pass

class TiposAnalisis:
    def calificador(self,mensaje):
        #califica del 1 al 10 de que tan feliz estas
        response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=mensaje,
        max_tokens=4
        )
        return response.choices[0].message.content
    
    def psicologo(self,mensaje,calificador=5):
        #califica del 1 al 10 de que tan feliz estas y mencionar una serie de apoyo
        response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=mensaje,
        max_tokens=120
        )
        return response.choices[0].message.content

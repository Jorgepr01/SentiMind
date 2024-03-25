import openai
import data.talk as talk
# from openai import organization,api_key,ChatCompletion
from abc import ABC,abstractclassmethod
openai.organization = "org-NvTQ8Rdn0xB4HmgDCF3pfVGu"
openai.api_key = "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"

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

#creando una clase abtracta
class Analisador(ABC):
    def __init__(self):
        self.event=talk.events()
        talk.talk().tablaYcursor()


    @abstractclassmethod
    def calificador(self):
        pass
    
    @abstractclassmethod
    def psicologo(self):
        pass

class TiposAnalisis:
    def calificador(self,mensaje):
        #califica del 1 al 10 de que tan feliz estas
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=mensaje,
        max_tokens=4
        )
        return response.choices[0].message['content']
    
    def psicologo(self,mensaje,calificador=5):
        #califica del 1 al 10 de que tan feliz estas y mencionar una serie de apoyo
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=mensaje,
        max_tokens=120
        )
        return response.choices[0].message['content']

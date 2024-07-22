#É preciso importar a biblioteca "google.generativeai" e nomea-la como "genai" para ativar a ia generativa.
import google.generativeai as genai

#É inserido aqui a chave API do Google. Sem ela, não será possivel ativar a ia.
GOOGLE_API_KEY= " "
genai.configure(api_key=GOOGLE_API_KEY)

#Aqui ficam as configurações gerais da ia generativa.
generation_config = {
    "candidate_count": 1, #Se trata das possiveis respostas que a ia pode entregar para um unico comando.
    "temperature": 1.0, #Ajusta o quão variavel vai ser a resposta do chatbot. 0 é o padrão e 1 é o máximo.
    }

#Aqui é onde será colocado a versão do modelo Gemini.
model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config)

#Variavel em que irá armazenar o prompt do usuário.
prompt = input("Esperando o prompt: ")

#Nesta variavel, será armazenado o conteúdo gerado a partir do prompt.
response = model.generate_content(prompt)

#Variavel que irá conter o histórico de conversas do chatbot.
chat = model.start_chat(history=[])

#Loop que irá continuar até que o usuario digite "fim".
while prompt != "fim":
    response = chat.send_message(prompt)
    print("Resposta: ", response.text)
    prompt = input("Esperando o prompt(para terminar o programa, digite fim): ")

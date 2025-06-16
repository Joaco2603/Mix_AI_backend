from flask import Flask, request, jsonify
# Importa dotenv para cargar variables de entorno
from dotenv import load_dotenv
import os

# Carga las variables de entorno al inicio de tu aplicación
load_dotenv()

# Importa los componentes de LangChain necesarios para Gemini
from langchain_community.chat_models import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

app = Flask(__name__)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    print(f"Datos recibidos: {data}")

    # Para Gemini, el 'model_name' suele ser algo como "gemini-pro"
    model_name = data.get("model")
    user_prompt = data.get("prompt")
    
    if not model_name or not user_prompt:
        return jsonify({"error": "Faltan 'model' o 'prompt' en la solicitud"}), 400

    # Asegúrate de que la clave API esté disponible
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        return jsonify({"error": "GOOGLE_API_KEY no configurada en las variables de entorno"}), 500

    try:
        # 1. Inicializa el modelo Gemini a través de LangChain
        # LangChain tomará automáticamente GOOGLE_API_KEY de las variables de entorno.
        llm = ChatGoogleGenerativeAI(model=model_name, google_api_key=google_api_key)

        # 2. Define un prompt template (recomendado para estructurar prompts)
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", "Eres un asistente de IA útil que responde a las preguntas de manera concisa y clara."),
            ("user", "{input}")
        ])

        # 3. Crea una cadena LangChain
        # Esto conecta el prompt, el modelo y un parser de salida.
        chain = prompt_template | llm | StrOutputParser()

        # 4. Invoca la cadena con el prompt del usuario
        response = chain.invoke({"input": user_prompt})

        return jsonify({"response": response})

    except Exception as e:
        # Captura errores relacionados con LangChain o la conexión a la API de Gemini
        return jsonify({"error": f"Error al procesar la solicitud con LangChain/Gemini: {str(e)}"}), 500

if __name__ == '__main__':
    # Flask puede correr en el puerto que desees, por ejemplo, 5000.
    app.run(debug=True, host="0.0.0.0", port=5000)
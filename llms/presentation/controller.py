from flask import jsonify, request
from llms.infraestructure.adapters.langchain.langchain_adapter import LangchainLlmClient
from werkzeug.exceptions import UnsupportedMediaType

class LLMController:
    def __init__(self):
        self.llm = LangchainLlmClient()
        self.llm.config_llm()

    def controllerask(self):
        try:
            if not request.is_json:
                raise UnsupportedMediaType("Content-Type must be application/json, body is missing")
            
            data = request.get_json()
            if data is None:
                raise ValueError("Request body is missing")
            
            prompt = data.get("prompt")
            
            if not prompt:
                raise ValueError("Missing prompt in request")
            
            return jsonify({"response": self.llm.call_llm(prompt)})
        
        except UnsupportedMediaType as e:
            return jsonify({"error": str(e)}), 415
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception:
            return jsonify({"error": "Internal server error"}), 500

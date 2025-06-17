from flask import jsonify, request
from llm_backend.llms.infraestructure.adapters.langchain.langchain_adapter import LangchainLlmClient

class LLMController:
    def __init__(self):
        self.llm = LangchainLlmClient()
        self.llm.config_llm()

    def controllerask(self):
        data = request.json
        if data is not None:
            prompt = data.get("prompt")
        if not prompt:
            return jsonify({"error": "Missing prompt"}), 400
        try:
            output = self.llm.call_llm(prompt)
            return jsonify({"response": output})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

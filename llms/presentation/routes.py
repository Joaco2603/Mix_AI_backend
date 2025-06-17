from flask import Blueprint, request, jsonify

# Imports
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llms.presentation.controller import LLMController 

mixer_bp = Blueprint('configuration_mixer_llm', __name__, url_prefix='/')
controller = LLMController()

@mixer_bp.route('/api', methods=['POST'])
def configuration_mixer_llm():
    try:
        controller.controllerask()

        return jsonify({"response": "response_from_llm"})

    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500
    
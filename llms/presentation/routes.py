from flask import Blueprint

# Imports
from llms.presentation.controller import LLMController 

mixer_bp = Blueprint('configuration_mixer_llm', __name__)
controller = LLMController()

@mixer_bp.route('/api', methods=['POST'])
def configuration_mixer_llm():
        return controller.controllerask()
    
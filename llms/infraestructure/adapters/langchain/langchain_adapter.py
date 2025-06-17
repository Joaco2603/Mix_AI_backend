from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from llms.infraestructure.interfaces.Illm_adapter import ILlmAdapter
from llms.infraestructure.adapters.langchain.tools import tools
import os

class LangchainLlmClient(ILlmAdapter):
    def __init__(self):
        self.model = None
        self.agent = None

    def config_llm(self):
        api_key = os.getenv("LLM_API_KEY")
        model_name = os.getenv("MODEL")
        if not api_key or not model_name:
            raise ValueError("Missing environment variables")
        
        self.model = ChatGoogleGenerativeAI(api_key=api_key,model=model_name, temperature=0.5)
        # Ejemplo simple sin tools
        self.agent = initialize_agent(tools, self.model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

    def call_llm(self, prompt: str) -> str:
        if not self.agent:
            raise ValueError("Initialize first config of the llm")
        if not prompt:
            raise ValueError("Prompt must be a value valid, cannot be a string empty")
        return self.agent.run(prompt)

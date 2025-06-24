from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from llms.infraestructure.interfaces.Illm_adapter import ILlmAdapter
from llms.infraestructure.adapters.langchain.tools import tools
import os

class GeminiLlmClient(ILlmAdapter):
    def __init__(self):
        self.model = None
        self.agent = None

    def config_llm(self):
        api_key = os.getenv("LLM_API_KEY")
        model_name = os.getenv("MODEL")


        if not api_key or not model_name:
            raise ValueError("Missing environment variables")

        self.model = ChatGoogleGenerativeAI(
            api_key=api_key,
            model=model_name,
            temperature=0.7
        )

        self.agent = initialize_agent(
            tools=tools,
            llm=self.model,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            agent_kwargs={
                "prefix": (
                    "You are a sound assistant that controls a digital mixer via text commands. "
                    "You can adjust volume, EQ (bass, mid, treble), and mute channels. "
                    "Use the available tools to execute precise actions. "
                    "Always return JSON in ENGLISH with fields like 'channel', 'eq', etc."
                )
            }
        )

    def call_llm(self, prompt: str) -> str:
        if not self.agent:
            raise ValueError("LLM not configured. Call `config_llm()` first.")
        if not prompt:
            raise ValueError("Prompt must be a non-empty string.")
        
        response = self.agent.invoke({'input': prompt})
        return response.get('output', str(response))
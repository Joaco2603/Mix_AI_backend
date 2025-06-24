from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from llms.infraestructure.interfaces.Illm_adapter import ILlmAdapter
from llms.infraestructure.adapters.langchain.tools import Mixer  # tus herramientas personalizadas
import os

class LangchainLlmClient(ILlmAdapter):
    def __init__(self):
        self.model = None
        self.agent_executor = None

    def config_llm(self):
        api_key = os.getenv("LLM_API_KEY")
        model_name = os.getenv("MODEL")

        if not api_key or not model_name:
            raise ValueError("Missing environment variables")

        mixer = Mixer()
        tools = mixer.get_all_tools()

        # Crea el modelo Gemini
        self.model = ChatGoogleGenerativeAI(
            api_key=api_key,
            model=model_name,
            temperature=0.7
        )

        # Prompt compatible con function-calling
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a sound assistant that controls a digital mixer via text commands. "
                       "You can adjust volume, EQ (bass, mid, treble), and mute channels. "
                       "Use the available tools to execute precise actions. "
                       "Always return JSON in ENGLISH with fields like 'channel', 'eq', etc."),
            ("user", "{input}"),
            ("system", "{agent_scratchpad}")
        ])

        # Crear el agente compatible con Gemini (function-calling)
        agent = create_openai_functions_agent(
            llm=self.model,
            tools=tools,
            prompt=prompt
        )

        self.agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    def call_llm(self, prompt: str) -> str:
        if not self.agent_executor:
            raise ValueError("LLM not configured. Call `config_llm()` first.")
        if not prompt:
            raise ValueError("Prompt must be a non-empty string.")

        try:
            response = self.agent_executor.invoke({"input": prompt})

            # Si devuelve string directo
            if isinstance(response, str):
                return response
            # Si devuelve dict
            elif isinstance(response, dict):
                return response.get('output', str(response))
            else:
                return str(response[:])

        except Exception as e:
            print(f"❌ Error en LangchainLlmClient.call_llm: {e}")
            return "error"

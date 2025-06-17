from abc import ABC, abstractmethod

class ILlmAdapter(ABC): # Esto sería la interfaz de tu dominio
    @abstractmethod
    def config_llm(self):
        pass

    @abstractmethod
    def call_llm(self) -> str:
        pass
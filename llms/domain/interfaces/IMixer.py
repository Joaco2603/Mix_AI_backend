from abc import ABC, abstractmethod

class IMixer(ABC): # Esto sería la interfaz de tu dominio
    @abstractmethod
    def adjust_volume(self, input_str: str) -> str:
        pass

    @abstractmethod
    def adjust_eq(self, input: str) -> str:
        pass

    @abstractmethod
    def mute_channel(self, input: str) -> str:
        pass
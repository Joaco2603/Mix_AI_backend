from abc import ABC, abstractmethod

class IMixer(ABC):
    @abstractmethod
    def adjust_volume(self, channel: int, level: str) -> str:
        pass

    @abstractmethod
    def adjust_eq(self, channel: int, frequency: str, action: str) -> str:
        pass

    @abstractmethod
    def mute_channel(self, channel: int) -> str:
        pass
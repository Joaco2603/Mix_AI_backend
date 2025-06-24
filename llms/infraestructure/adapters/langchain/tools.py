from langchain.tools import tool
from llms.domain.interfaces.IMixer import IMixer

class Mixer(IMixer):
    def __init__(self) -> None:
        pass

    @tool
    def adjust_volume(channel, level: str) -> str:
        """
        Ajusta el volumen de un canal específico.
            - channel: número de canal
            - level: nivel como 'bajo', 'medio', 'alto'
        """
        
        return f"✅ Volumen del canal {channel} ajustado a {level}"


    @tool
    def adjust_eq(channel, frequency: str, action: str) -> str:
        """
        Ajusta la ecualización del canal.
            - channel: número de canal
            - frequency: 'graves', 'medios', 'agudos'
            - action: 'subir' o 'bajar'
        """
        return f"✅ EQ canal {channel}: {frequency} {action}"


    @tool
    def mute_channel(channel) -> str:
        """Silencia el canal especificado"""
        return f"✅ Canal {channel} silenciado"

    def get_all_tools(self):
        return [self.adjust_volume, self.adjust_eq, self.mute_channel]






from langchain.tools import tool

@tool
def adjust_volume(input: str) -> str:
    """
    Ajusta el volumen del canal.
    Formato esperado: '2 bajo' (canal nivel)
    """
    try:
        channel, level = input.strip().split()
        return f"✅ Volumen del canal {channel} ajustado a {level}"
    except Exception:
        return "❌ Formato incorrecto. Usa: '<canal> <nivel>'"

@tool
def adjust_eq(input: str) -> str:
    """
    Ajusta la ecualización.
    Formato: '2 graves subir'
    """
    try:
        channel, freq, action = input.strip().split()
        return f"✅ EQ canal {channel}: {freq} {action}"
    except Exception:
        return "❌ Formato inválido. Usa: '<canal> <frecuencia> <acción>'"

@tool
def mute_channel(input: str) -> str:
    """Silencia el canal especificado (ej: '3')"""
    return f"✅ Canal {input.strip()} silenciado"


tools = [adjust_volume, adjust_eq, mute_channel]
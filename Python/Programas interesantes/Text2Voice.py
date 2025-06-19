import pyttsx3 as pt3  # Importa la librería para convertir texto a voz utilizando el motor TTS local

# Función para mostrar las voces disponibles
def listar_voces():
    engine = pt3.init()  # Inicializa el motor TTS
    voices = engine.getProperty('voices')  # Obtiene todas las voces instaladas
    print("Voces disponibles:\n")
    # Recorre e imprime cada voz con su índice, nombre, ID e idiomas
    for i, voice in enumerate(voices):
        print(f"{i}: {voice.name} | ID: {voice.id} | Idioma(s): {voice.languages}")
    engine.stop()  # Libera el motor

# Función que convierte el texto en voz
def text2voice(text, voice_index):
    engine = pt3.init()
    voices = engine.getProperty('voices')  # Obtiene la lista de voces disponibles
    engine.setProperty('voice', voices[voice_index].id)  # Configura la voz seleccionada por índice
    engine.say(text)          # Carga el texto para ser leído
    engine.runAndWait()       # Ejecuta la lectura
    engine.stop()             # Detiene el motor

# Bloque principal del programa
if __name__ == "__main__":
    
    listar_voces()  # Muestra las voces disponibles al inicio
    while True:
        # Solicita al usuario el texto a convertir
        text = input("\nIngrese el texto a convertir en voz: ")
        # Solicita el número de la voz a utilizar
        voice = int(input("Ingrese el número de voz a utilizar (según la lista): "))
        # Ejecuta la conversión de texto a voz
        text2voice(text, voice)
        # Pregunta si desea continuar o salir
        if input("¿Desea continuar? (s/n): ").lower() != "s":
            break



# -------------------------------
# Este script permite convertir texto en voz (TTS, Text-To-Speech) utilizando la biblioteca `pyttsx3`.
#
# ✅ Requisitos:
# - Librería `pyttsx3` (instalable con pip):
#     pip install pyttsx3
#
# ⚠️ Notas:
# - El número de voces puede variar según el sistema operativo.
# -------------------------------
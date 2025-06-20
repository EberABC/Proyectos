# Diccionario Morse: Traduce caracteres a código Morse.
Morse = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
    'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
    'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
    'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',
    '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',  '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '!': '-.-.--',
    '/': '-..-.',  '-': '-....-', '(': '-.--.',  ')': '-.--.-',
    "'": '.----.', '"': '.-..-.', ':': '---...', ';': '-.-.-.',
    '=': '-...-',  '+': '.-.-.',  '_': '..--.-', '&': '.-...',
    '$': '...-..-', '@': '.--.-.', '¿': '..-.-', '¡': '--...-',
    ' ': ' '  # Espacio entre palabras
}

# Función: convierte texto plano a código Morse
def Text2Morse(text):
    return ' '.join(Morse[i] for i in text.upper() if i in Morse)

# Función: convierte código Morse a texto plano
def Morse2Text(morse):
    text = ""
    # Separa las palabras en Morse (doble espacio)
    morse_words = morse.strip().split("  ")
    for morse_word in morse_words:
        # Separa las letras (espacio simple)
        morse_chars = morse_word.strip().split(" ")
        for morse_char in morse_chars:
            for char, code in Morse.items():
                if code == morse_char:
                    text += char
                    break
        text += " "  # Añade espacio entre palabras
    return text.strip()

# Programa principal interactivo
if __name__ == "__main__":
    print("Conversor Texto - Código Morse")
    while True:
        # Selección de modo: texto a morse o morse a texto
        choice = input("¿Convertir texto a morse o morse a texto? (1/2): ")
        
        if choice == "1":
            text = input("Ingresa el texto: ")
            morse = Text2Morse(text)
            print("Código Morse:", morse)
        
        else:
            morse = input("Ingresa el código Morse (usa doble espacio entre palabras): ")
            text = Morse2Text(morse)
            print("Texto:", text)
        
        # Continuar o salir
        again = input("¿Deseas convertir otro mensaje? (y/n): ")
        if again.lower() != 'y':
            print("Finalizado")
            break

# -------------------------------
# Este script permite convertir texto plano a código Morse y viceversa,
# directamente desde la línea de comandos. Ideal para tareas educativas,
# de codificación básica o experimentación con mensajes cifrados.
#
# ✅ Características:
# - Traducción completa de letras, números, símbolos y espacios.
# - Diccionario Morse extendido con signos de puntuación y caracteres especiales.
# - Conversión bidireccional: Texto → Morse y Morse → Texto.
#
# 💡 Ejemplo de entrada (texto):
#    Hola Mundo! → .... --- .-.. .-   -- ..- -. -.. --- -.-.--
#
# 💡 Ejemplo de entrada (morse):
#    .... --- .-.. .-   -- ..- -. -.. --- -.-.-- → HOLA MUNDO!
# -------------------------------

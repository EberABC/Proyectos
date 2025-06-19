from time import sleep as sl            # Importa la función sleep
from datetime import datetime as dt     # Importa datetime

# Función que muestra la hora actual formateada como HH:MM:SS
def show_time():
    sl(1)  # Pausa de 1 segundo entre cada actualización (control del ritmo)
    now = dt.now()  # Obtiene la fecha y hora actuales del sistema
    # Imprime la hora con formato, sobrescribiendo la misma línea en consola
    return print(now.strftime("%H:%M:%S"), end="\r")  # '\r' regresa el cursor al inicio de la línea

# Bloque principal que se ejecuta si el archivo se corre directamente
if __name__ == "__main__":
    while True:
        show_time()  # Llama a la función para mostrar la hora cada segundo

# -------------------------------
# Este script muestra un reloj en tiempo real en la consola, actualizando la hora cada segundo.
# Usa formato HH:MM:SS (24 horas) y mantiene la hora en una sola línea con actualización constante.
# -------------------------------
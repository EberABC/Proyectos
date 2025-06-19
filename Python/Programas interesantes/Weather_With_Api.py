import requests as req  # Librería para hacer solicitudes HTTP

# Lista de ciudades mexicanas
MXCities = (
    "Tulancingo",        # Tulancingo (México)
    "Pachuca",           # Pachuca (México)
    "Cd+de+Mexico",      # Ciudad de México (México)
    "Tula+de+Allende",   # Tula de Allende (México)
    "Tepeapulco",        # Tepeapulco (México)
    "Apan",              # Apan (México)
    "Actopan",           # Actopan (México)
    "Tlaxcala",          # Tlaxcala (México)
    "Puebla",            # Puebla (México)
    "Queretaro",         # Querétaro (México)
    "Guadalajara",       # Guadalajara (México)
    "Monterrey"          # Monterrey (México)
)

# Lista de ciudades internacionales
WorldCities = (
    "New+York",        # Nueva York (EE. UU.)
    "Los+Angeles",     # Los Ángeles (EE. UU.)
    "Toronto",         # Toronto (Canadá)
    "Bogota",          # Bogotá (Colombia)
    "Buenos+Aires",    # Buenos Aires (Argentina)
    "Madrid",          # Madrid (España)
    "London",          # Londres (Reino Unido)
    "Paris",           # París (Francia)
    "Berlin",          # Berlín (Alemania)
    "Rome",            # Roma (Italia)
    "Tokyo",           # Tokio (Japón)
    "Seoul",           # Seúl (Corea del Sur)
    "Beijing",         # Pekín (China)
    "Delhi",           # Delhi (India)
    "Sydney"           # Sídney (Australia)
)

# Función para obtener el clima usando la API de wttr.in
def get_weather(city):
    url = "http://wttr.in/" + city + "?format=4"  # Formato de consulta
    res = req.get(url)  # Solicitud GET al servicio
    if res.status_code == 200:
        print(res.text)  # Muestra el clima
    else:
        print("Error: " + str(res.status_code))  # Muestra errores si la solicitud falla

# Bloque principal del programa
if __name__ == "__main__":
    print("Cities in Mexico:")
    print(", \n".join(city for city in MXCities))  # Imprime las ciudades mexicanas disponibles
    print()
    print("Cities in the World:")
    print(", \n".join(city for city in WorldCities))  # Imprime las ciudades internacionales disponibles
    while True:
        city = input("Enter a city name (e to exit): ")
        if city == "e":
            break
        get_weather(city) if city in MXCities or city in WorldCities else print("City not found. Try again.") # Llama a la función para mostrar el clima

# -------------------------------
# Este script consulta el clima actual en distintas ciudades (nacionales e internacionales)
# utilizando el servicio gratuito de wttr.in, todo desde la línea de comandos.
#
# 🌐 El servicio devuelve datos en formato simple como:
#     Ciudad: Condición 🌦  Temperatura 🌡
#
# ✅ Requisitos:
# - Librería `requests` (instalación con pip):
#     pip install requests
#
# ⚠️ El servicio wttr.in no requiere clave API, pero depende de que el sitio esté disponible.
# -------------------------------
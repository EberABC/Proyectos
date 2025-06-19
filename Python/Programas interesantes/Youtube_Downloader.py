import yt_dlp  # Librería para descargar videos/audio de YouTube y otros sitios
import os      # Librería para manejar rutas de archivos de forma portátil

# Define rutas predeterminadas a las carpetas de Videos y Música del usuario actual
default_video_path = os.path.join(os.path.expanduser("~"), "Videos")
default_audio_path = os.path.join(os.path.expanduser("~"), "Music")

# Función para descargar el video completo
def download_video(url, output_path):
    ydl_opts = {
        # Selecciona la mejor calidad de video + audio, con preferencia por MP4
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        # Ruta de guardado
        'outtmpl': output_path + "/%(title)s.%(ext)s",
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Inicia la descarga
        print("Video descargado exitosamente.")
    except Exception as e:
        print("Error al descargar el video:", str(e))

# Función para descargar solo el audio
def download_audio(url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',        # Selecciona el mejor audio disponible
        'audio_format': 'mp3',             # Se especifica el formato final de audio
        'outtmpl': output_path + "/%(title)s.%(ext)s",
        'postprocessors': [{               # Filtro para convertir el audio a MP3 con FFmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Inicia la descarga
        print("Audio descargado exitosamente.")
    except Exception as e:
        print("Error al descargar el audio:", str(e))

# Programa principal
if __name__ == "__main__":
    print("YouTube Downloader")
    while True:
        # Pregunta al usuario si quiere video o solo audio
        select = input("Download video or only audio (v/a)?: ")
        url = input("Enter the URL of the video: ")
        
        # Descarga de video
        if select.lower() == 'v':
            x = input(f"Enter the path of the output folder ({default_video_path}): ")
            output_path = x if x != '' else default_video_path
            download_video(url, output_path)
        
        # Descarga de audio
        else:
            x = input(f"Enter the path of the output folder ({default_audio_path}): ")
            output_path = x if x != '' else default_audio_path
            download_audio(url, output_path)
        
        # Pregunta si el usuario desea continuar
        print("Download another video? (y/n): ", end='')
        if input().lower() != 'y':
            break

# -------------------------------
# Este script permite descargar videos o extraer solo el audio desde YouTube
# de forma sencilla desde la línea de comandos, usando la biblioteca yt_dlp.
# Las rutas de guardado predeterminadas se adaptan al sistema del usuario.
#
# ✅ Requisitos antes de ejecutar el script:
#
# 1. Instalar yt-dlp (desde pip):
#    pip install yt-dlp
#
# 2. Instalar FFmpeg:
#    FFmpeg es necesario para convertir el audio a MP3.
#
# ⚠️ Este script es solo para fines personales y educativos.
# No está destinado a infringir los Términos de Servicio de YouTube.
# Respeta los derechos de autor y el uso permitido del contenido.
# -------------------------------
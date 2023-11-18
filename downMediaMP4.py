import subprocess

def descargar_video(url):
    comando = ['yt-dlp', url]
    try:
        subprocess.run(comando, check=True)
        print("Video descargado con éxito.")
    except subprocess.CalledProcessError as e:
        print(f"Error al descargar el video: {e}")

# Solicitar la URL del video
url_video = input("Ingresa el enlace del video: ")
descargar_video(url_video)

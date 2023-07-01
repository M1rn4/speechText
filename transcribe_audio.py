import openai
from dotenv import load_dotenv
import os
from gtts import gTTS


# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave de API desde las variables de entorno
api_key = os.getenv("OPENAI_API_KEY")

# Configurar la clave de API en openai
openai.api_key = api_key

# Abrir el archivo de audio
with open("./audio.mp3", "rb") as audio_file:
    # Transcribir el audio
    # transcript = openai.Audio.transcribe("whisper-1", audio_file)
    transcript = openai.Audio.translate("whisper-1", audio_file)


    #Imprimir la transcripción
    print(transcript)

# # Generar la voz del texto traducido
# respuesta = openai.Completion.create(
#     engine="gpt-3.5-turbo",
#     prompt=transcript,
#     max_tokens=50,
#     temperature=0.8,
#     n = 1,
#     stop=None,
#     echo=True
# )

# # Obtener la respuesta generada
# voz_generada = respuesta.choices[0].text.strip()

# # Imprimir la voz generada
# print(voz_generada)

#create voz
tts = gTTS(text= transcript["text"], lang="es")

tts.save("audiotraslate.mp3")
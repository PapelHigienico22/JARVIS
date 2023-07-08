import pyttsx3
import fakeyou
import tempfile
import os
import time
from pygame import mixer

fake_you = fakeyou.FakeYou()


class FakeYouTalker:
    def __init__(self, username, password, model_name):
        self.username = username
        self.password = password
        self.model_name = model_name

    def __login_to_fakeyou(self):
        fake_you.login(self.username, self.password)

    def __get_tts_token(self, model_name):
        result = fake_you.search(model_name)
        return result.voices.modelTokens[0]

    def __generate_audio(self, text):
        print('procesando modelo de voz...')
        temp_file = tempfile.mkdtemp()
        filename = os.path.join(temp_file, 'temp.wav')
        tts_model_token = self.__get_tts_token(self.model_name)
        fake_you.say(text=text, ttsModelToken=tts_model_token, filename=filename)
        return filename

    def talk(self, text):
        # mixer.init()
        # filename = self.__generate_audio(text)
        # mixer.music.load(filename)
        # mixer.music.load(bandolero_audio)
        # audio_duration = mixer.Sound(filename).get_length()
        # mixer.music.play()
        # time.sleep(audio_duration)
        mixer.init()
        filename = self.__generate_audio(text)
        song_path = 'Tego Calderon – Bandoleros.mp3'
        audio = mixer.Sound(filename)
        song = mixer.Sound(song_path)
        song.set_volume(0.1)
        song.play()
        audio.play()
        audio_duration = audio.get_length()
        time.sleep(audio_duration)
        pass



#Usa las voces instaladas en el programa
class TtsTalker:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 145)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


class Talker:
    def __init__(self, talker_cls):
        self.talker_cls = talker_cls
    
    def talk(self, text):
        self.talker_cls.talk(text)
    
        # Nos saluda
    def say_welcome(self):
        print('Hola señor. Me alegra volver a verlo, ¿de qué tema le gustaría saber?')
        mixer.init()
        audio_path = 'hola.wav'
        audio = mixer.Sound(audio_path)
        audio.play()
        audio_duration = audio.get_length()
        time.sleep(audio_duration)
    
    def listo(self):
        print('Listo')
        mixer.init()
        audio_path = 'listo.wav'
        audio = mixer.Sound(audio_path)
        audio.play()
        audio_duration = audio.get_length()
        time.sleep(audio_duration)
    
    def cumbiones(self):
        print('Reproduciendo unos buenos cumbiones, señor.')
        mixer.init()
        audio_path = 'cumbiones.wav'
        audio = mixer.Sound(audio_path)
        audio.play()
        audio_duration = audio.get_length()
        time.sleep(audio_duration)
    def proposito(self):
        print("JARVIS es una IA diseniada para asistir al usuario en diversas tareas, como responder preguntas, reproducir audios y videos, y realizar automatizaciones domóticas.")
        mixer.init()
        audio_path = 'funcion.wav'
        audio = mixer.Sound(audio_path)
        audio.play()
        audio_duration = audio.get_length()
        time.sleep(audio_duration)
    def familia(self):
        print("La familia es nuestro motor, la fuerza que nos impulsa a superar cualquier obstáculo en el camino.")
        print("Son nuestro refugio inquebrantable en medio de la tormenta, nuestra roca en un mundo lleno de caos.")
        mixer.init()
        audio_path = 'familiaToretto.wav'
        audio = mixer.Sound(audio_path)
        audio.play()
        audio_duration = audio.get_length()
        time.sleep(audio_duration)
    def familia2(self):
        print("Lo más importante es tener familia. Que trabaje en la municipalidad y te pueda conseguir algún puestito.")
        mixer.init()
        audio_path = 'familia2.wav'
        audio = mixer.Sound(audio_path)
        audio.play()
        audio_duration = audio.get_length()
        time.sleep(audio_duration)
    def vallenato(self):
        print("Reproduciendo un buen vallenato, señor.")
        mixer.init()
        audio_path = 'vallenato.wav'
        audio = mixer.Sound(audio_path)
        audio.play()
        audio_duration = audio.get_length()
        time.sleep(audio_duration)
    
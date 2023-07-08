import pywhatkit

from modules.listen import Listener
from modules.keywords.keywords import keywords
from modules.talker.talk import Talker, TtsTalker

from modules.ESP32.esp32 import EspMethods

import customtkinter
from PIL import Image
from CTkMessagebox import CTkMessagebox


talker = Talker(TtsTalker())
esp = EspMethods()

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")
#pagina
root = customtkinter.CTk()
root.geometry("700x450")
root.title("JARVIS")
# create 2x2 grid system
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure((0, 2), weight=1)

# load images
microphone = customtkinter.CTkImage(light_image=Image.open("microphone.png"),
                                  dark_image=Image.open("microphone.png"),
                                  size=(30, 30))

# ventana1
frame = customtkinter.CTkFrame(master=root)
frame.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")# "nsew" rellena verticalmente
# ventana2
frame2 = customtkinter.CTkFrame(master=root)
frame2.grid(row=0, column=2, padx=10, pady=20, sticky="nsew")# columnspan es el tamanio de la columna

# titulo
titulo = customtkinter.CTkLabel(master=frame, text="J.A.R.V.I.S.", font=("Roboto", 32))
titulo.pack(pady=(50,12), padx=10)
# subtitulo
subtitulo = customtkinter.CTkLabel(master=frame, text="(Just A Rather Very Intelligent System)", font=("Roboto", 12))
subtitulo.pack(pady=12, padx=10)

# text box
textbox = customtkinter.CTkTextbox(frame2)
textbox.pack(pady=12, padx=12,fill="both", expand=True)
textbox.insert("0.0", 'Press "play" to start talking. do not close the application')

def printTxt(txt):
    textbox.delete("0.0", "end")  # delete all text
    textbox.insert("0.0", text=txt)
    textbox.configure(state="disabled")

def main():
    listener = Listener()
    try:
        #escucha
        user_prompt = listener.listen()
        # Reproduce una cancion en youtube
        if 'reproduce' in user_prompt.lower() or 'produce' in user_prompt.lower() or 'reproduces' in user_prompt.lower() or 'ponte' in user_prompt.lower():
            song = user_prompt.replace('reproduce', '')
            talker.listo()
            printTxt(song)
            pywhatkit.playonyt(song)
        elif 'conviones' in user_prompt.lower() or 'cumbiones' in user_prompt.lower():
            printTxt(user_prompt)
            talker.cumbiones()
            pywhatkit.playonyt('https://www.youtube.com/watch?v=21tVgzbqd70')
        elif 'vallenato' in user_prompt.lower() or 'ballenado' in user_prompt.lower() or 'bajinatoor' in user_prompt.lower() or 'bañenato' in user_prompt.lower():
            printTxt(user_prompt)
            talker.vallenato()
            pywhatkit.playonyt('https://www.youtube.com/watch?v=qVmjOOEEEzU')
        elif 'función' in user_prompt.lower() or 'qué puedes hacer' in user_prompt.lower() or 'proposito' in user_prompt.lower() or '¿para qué sirves?' in user_prompt.lower() or 'propósito' in user_prompt.lower():
            printTxt(user_prompt)
            talker.proposito()
        elif 'importancia de la familia' in user_prompt.lower():
            printTxt(user_prompt)
            talker.familia()
        elif 'familia' in user_prompt.lower():
            printTxt(user_prompt)
            talker.familia2()
        elif 'prende' in user_prompt.lower() or 'enciende' in user_prompt.lower() or 'prendelo' in user_prompt.lower() or 'enciéndelo' in user_prompt.lower():
            printTxt(user_prompt)
            talker.listo()
            esp.on_led()
        elif 'apaga' in user_prompt.lower() or 'apáigalo' in user_prompt.lower() or 'apágalo' in user_prompt.lower():
            printTxt(user_prompt)
            talker.listo()
            esp.off_led()
        # Entra en modo sabiondo
        command = list(filter(lambda x: x in user_prompt, keywords))
        if command:
            keywords[command[0]]()
        else:
            print(user_prompt)
            printTxt(user_prompt)
    except Exception as e:
        print(f"Los siento no te entendí debido a este error: {e}")
        print(e)

# Play
button = customtkinter.CTkButton(master=frame, text="play", command=main, image=microphone, height=50, compound="right", font=("Roboto", 12))
button.pack(pady=12, padx=10)

def optionmenu_callback(choice):
    if choice == "Toretto":
        CTkMessagebox(title="Info", message="This option may experience problems")
    print("optionmenu dropdown clicked:", choice)

# menu desplegable
subtitulo = customtkinter.CTkLabel(master=frame2, text="Voice: ", font=("Roboto", 12))
subtitulo.pack(pady=2, padx=10)
optionmenu = customtkinter.CTkOptionMenu(master=frame2, values=["TtsTalker", "Toretto"], command=optionmenu_callback)
optionmenu.set("TtsTalker")
optionmenu.pack(pady=2, padx=10)


def appearenceMode(choice):
    customtkinter.set_appearance_mode(choice)

# menu apariencia
# subtitulo
subtitulo = customtkinter.CTkLabel(master=frame2, text="Theme color:", font=("Roboto", 12))
subtitulo.pack(pady=2, padx=10)
appearenceModeMenu = customtkinter.CTkOptionMenu(master=frame2, values=["dark", "light", "system"], command=appearenceMode)
appearenceModeMenu.set("system")
appearenceModeMenu.pack(pady=(2, 30), padx=10)


if __name__ == '__main__':
    root.mainloop()
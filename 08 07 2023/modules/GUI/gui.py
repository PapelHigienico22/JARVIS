import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x350")


def play():
    print("Test")

# load images
microphone = customtkinter.CTkImage(light_image=Image.open("microphone.png"), dark_image=Image.open("microphone.png"), size=(30, 30))

# ventana padre
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# titulo
label = customtkinter.CTkLabel(master=frame, text="J.A.R.V.I.S.", font=("Roboto", 32))
label.pack(pady=12, padx=10)
# titulo
label = customtkinter.CTkLabel(master=frame, text="(Just A Rather Very Intelligent System)", font=("Roboto", 12))
label.pack(pady=12, padx=10)

#Play
button = customtkinter.CTkButton(master=frame, text="Play", command=play, image=microphone, height=50, compound="right", font=("Roboto", 12))
button.pack(pady=12, padx=10)


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

# menu desplegable
optionmenu = customtkinter.CTkOptionMenu(master=frame, values=["TtsTalker", "Toretto (puede experimentar problemas de lentitud)"], command=optionmenu_callback)
optionmenu.pack(pady=12, padx=10)


root.mainloop()
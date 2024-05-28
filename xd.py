import tkinter as tk
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import customtkinter as ctk
def sillas():
    logo_sillas = Image.open("silla.png")
    sitios = tk.Button()


# Crear la ventana principal de la aplicación usando customtkinter
app = ctk.CTk()
app.geometry("900x700")
app.title("Mi Proyecto")
sillas()

app.mainloop()
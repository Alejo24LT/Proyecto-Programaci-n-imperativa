# app.mainloop()
#Todo lo que esta aqui es las librerias que se necesita 
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import customtkinter as ctk

# Crear la ventana principal de la aplicación usando customtkinter
app = ctk.CTk()
app.geometry("900x700")
app.title("Mi Proyecto")

#En esta parte se configura toda la parte de bienvenida 
label_font = ("Georgia", 40, "bold")
label = ctk.CTkLabel(app, text="Bienvenido a Bluesky Airlines", font=label_font, text_color="blue")
label.pack(pady=20)

#Aqui carga la imagen que esta en un directorio 
imagen = Image.open("airplane-flying-vector-icon.jpg")
imagen = imagen.resize((800, 600))
imagen_tk = ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(app, image=imagen_tk)
label_imagen.pack()


def ventana_dos():#En esta funcion se abre una nueva ventana 
    nueva_ventana = tk.Toplevel(app)
    nueva_ventana.title("Realizar compra de ticket")
    label = tk.Label(nueva_ventana, text="Realiza Compra de tu ticket", font=("Georgia", 20, "bold"))
    label.pack(pady=20)
    nueva_ventana.geometry("900x800")
#con el button que esta adelante es que se abre la nueva ventana 
boton = tk.Button(app, text="Click para Continuar", width=20, bg="blue", fg="white", font=("Helvetica", 16, "italic"), command=ventana_dos)
boton.pack(pady=30)

# esta es la funcion con la que se corre el codigo 
app.mainloop()




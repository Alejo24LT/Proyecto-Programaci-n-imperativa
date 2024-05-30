# app.mainloop()
#Todo lo que esta aqui es las librerias que se necesita 
import tkinter as tk
import time
import random
from tkinter import Label
from PIL import Image, ImageTk
import customtkinter as ctk
from tabulate import tabulate
# Crear la ventana principal de la aplicación usando customtkinter
app = ctk.CTk()
app.geometry("650x600")
app.title("Mi Proyecto")

#En esta parte se configura toda la parte de bienvenida 
label_font = ("Georgia", 40, "bold")
label = ctk.CTkLabel(app, text="Bienvenido a Bluesky Airlines", font=label_font, text_color="blue")
label.grid(row=0,column=2, columnspan=5, pady=20)  #Modificacion temporal por compatibilida del grid

# # Aqui carga la imagen que esta en un directorio
# imagen = Image.open("airplane-flying-vector-icon.jpg")
# imagen = imagen.resize((800, 600))
# imagen_tk = ImageTk.PhotoImage(imagen)
# label_imagen = tk.Label(app, image=imagen_tk)
# label_imagen.pack()


# def ventana_dos():#En esta funcion se abre una nueva ventana 
#     nueva_ventana = tk.Toplevel(app)
#     nueva_ventana.title("Realizar compra de ticket")
#     label = tk.Label(nueva_ventana, text="Realiza Compra de tu ticket", font=("Georgia", 20, "bold"))
#     label.pack(pady=20)
#     nueva_ventana.geometry("900x800")
# #con el button que esta adelante es que se abre la nueva ventana 
# boton = tk.Button(app, text="Click para Continuar", width=20, bg="blue", fg="white", font=("Helvetica", 16, "italic"), command=ventana_dos)
# boton.pack(pady=30)


import tkinter as tk
import random


def sillas_premium(app):                                ##Aqui guarde todas las funciones de los premium NO MOVER POR EL PUTAS 
    sillas_ocupadas = []                                    ##No borrar los prints, los uso como guia
    filas_sillas = ["A", "B", "C", "D", "E", "F"]
    
    with open("SillasOcupadas.txt", "r") as sillas_txt:             ##Lee todas las sillas ocupadas
        sillas_ocupadas = sillas_txt.read().splitlines()
            
    def silla_escogida(sitio, id):
        if id in sillas_ocupadas:                    ##Si la silla ya la ocuparon, este muestra el mensaje
            aviso = tk.Toplevel(app)
            aviso.title("Aviso")
            texto_aviso = tk.Label(aviso, text=f"La silla {id} ya está ocupada\nO no está disponible.", font=("Georgia", 20, "bold"))
            texto_aviso.pack(pady=20)
            print(f"La silla {id} ya está ocupada.")
        else:
            print(f"Silla escogida: {id}")
            sitio.config(bg="red")
            sillas_ocupadas.append(id)              ##Este mete la silla en una lista y en el txt    
            with open("SillasOcupadas.txt", "w") as sillas_txt:
                for asiento in sillas_ocupadas:
                    sillas_txt.write(f"{asiento}\n")            #Si un premium quiere escoger clase pobre, muestra mensaje
            texto_aviso = tk.Label(aviso, text=f"Por favor escoja una silla del nivel DIAMANTE\nPara eso pagó", font=("Georgia", 20, "bold"))
            texto_aviso.pack(pady=20)

    recuadro_sillas = tk.Frame(app, bg='blue')                          #El marco de los asientos
    recuadro_sillas.grid(row=1, column=2,columnspan=5, padx=5, pady=5)  
        
    for i in range(len(filas_sillas)):                          ##Genera las sillas en el marco
        for j in range(1, 13):
            silla_especifica = f"{filas_sillas[i]}{j}" 
            if j == 1:  
                sitios = tk.Label(recuadro_sillas, text=silla_especifica, width=1, height=1)
            else:
                sitios = tk.Label(recuadro_sillas, width=1, height=1)
            sitios.bind("<Button-1>", lambda event, sitio=sitios, id=silla_especifica: silla_escogida(sitio, id))
        
            if silla_especifica in sillas_ocupadas:
                sitios.config(bg="red")
            if j <= 3:                                          ##Separa en dos columnas las sillas
                sitios.grid(column=i, row=j-1, padx=5, pady=5)  
            else:
                sitios.grid(column=i, row=j+1, padx=5, pady=5)  


def sillas_diamante(app):
    sillas_ocupadas = []
    silla_azar1 = None
    filas_sillas = ["A", "B", "C", "D", "E", "F"]
    boton_seleccionar = tk.Button(app, text="Seleccionar silla", command=None)

    with open("SillasOcupadas.txt", "r") as sillas_txt:
        sillas_ocupadas = sillas_txt.read().splitlines()

    sillas_disponibles = ["A5","A6","A7","A8","B5","B6","B7","B8","C5","C6","C7","C8","D5","D6","D7","D8","E5","E6","E7","E8","F5","F6","F7","F8"]

    def silla_azar(silla_azar1):
        if sillas_disponibles:
            silla_azar1 = random.choice(sillas_disponibles)
            sillas_disponibles.remove(silla_azar1)
            return silla_azar1
        else:
            sin_sillas_diamante = tk.Toplevel(app)
            sin_sillas_diamante.title("Aviso")
            texto_nosillas_diamante = tk.Label(sin_sillas_diamante, text="No hay mas sillas disponibles en esta clase!", font=("Georgia", 20, "bold"))
            texto_nosillas_diamante.pack(pady=20)

    def silla_aleatoria_agg(silla_azar1):
        sillas_ocupadas.append(silla_azar1)
        with open("SillasOcupadas.txt", "a") as sillas_txt:
            sillas_txt.write(f"{silla_azar1}\n")

    def actualizar_sillas(silla_azar1):
        for i in range(len(filas_sillas)):
            for j in range(1, 13):
                silla_especifica = f"{filas_sillas[i]}{j}"
                sitios = tk.Label(recuadro_sillas, width=1, height=1)

                if silla_especifica in sillas_ocupadas:
                    sitios.config(bg="red")
                elif silla_especifica == silla_azar1:
                    sitios.config(text="X",bg="green yellow")

                if j <= 3:
                    sitios.grid(column=i, row=j-1, padx=5, pady=5)
                else:
                    sitios.grid(column=i, row=j+1, padx=5, pady=5)

    recuadro_sillas = tk.Frame(app, bg='blue')
    recuadro_sillas.grid(row=1, column=2,columnspan=5, padx=5, pady=5)

    def seleccionar_silla(silla_azar1):
        boton_seleccionar.config(state=tk.DISABLED)
        silla_azar1 = silla_azar(silla_azar1)
        if silla_azar1 is not None:
            silla_aleatoria_agg(silla_azar1)
            actualizar_sillas(silla_azar1)
 

    boton_seleccionar.config(command=lambda: seleccionar_silla(silla_azar1))  # Set the initial state of the button to normal
    boton_seleccionar.grid(column=2)
    actualizar_sillas(silla_azar1)
    boton_seleccionar.config(state=tk.NORMAL)

    def paquetes_vuelo():
        recuadro_paquetes = tk.Frame(app, bg='blue')
        recuadro_paquetes.grid(row=1, column=2, padx=5, pady=5)
        paquetes = tk.Label(recuadro_paquetes, text="PREMIUM\n\n\n\nDIAMANTE\n\n\n\nALUMINIO", font=("Georgia", 20, "bold"))
        paquetes.pack()
        paquetes.config(bg=recuadro_paquetes.cget('bg'))

    paquetes_vuelo()

sillas_diamante(app)
app.mainloop()

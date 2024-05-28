# app.mainloop()
#Todo lo que esta aqui es las librerias que se necesita 
import tkinter as tk
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




def sillas_diamante(app): #Funcion para usuarios diamante poder escoger silla
    sillas_ocupadas = []
    filas_sillas = ["A", "B", "C", "D", "E", "F"]
    with open("SillasOcupadas.txt", "r") as sillas_txt:
        sillas_ocupadas = sillas_txt.read().splitlines() #Lee en el txtque sillas ya se encuentran ocupadas
        
    def silla_escogida(sitio, id):
        if id in sillas_ocupadas:  # Si la silla presionada ya esta ocupada 
            silla_no_disponible = tk.Toplevel(app, bg="blue", width=200, height=200)
            txt_silla_ocupada = tk.Label(silla_no_disponible, text="Silla ocupada, seleccione otra", font=("Georgia", 20, "bold"))
            txt_silla_ocupada.pack(pady=20)
            print(f"La silla {id} ya está ocupada.")
        else:
            print(f"Silla escogida: {id}")
            sitio.config(bg="red")
            sillas_ocupadas.append(id)  ##NO BORRAR ESTA LINEA, NO SE AUN SI ES NECESARIA
            with open("SillasOcupadas.txt", "w") as sillas_txt: ##Escribe en el txt que silla se ocupo
                for asiento in sillas_ocupadas:
                    sillas_txt.write(f"{asiento}\n")

    recuadro_sillas = tk.Frame(app, bg='blue')  # Marco para las sillas
    recuadro_sillas.grid(row=1, column=2,columnspan=5, padx=5, pady=5)  
    
    for i in range(len(filas_sillas)):
        for j in range(1, 13):
            silla_especifica = f"{filas_sillas[i]}{j}" ##Las 12 sillas por cada letra
            sitios = tk.Label(recuadro_sillas, width=1, height=1)  
            sitios.bind("<Button-1>", lambda event, sitio=sitios, id=silla_especifica: silla_escogida(sitio, id))
    
            if silla_especifica in sillas_ocupadas:  # Si la silla está ocupada o se ocupa, cambia su color a rojo
                sitios.config(bg="red")
    
            if j <= 3:
                sitios.grid(column=i, row=j-1, padx=5, pady=5)  # Primeras 3 columnas
            else:
                sitios.grid(column=i, row=j+1, padx=5, pady=5)  # Segundas 3 columnas
    def paquetes_vuelo():
        recuadro_paquetes = tk.Frame(app, bg='blue')  # Marco para los paquetes
        recuadro_paquetes.grid(row=1, column=2, padx=5, pady=5)
        paquetes = tk.Label(recuadro_paquetes, text="PREMIUM\n\n\n\nDIAMANTE\n\n\n\nALUMINIO", font=("Georgia", 20, "bold"))
        paquetes.pack()
        paquetes.config(bg=recuadro_paquetes.cget('bg'))   #Quitar fondo al tetxo
    
    paquetes_vuelo()  


        


sillas_diamante(app)


app.mainloop()  # Iniciar la aplicación
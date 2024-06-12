import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

#se crea esta funcion con la que mas adelante se va a utilizar ya que aqui se guardan datos
def solicitud_datos():
    def Datos_A_guardar():
        nombres = entrada_nombres.get()
        apellidos = entrada_apellidos.get()
        genero = entrada_genero.get()
        identificacion = entrada_identificacion.get()
        nacionalidad = entrada_nacionalidad.get()
        correo = entrada_correo.get()
        telefono = entrada_telefono.get()
        
    #Condicion del correo electrónico
        if "@" not in correo or "." not in correo:
    #todos lo messagebox son para mostrar ventanillas de errores o tambien informar si es correcto

            messagebox.showerror("ERROR", "Para validar tu correo debe tener (@) y un (.) ")#La separacion de la coma permite que aparezca los datos en una ventanilla pequeño
            return

    #Condicion para el numero de telefono
        if not re.match(r"^[3]\d{9}$", telefono): 
            messagebox.showerror("ERROR", "El número de teléfono debe tener minimo 10 numeros y comenzar con 3")
            return
        
    #Condicion de no permitir dejar espacios en blanco
        if not all([nombres, apellidos, genero, identificacion, nacionalidad, correo, telefono]):
            messagebox.showerror("Error de validación", "Todos los campos deben estar llenos")
            return
    #guardamos los datos en un archivo de texto
        with open("datos_usuario.txt", "a") as file:
            file.write(f"Nombres: {nombres}\n") 
            file.write(f"Apellidos: {apellidos}\n")
            file.write(f"Genero: {genero}\n")
            file.write(f"Numero de Identificacion: {identificacion}\n")
            file.write(f"Nacionalidad: {nacionalidad}\n")
            file.write(f"Correo electronico: {correo}\n")
            file.write(f"Numero de Telefono: {telefono}\n")
            file.write("-" * 40 + "\n")
        messagebox.showinfo("CORRECTO", "Los datos se han guardado en la base de datos")

    la_ventana = tk.Tk()
    la_ventana.title("Datos del usuario")
    la_ventana.geometry("800x500")
    la_ventana.configure(bg="#2c3e50")

    #Estilos personalizados aqui todos lo que aparece en las ventanas para escribir y su estetica va aqui
    style = ttk.Style()
    style.configure("Custom.TFrame", background='#0a3d62')
    style.configure("Custom.TLabel", background='#0a3d62', foreground='#ffffff', font=('Courier New', 16))
    style.configure("Titulo.TLabel", background='#0a3d62', foreground='#ffffff', font=('Courier New', 20, 'bold'))
    style.configure("Custom.TButton", background='#78e08f', foreground='#1e272e', font=('Courier New', 12, 'bold'))
    style.configure("Custom.TEntry", fieldbackground='#ffffff', font=('Courier New', 12))
    style.map("Custom.TButton",
            background=[('active', '#38ada9'), ('pressed', '#78e08f')],
            foreground=[('active', '#ffffff'), ('pressed', '#1e272e')])

    # Para el marco 
    ventana1 = ttk.Frame(la_ventana, padding="20", style="Custom.TFrame")
    ventana1.pack(fill="both", expand=True)

    #SU detalle del titulo
    titulodentro = ttk.Label(ventana1, text="Datos del usuario", style="Titulo.TLabel")
    titulodentro.grid(row=0, column=0, columnspan=2, pady=20)#lugar de su ubicacion  con grid

    #funcion para crear los campos de entrada
    def datos_que_entran(ventana1, label_text, row):
        datos = ttk.Label(ventana1, text=label_text, style="Custom.TLabel")
        datos.grid(row=row, column=0, pady=5, sticky=tk.W)
        entradas = ttk.Entry(ventana1, style="Custom.TEntry")
        entradas.grid(row=row, column=1, pady=5, padx=10, sticky=tk.EW)
        return entradas
    entrada_nombres = datos_que_entran(ventana1, "Nombres Completos:", 1)
    entrada_apellidos = datos_que_entran(ventana1, "Apellidos Completos:", 2)
    entrada_genero = datos_que_entran(ventana1, "Género (Masculino/Femenino/Otro):", 3)
    entrada_identificacion = datos_que_entran(ventana1, "Número de Identificación:", 4)
    entrada_nacionalidad = datos_que_entran(ventana1, "Nacionalidad:", 5)
    entrada_correo = datos_que_entran(ventana1, "Correo Electrónico:", 6)
    entrada_telefono = datos_que_entran(ventana1, "Número de Teléfono:", 7)

    #boton para cargar datos a la funcion datos_A_guardar
    boton = ttk.Button(ventana1, text="Registrar Datos", style="Custom.TButton", command=Datos_A_guardar)
    boton.grid(row=8, column=0, columnspan=2, pady=20)

    # con esta parte nos permite extender la parte del codigo
    ventana1.columnconfigure(0, weight=1)
    ventana1.columnconfigure(1, weight=2)

    la_ventana.mainloop()#Imprimimos para mostrar en ventana
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

#se crea esta funcion con la que mas adelante se va a utilizar ya que aqui se guardan datos
def Datos_A_guardar():
    nombres = entry_nombres.get()
    apellidos = entry_apellidos.get()
    genero = entry_genero.get()
    identificacion = entry_identificacion.get()
    nacionalidad = entry_nacionalidad.get()
    correo = entry_correo.get()
    telefono = entry_telefono.get()
    
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

root = tk.Tk()
root.title("Datos del usuario")
root.geometry("800x500")
root.configure(bg="#2c3e50")

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
frame = ttk.Frame(root, padding="20", style="Custom.TFrame")
frame.pack(fill="both", expand=True)

#SU detalle del titulo
label = ttk.Label(frame, text="Datos del usuario", style="Titulo.TLabel")
label.grid(row=0, column=0, columnspan=2, pady=20)#lugar de su ubicacion  con grid

#funcion para crear los campos de entrada
def create_entry(frame, label_text, row):
    label = ttk.Label(frame, text=label_text, style="Custom.TLabel")
    label.grid(row=row, column=0, pady=5, sticky=tk.W)
    entry = ttk.Entry(frame, style="Custom.TEntry")
    entry.grid(row=row, column=1, pady=5, padx=10, sticky=tk.EW)
    return entry
entry_nombres = create_entry(frame, "Nombres Completos:", 1)
entry_apellidos = create_entry(frame, "Apellidos Completos:", 2)
entry_genero = create_entry(frame, "Género (Masculino/Femenino/Otro):", 3)
entry_identificacion = create_entry(frame, "Número de Identificación:", 4)
entry_nacionalidad = create_entry(frame, "Nacionalidad:", 5)
entry_correo = create_entry(frame, "Correo Electrónico:", 6)
entry_telefono = create_entry(frame, "Número de Teléfono:", 7)

#boton para cargar datos a la funcion datos_A_guardar
update_button = ttk.Button(frame, text="Registrar Datos", style="Custom.TButton", command=Datos_A_guardar)
update_button.grid(row=8, column=0, columnspan=2, pady=20)

# con esta parte nos permite extender la parte del codigo
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=2)

root.mainloop()#Imprimimos para mostrar en ventana

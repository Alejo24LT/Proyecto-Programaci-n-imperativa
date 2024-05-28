

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

def datos_a_guardar():
    nombres = entry_nombres.get()
    apellidos = entry_apellidos.get()
    genero = entry_genero.get()
    identificacion = entry_identificacion.get()
    nacionalidad = entry_nacionalidad.get()
    correo = entry_correo.get()
    telefono = entry_telefono.get()
    
    # esta es como lo mas principal para que al momento de dejar un espacio en blanco no deje continuar 
    if not all([nombres, apellidos, genero, identificacion, nacionalidad, correo, telefono]):
        messagebox.showerror("ah ocurrido un error ", "Por favor debes llenar todos los datos que se solicitan :(")
        return

    # esta condicion es para poder verificar el correo 
    if "@" not in correo or "." not in correo:
        messagebox.showerror("Error", "EL correo electrónico debe contener por lo menos una (@) y un (.)")
        return

    #condicion para verficar el numero de telefono
    if not re.match(r"^[367]\d{9}$", telefono):
        messagebox.showerror("Error", "El número de teléfono debe tener al menos 10 dígitos y comenzar con 3")
        return

    #aqui se guardan los datos en un archivo de texto
    with open("datos_usuario.txt", "a") as file:
        file.write(f"Nombres: {nombres}\n")
        file.write(f"Apellidos: {apellidos}\n")
        file.write(f"Género: {genero}\n")
        file.write(f"Número de Identificación: {identificacion}\n")
        file.write(f"Nacionalidad: {nacionalidad}\n")
        file.write(f"Correo electrónico: {correo}\n")
        file.write(f"Número de Teléfono: {telefono}\n")
        file.write("-" * 40 + "\n")

    #con esto mostramos los datos en la ventana
    result_label.config(text=f"Nombres: {nombres}\nApellidos: {apellidos}\nGénero: {genero}\nIdentificación: {identificacion}\nNacionalidad: {nacionalidad}\nCorreo: {correo}\nTeléfono: {telefono}")

    # aqui con esto se oculta la ventana para poder mostrar los datos 
    for widget in entry_widgets:
        widget.grid_forget()

root = tk.Tk()
root.title("Datos del usuario")
root.geometry("800x700")
root.configure(bg="#2c3e50")

# Creamos un marco estilo personalizado frame
frame = ttk.Frame(root, padding="20 20 20 20", style="Custom.TFrame")
frame.pack(fill="both", expand=True)

#es para su titulo
label = ttk.Label(frame, text="Datos del usuario", style="Title.TLabel")
label.grid(row=0, column=0, columnspan=4, pady=20)

#configuramos su ubicacion y todos los widgets para los datos que se solicita
def create_entry(frame, label_text, row, col):
    label = ttk.Label(frame, text=label_text, style="Custom.TLabel")
    label.grid(row=row, column=col, padx=10, pady=5, sticky="e")
    entry = ttk.Entry(frame, style="Custom.TEntry")
    entry.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
    return label, entry

entry_widgets = []

label_nombres, entry_nombres = create_entry(frame, "Nombres Completos:", 1, 0)
label_apellidos, entry_apellidos = create_entry(frame, "Apellidos Completos:", 2, 0)
label_genero, entry_genero = create_entry(frame, "Género (Masculino/Femenino/Otro):", 3, 0)
label_identificacion, entry_identificacion = create_entry(frame, "Número de Identificación:", 4, 0)
label_nacionalidad, entry_nacionalidad = create_entry(frame, "Nacionalidad:", 5, 0)
label_correo, entry_correo = create_entry(frame, "Correo Electrónico:", 6, 0)
label_telefono, entry_telefono = create_entry(frame, "Número de Teléfono:", 7, 0)

entry_widgets.extend([label_nombres, entry_nombres, label_apellidos, entry_apellidos,
                      label_genero, entry_genero, label_identificacion, entry_identificacion,
                      label_nacionalidad, entry_nacionalidad, label_correo, entry_correo,
                      label_telefono, entry_telefono])

#esta es la parte donde creamos el boton para que cargue los datos que se registro
update_button = ttk.Button(frame, text="Cargar Datos", style="Custom.TButton", command=datos_a_guardar)
update_button.grid(row=8, column=0, columnspan=2, pady=20, padx=200, sticky="nsew")
entry_widgets.append(update_button)  # Añadimos el botón a la lista de widgets

#se muestran los resultados
result_label = ttk.Label(frame, text="", style="Custom.TLabel")
result_label.grid(row=9, column=0, columnspan=2, pady=20, padx=200, sticky="nsew")

#aqui personalizamos el color 
style = ttk.Style()
style.configure("Custom.TFrame", background='#2c3e50')
style.configure("Title.TLabel", background='#2c3e50', foreground='#ffffff', font=('Comic Sans MS', 24, 'bold'))
style.configure("Custom.TLabel", background='#2c3e50', foreground='#ffffff', font=('Comic Sans MS', 14))
style.configure("Custom.TButton", background='#2ce08f', foreground='#1e272e', font=('Comic Sans MS', 14, 'bold'))
style.configure("Custom.TEntry", fieldbackground='#ffffff', font=('Helvetica', 14), padding=5)
style.map("Custom.TButton",
          background=[('active', '#38ada9'), ('pressed', '#78e08f')],
          foreground=[('active', '#ffffff'), ('pressed', '#1e272e')])

root.mainloop()

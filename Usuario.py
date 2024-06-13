import tkinter as tk
from tkinter import messagebox
import re
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import re
def abrir_ventana():
    from Vuelos import abrir_ventana
                                                ##ESTA FUNCION ES LA QUE DEJA EJECUTAR LOS ASIENTOS Y LOS VUELOS

def verifica_datos_existentes():
    pass

def validar_check_in():
    telefono = telefono_entrada.get()
    correo = correo_entrada.get()
    if not telefono.isdigit() or len(telefono) < 10:
        messagebox.showerror("Incorrecto", "Tu numero de celular necesita contener 10 digitos por lo minimo.")
        return
    datos = {
        "Nombre": nombre_entrada.get(),
        "Apellido": apellido_entrada.get(),
        "Genero": genero_entrada.get(),
        "Identificacion": identificacion_entrada.get(),
        "Nacionalidad": nacion_entrada.get(),
        "Telefono": telefono,
        "Correo": correo
    }
    with open("datos.txt", "a") as file:
        for i, valor in datos.items():
            file.write(f"{i}: {valor}\n")
        file.write("\n")

    messagebox.showinfo("Éxito", "Tus datos se han guardado para el check-in, continua con el proceso.")
    

    chequeo_ventana.destroy()
    abrir_nueva_ventana()
#Con esta abre a la nueva ventana osea la tercera ventana que ya de lo de   del destino origen del vuelo y todo lo demas
def abrir_nueva_ventana():
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry("600x400")
    nueva_ventana.configure(bg="#000080")
    nueva_ventana.resizable(False, False)
    
    titulo_nueva_ventana = tk.Label(nueva_ventana, text="¡Tercera ventana!", font=("Times", 30), bg="#000080", fg="white")
    titulo_nueva_ventana.pack(pady=20)

    # Agregar más widgets o lógica según sea necesario

    boton_cerrar = tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy, bg="beige", fg="#1e272e", font=("Comic Sans MS", 13, "bold"))
    boton_cerrar.pack(pady=20)

def solicitar_check_in():
    ventanita.withdraw()
    global chequeo_ventana
    chequeo_ventana = tk.Toplevel(ventanita)
    chequeo_ventana.title("Ventana de datos para check-in")
    chequeo_ventana.geometry("600x400")
    chequeo_ventana.configure(bg="#000080")
    chequeo_ventana.resizable(False, False)

    def crear_entrada(frame, texto, fila, columna):
        bloque = tk.Label(frame, text=texto, bg="#000080", fg="white")
        bloque.grid(row=fila, column=columna, padx=5, pady=5, sticky="w")
        bloque_uno = tk.Entry(frame)
        bloque_uno.grid(row=fila, column=columna + 1, padx=5, pady=5)
        return bloque_uno

    titulo_delcheck = tk.Label(chequeo_ventana, text="Realizar Check-in", font=("Times", 30), bg="#000080", fg="white")
    titulo_delcheck.pack(pady=20)

    frame = tk.Frame(chequeo_ventana, bg='#000080', bd=2)
    frame.pack(pady=10, padx=10, fill="both", expand=True)

    global genero_entrada, nombre_entrada, apellido_entrada, identificacion_entrada, nacion_entrada, telefono_entrada, correo_entrada
    nombre_entrada = crear_entrada(frame, "Nombre", 1, 0)
    apellido_entrada = crear_entrada(frame, "Apellido", 2, 0)
    genero_entrada = crear_entrada(frame, "Genero", 0, 0)
    identificacion_entrada = crear_entrada(frame, "Numero de Identificacion", 3, 0)
    nacion_entrada = crear_entrada(frame, "Nacionalidad", 4, 0)
    telefono_entrada = crear_entrada(frame, "Telefono", 5, 0)
    correo_entrada = crear_entrada(frame, "Correo electronico", 6, 0)

    boton_seleccionar = tk.Button(frame, text="Continuar", bg='beige', font=("Comic Sans MS", 10), command=abrir_ventana)
    boton_seleccionar.grid(row=7, column=0, columnspan=2, pady=10)

    boton_cierra = tk.Button(chequeo_ventana, text="Cerrar", command=ventanita.destroy, bg="beige", fg="#1e272e", font=("Comic Sans MS", 13, "bold"))
    boton_cierra.pack(pady=20)

ventanita = tk.Tk()
ventanita.title("Ventana Entrada 1")
ventanita.geometry("600x400")
ventanita.configure(bg="#000080")
ventanita.resizable(False, False)

titulo_abajo = tk.Label(ventanita, text="¡Cada vuelo es una aventura!", fg="white", bg="#000080", font=("Fixedsys", 14), anchor="w")
titulo_abajo.place(x=160, y=370, relwidth=1.0, height=30)

dibujo = tk.Label(ventanita, text="✈️", bg="#000080", fg="white", font=("Tahoma", 40), anchor="w")
dibujo.place(x=30, y=150, relwidth=1.0, height=30)
dibujo2 = tk.Label(ventanita, text="✈️", bg="#000080", font=("Tahoma", 40), fg="white", anchor="w")
dibujo2.place(x=490, y=150, relwidth=1.0, height=30)

titulo_principal = tk.Label(ventanita, text="Bienvenido a Bluesky Airlines", font=("Times", 30), bg="#000080", fg="white")
titulo_principal.pack(pady=20)

nombre_viajero = tk.Label(ventanita, fg="white", bg="#000080", font=("Comic Sans MS", 14), text="Apellido:")
nombre_viajero.pack(pady=5)
entradausuario = tk.Entry(ventanita)
entradausuario.pack(pady=5)

codigo_viajero = tk.Label(ventanita, bg="#000080", font=("Comic Sans MS", 14), fg="white", text="Código:")
codigo_viajero.pack(pady=5)
entradacodigo = tk.Entry(ventanita, show="★")
entradacodigo.pack(pady=5)

boton_login = tk.Button(ventanita, text="Cargar", command=verifica_datos_existentes, bg="beige", font=("Comic Sans MS", 13, "bold"), fg="#1e272e")
boton_login.place(x=250, y=250, width=100, height=40)

boton_de_entrada_proceso = tk.Button(ventanita, text="Solicitar Check-in", command=solicitar_check_in, bg="beige", fg="#1e272e", font=("Comic Sans MS", 10, "bold"))
boton_de_entrada_proceso.place(x=240, y=300, width=120, height=40)

ventanita.mainloop()


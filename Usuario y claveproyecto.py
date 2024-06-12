import tkinter as tk
from tkinter import messagebox

def verifica_datos_existentes():
    nombre = entradausuario.get()
    codigo = entradacodigo.get()

    # para ejemplo
    usuario_correcto = "univalle"
    codigo_viaje = "3743"

    if nombre == usuario_correcto and codigo == codigo_viaje:
        messagebox.showinfo("Usuario ya registrado", "¡Bienvenido!")
    else:
        messagebox.showerror("No registrado", "Tus datos no estan registrado en nuestra base de datos")

def solicitar_check_in():
    ventanita.withdraw()  # Ocultar ventana principal
    check_in_window = tk.Toplevel(ventanita)
    check_in_window.title("Check-in")
    check_in_window.geometry("600x400")
    check_in_window.configure(bg="red")
    check_in_window.resizable(False, False)

    # Etiqueta de check-in exitoso es temporal aqui ya van los datos que se van las funciones de los codigos de vuelo y todo lo demas
    check_in_label = tk.Label(check_in_window, text="Check-in exitoso", font=("Times", 30), bg="red", fg="white")
    check_in_label.pack(pady=20)
    close_button = tk.Button(check_in_window, text="Cerrar", command=ventanita.destroy, bg="beige", fg="#1e272e", font=("Comic Sans MS", 13, "bold"))
    close_button.pack(pady=20)
# Configuración de la ventana principal
ventanita = tk.Tk()
ventanita.title("Login")
ventanita.geometry("600x400")
ventanita.configure(bg="#000080")
ventanita.resizable(False, False)
#Configuracion del titulo estetico de la ventana
titulo_abajo = tk.Label(ventanita, text="¡Cada vuelo es una aventura!",fg="white",bg="#000080",font=("Fixedsys",14),anchor="w")
titulo_abajo.place(x=160, y=370, relwidth=1.0, height=30)
#Configuracion de los aviones en la ventana
dibujo = tk.Label(ventanita, text="✈️", bg="#000080",fg="white",font=("Tahoma", 40), anchor="w")
dibujo.place(x=30, y=150, relwidth=1.0, height=30)
dibujo2 = tk.Label(ventanita, text="✈️", bg="#000080",font=("Tahoma", 40),fg="white", anchor="w")
dibujo2.place(x=490, y=150, relwidth=1.0, height=30)
#Titulo de bienvenida
titulo_principal = tk.Label(ventanita, text="Bienvenido a Bluesky Airlines",font=("Times", 30), bg="#000080", fg="white")
titulo_principal.pack(pady=20)
#Configuracion que pide los datos
nombre_viajero = tk.Label(ventanita, fg="white", bg="#000080",font=("Comic Sans MS", 14),text="Apellido:")
nombre_viajero.pack(pady=5)
entradausuario = tk.Entry(ventanita)
entradausuario.pack(pady=5)
#Configuracion que pide su codigo 
codigo_viajero = tk.Label(ventanita,bg="#000080",font=("Comic Sans MS", 14),fg="white",text="Codigo:")
codigo_viajero.pack(pady=5)
entradacodigo = tk.Entry(ventanita, show="★")
entradacodigo.pack(pady=5)
#Boton para cargar los datos verifica si los datos estan registrados o no 
boton_login = tk.Button(ventanita, text="Cargar",command=verifica_datos_existentes,bg="beige",font=("Comic Sans MS", 13, "bold"), fg="#1e272e")
boton_login.place(x=250, y=250, width=100, height=40)
#Boton para solicitar el check-in aqui es que nos toca poner el nombre de la funcion del otro codigo 
boton_de_entrada_proceso = tk.Button(ventanita,text="Solicitar Check-in", command=solicitar_check_in, bg="beige", fg="#1e272e", font=("Comic Sans MS", 10, "bold"))
boton_de_entrada_proceso.place(x=240, y=300, width=120, height=40)
#ejecuta la ventana
ventanita.mainloop()

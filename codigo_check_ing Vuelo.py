
import tkinter as tk

#creacion de la primera principal
ventana_de_tiquetes = tk.Tk()
ventana_de_tiquetes.title("Tu Ticket de Vuelo")
#establecemos el tamaño de la ventana
ventana_de_tiquetes.geometry("600x300")
#no expandir su tamaño lo dejamos fijo para que no alteremos el tamaño si se lo quiere expandir ya que no es necesario 
ventana_de_tiquetes.resizable(False, False)

# Crear un marco para el tiquete de abordaje
ventanainterna = tk.Frame(ventana_de_tiquetes, bg="white", bd=2, relief="solid")
ventanainterna.place(relx=0.5, rely=0.5, anchor="center", width=550, height=250)

#con este configuramos el color de fondo pero solo del marco 
ventanainterna.configure(bg="beige")

# Nombre de la aerolínea en el lado izquierdo y configuramos tanto su fondo de color de una parte y su tipo y todo lo demas
mi_primertitulo = tk.Label(ventanainterna, text="✈️" + "\n" + "TU" + "\n" + "TIQUETE" + "\n" + "🛬", fg="white", bg="#000080", font=("Times", 25), anchor="w")
mi_primertitulo.place(relheight=1, width=150)

#esta etiqueta  es para dar un diseño mas bonito a la parte de arriba configuramos su color de fondo a un tamaño indicado y su estructura su color y todo lo demas 
mi_segundotitulo = tk.Label(ventanainterna, text="Viaja Seguro con Bluesky Airlines ✈️", fg="white", bg="#000080", font=("Fixedsys", 14), anchor="w")
mi_segundotitulo.place(x=150, y=0, relwidth=1.0, height=30)

# Ya en esta parte ya es en sus datos personales la fecha el origen y destino y todo lo demas
nombre_pasajero = tk.Label(ventanainterna, text="Nombre Pasajero", fg="black", bg="beige", font=("Arial", 10), anchor="w")
nombre_pasajero.place(x=160, y=50)
nombre_entrada = tk.Label(ventanainterna, text="------", fg="black", bg="beige", font=("Arial", 14), anchor="w")
nombre_entrada.place(x=160, y=70)
#Origen
titulo_de_origen = tk.Label(ventanainterna, text="Origen", fg="black", bg="beige", font=("Arial", 10), anchor="w")
titulo_de_origen.place(x=160, y=110)#aqui como en los demas ubicamos la etiqueta en la ventana con place
origen_entradas = tk.Label(ventanainterna, text="------", fg="black", bg="beige", font=("Arial", 14), anchor="w")
origen_entradas.place(x=160, y=130)

#Destino
titulo_destinos = tk.Label(ventanainterna, text="Destino", fg="black", bg="beige", font=("Arial", 10), anchor="w")
titulo_destinos.place(x=160, y=170)
sudestino_entrada = tk.Label(ventanainterna, text="------", fg="black", bg="beige", font=("Arial", 14), anchor="w")
sudestino_entrada.place(x=160, y=190)

#Su numero de vuelo 
titulo_vuelo = tk.Label(ventanainterna, text="Vuelo", fg="black", bg="beige", font=("Arial", 10), anchor="w")
titulo_vuelo.place(x=360, y=50)
vuelo_entrada = tk.Label(ventanainterna, text="------", fg="black", bg="beige", font=("Arial", 14), anchor="w")
vuelo_entrada.place(x=360, y=70)

#SU fecha de vuelo 
fecha_titulo = tk.Label(ventanainterna, text="Fecha", fg="black", bg="beige", font=("Arial", 10), anchor="w")
fecha_titulo.place(x=360, y=110)
fecha_entrada = tk.Label(ventanainterna, text="------", fg="black", bg="beige", font=("Arial", 14), anchor="w")
fecha_entrada.place(x=360, y=130)

#La  hora
hora_titulo = tk.Label(ventanainterna, text="Hora", fg="black", bg="beige", font=("Arial", 10), anchor="w")
hora_titulo.place(x=360, y=170)
hora_entrada = tk.Label(ventanainterna, text="------", fg="black", bg="beige", font=("Arial", 14), anchor="w")
hora_entrada.place(x=360, y=190)
#Ya con esta imprimimos la ventana para poder mostrar
ventana_de_tiquetes.mainloop()

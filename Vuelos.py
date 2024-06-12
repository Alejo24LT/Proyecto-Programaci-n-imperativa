import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import csv
import calendar 
from datetime import datetime
from tkcalendar import Calendar
from . import busqueda_posicion

# ################
# # with open('DatosVuelos.txt', 'r') as file:
# #     reader = csv.reader(file, delimiter=',')
# #     salida = []
# #     for row in reader:
# #         salida.append(row[7])
# #     print(salida)
    
# ##recuadro 
root = tk.Tk()
root.title("Vuelos")
root.geometry("500x500")
root.config(bg="light blue")
root.resizable(0, 0)
recuadro_datos = tk.Frame(root, bg="light yellow", width=480, height=300)
recuadro_datos.grid(row=0, column=0, padx=10, pady=10)
recuadro_datos.grid_propagate(False)

# def verificacion():
#     if destino_select == destino_select_1:
#         messagebox.showerror("ERROR! ", "El origen y el destino no pueden ser iguales")
#     else:
#         pass
def origen():
    ##Datos de origen del passajero
    ##Menu y opciones
    global destino_select
    destino_select = tk.StringVar(value="Seleccione Origen")
    destino = tk.Menubutton(recuadro_datos, text="Origen", relief="sunken")
    destino_sub = tk.Menu(destino, tearoff=0)
    destino.grid(row=0, column=1, padx=10, pady=10)
    destino.config(menu=destino_sub)
                                    ###OPCIONES
    destino_sub.add_radiobutton(label="Santa Marta", variable=destino_select, value="Santa Marta")
    destino_sub.add_radiobutton(label="Medellín", variable=destino_select, value="Medellín")
    destino_sub.add_radiobutton(label="Cali", variable=destino_select, value="Cali")
    destino_sub.add_radiobutton(label="Cartagena", variable=destino_select, value="Cartagena")
    destino_sub.add_radiobutton(label="Bogotá", variable=destino_select, value="Bogotá")
    mota = tk.Label(recuadro_datos, textvariable=destino_select, bg="light blue", width=15)       ##MUESTRA CIUDAD SELECCIONADA
    mota.grid(row=0, column=2, padx=10, pady=10)
    mota.config(bg="light blue")
    destino.config(menu=destino_sub)
    
    return destino_select

#


def destino():
    global destino_select_1
    destino_select_1 = tk.StringVar(value="Seleccione Destino")
    destino = tk.Menubutton(recuadro_datos, text="Destino", relief="sunken")
    destino_sub = tk.Menu(destino, tearoff=0)
    destino.grid(row=0, column=3, padx=10, pady=10)
    destino.config(menu=destino_sub)
                                    ###OPCIONES
    destino_sub.add_radiobutton(label="Santa Marta", variable=destino_select_1, value="Santa Marta")
    destino_sub.add_radiobutton(label="Medellín", variable=destino_select_1, value="Medellín")
    destino_sub.add_radiobutton(label="Cali", variable=destino_select_1, value="Cali")
    destino_sub.add_radiobutton(label="Cartagena", variable=destino_select_1, value="Cartagena")
    destino_sub.add_radiobutton(label="Bogotá", variable=destino_select_1, value="Bogotá")    
    destino.config(menu=destino_sub)
    destino_seleccionado = tk.Label(recuadro_datos, textvariable=destino_select_1, bg="light blue", width=15)
    destino_seleccionado.grid(row=0, column=4, padx=10, pady=10)            ##Muestra la seleccion del destino 
    
    return destino_select_1
#####################BOTONES Y FUNCIONALIDADES DE LAS FECHAS

dias_validos = [[5, 12, 19, 26],[6, 13, 20, 27]] 
def fecha_viaje():
    try:
        global dia_viaje
        dia_viaje = int(dia_seleccionado.get())
    except ValueError:
        messagebox.showerror("ERROR! ", "Por favor, seleccione un día válido")
        return
    for i in range(len(dias_validos)):
        if dia_viaje in dias_validos[0]:
            messagebox.showinfo("AVISO! ", f"Sea a escogido para viajar el Miercoles: {dia_viaje}")
            break
        elif dia_viaje in dias_validos[1]:
            messagebox.showinfo("AVISO! ", f"Sea a escogido para viajar el Jueves: {dia_viaje}")
            break
    mota = tk.Label(recuadro_datos, text=f"Dia seleccionado\n2024-06-{dia_viaje}", bg="light blue", width=25)       ##MUESTRA CIUDAD SELECCIONADA
    mota.grid(row=10, column=2, padx=10, pady=10)
    def prueba():
        pass
    siguiente_boton = tk.Button(recuadro_datos, text="Siguiente", relief="flat", command=busqueda_posicion)
    siguiente_boton.grid(row=10, column=4, padx=10, pady=10)
    # verificacion()
    
papaleta = tk.Label(recuadro_datos, text=f"Por favor, Selecciona un dia\nPara viajar", bg="light blue", width=25)       ##MUESTRA CIUDAD SELECCIONADA
papaleta.grid(row=3, column=2, padx=10, pady=10)
label_miercoles = tk.Label(recuadro_datos, text="Miércoles")
label_miercoles.grid(row = 5, column=2)  # Coloca el label "Miércoles" en la columna 2, fila 3
label_jueves = tk.Label(recuadro_datos, text="Jueves")
label_jueves.grid(row = 5, column= 3)  # Coloca el label "Jueves" en la columna 3, fila 3

dia_seleccionado = tk.StringVar()

dia_anterior = None             ##Pa q siempre simule un valor 

def seleccionar_dia(event, dia, widget):
    global dia_anterior
    if dia_anterior:
        dia_anterior.config(bg="SystemButtonFace")  # Vuelve la casilla que se quito otra vez blanca
    dia_seleccionado.set(dia)
    widget.config(bg="light blue")  ##Lo pone amarillo si se clickea
    dia_anterior = widget  

for i, lista_dias in enumerate(dias_validos, start=2):              ##i, lista_dias recorre la matriz
    for j, dia in enumerate(lista_dias, start=1):           ##  igual aqui
        dias_1 = tk.Label(recuadro_datos, text=str(dia), width=1, height=1)
        dias_1.bind("<Button-1>", lambda event, dia=dia, widget=dias_1: seleccionar_dia(event, dia, widget))
        dias_1.grid(column=i, row=j+5, padx=5, pady=1)  ##Pone los días a partir de la fila 6 
boton_confirmar_dia = tk.Button(recuadro_datos, text="Confirmar\nFecha", relief="flat", command=fecha_viaje)
boton_confirmar_dia.grid(row=3, column=4, padx=10, pady=10)






destino()
origen()

# Inicia el bucle principal de la aplicación
root.mainloop()



    
    
    
    
    














































    
# vuelos = []
# def vuelos_disponibles():
#     # vuelo_seleccionado = tk.Label(root, text="Select: " )
    
#     with open('DatosVuelos.txt', 'r') as file:
#         for line in file:
#             vuelos.index(line.strip())
#     return vuelos
    
# print(vuelos_disponibles())
# vuelo_seleccionado.bind("<Button-1>", vuelos_disponibles)

# vuelo_seleccionado.pack()
# root.mainloop()


# def destino_ida():
#     destino = tk.Menu(root)
#     # Crear un menú desplegable
#     destinos_libres = tk.Menu(destino, tearoff=0)
        
#     # Agregar opciones al menú desplegable
#     destinos_libres.add_command(label="Cali")
#     destinos_libres.add_command(label="Cartagena")
#     destinos_libres.add_command(label="Bogotá")

#     # Agregar la opción que abrirá el menú desplegable al menú principal
#     destino.add_cascade(label="Opciones", menu=destinos_libres)

#     # Mostrar el menú principal
#     root.config(menu=destino)

# root.mainloop()
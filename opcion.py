import tkinter as tk
from tkinter import messagebox
import csv

# # Función para leer datos de vuelo desde el archivo de texto
# def leer_datos_vuelo(origen, destino, fecha, hora_salida):
#     with open('date_vul.txt', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             if origen == row[6] and destino == row[7] and fecha == row[0] and hora_salida == row[1]:
#                 return row
#     return None

# # Función para mostrar la interfaz de opciones
# def mostrar_opciones(origen, destino, fecha, hora_salida):
#     datos_vuelo = leer_datos_vuelo(origen, destino, fecha, hora_salida)
#     if datos_vuelo:
#         fecha, hora_salida, hora_llegada, costo_aluminio, costo_diamante, costo_premium, _, _ = datos_vuelo
        
        # Crear ventana para opciones de vuelo
tool_opt = tk.Tk()
tool_opt.title("Bluesky Airlines - Selección de Clase")
tool_opt.geometry("1300x600")
tool_opt.resizable(False, False)
        
        # Etiqueta de título
title = tk.Label(tool_opt, text="Selección de Clase de Vuelo", font=("Arial", 18, "bold"), fg="green")
title.pack(pady=10)
        
        # Información de vuelo
info_vuelo = tk.Frame(tool_opt)
info_vuelo.pack(pady=10, padx=20, fill="x")
        
# ida_label = tk.Label(info_vuelo, text=f"Ida: {origen} - {destino}", font=("Arial", 14))
# ida_label.pack(anchor='w')
        
# fecha_label = tk.Label(info_vuelo, text=f"Fecha: {fecha}", font=("Arial", 12))
# fecha_label.pack(anchor='w')
        
# horario_label = tk.Label(info_vuelo, text=f"Horario: {hora_salida} - {hora_llegada}", font=("Arial", 12))
# horario_label.pack(anchor='w')
        
        # Opciones de selección
opcions_clas = tk.Frame(tool_opt)
opcions_clas.pack(pady=10, padx=20, fill="x")
        
def crea_op(frame, titulo, descripcion, costo):
    opcions_t = tk.Frame(frame, bd=2, relief="ridge")
    opcions_t.pack(side="left", padx=10, pady=10, fill="y")
        
    tiltulo = tk.Label(opcions_t, text=titulo, font=("Arial", 12, "bold"))
    tiltulo.pack(pady=5)
        
    descripcion_label = tk.Label(opcions_t, text=descripcion, font=("Arial", 10), justify="left")
    descripcion_label.pack(pady=5)
            
    costo_label = tk.Label(opcions_t, text=f"Costo: {costo} COP", font=("Arial", 10, "bold"))
    costo_label.pack(pady=5)
        
    seleccionar_clas = tk.Button(opcions_t, text="Seleccionar", command=lambda: avanzar_interfaz(tool_opt))
    seleccionar_clas.pack(pady=5)
        
        # Opciones de vuelo
crea_op(opcions_clas, "Aluminio", 
        "1 artículo personal (bolso) (Debe caber debajo del asiento)\n"
        "1 equipaje de mano (10 kg)\n"
        "Equipaje de bodega (23 kg)\n"
        "Asiento Economy (Aleatoria - clasificado Aluminio)\n"
        "Cambios de vuelo (No es permitido)\n"
        "Reembolso (No es permitido)" , "costo_aluminio")
        
crea_op(opcions_clas, "Diamante", 
        "1 artículo personal (bolso) (Debe caber debajo del asiento)\n"
        "1 equipaje de bodega (23 kg) (Debe caber en el compartimiento superior)\n"
        "1 equipaje de mano (10 kg) (Entrega el equipaje en el counter)\n"
        "Asiento Economy (Filas específicas disponibles de manera aleatoria)\n"
        "Cambios de vuelo (No es permitido)\n"
        "Reembolso (No es permitido)" , "costo_diamante")
        
crea_op(opcions_clas, "Premium", 
        "1 artículo personal (bolso) (Debe caber debajo del asiento)\n"
        "1 equipaje de mano (10 kg) (Debe caber en el compartimiento superior)\n"
        "1 equipaje de bodega (23 kg) (Entrega el equipaje en el counter)\n"
        "Asiento Plus (Sujeto a disponibilidad - clasificado Premium)\n"
        "Cambios de vuelo (Sin cargo por cambio, antes del vuelo)\n"
        "Reembolso (No es permitido)", "costo_premium")
        
tool_opt.mainloop()
#     else:
#         messagebox.showerror("Error", "Datos del vuelo no encontrados")

# Función para avanzar a la siguiente interfaz
def avanzar_interfaz(ventana_actual):
    ventana_actual.destroy()
    # Aquí debes agregar el código para abrir la interfaz siguiente que ya tienes creada.
    # Por ejemplo:
    # from siguiente_interfaz import siguiente_interfaz
    # siguiente_interfaz()

# Supongamos que estos 

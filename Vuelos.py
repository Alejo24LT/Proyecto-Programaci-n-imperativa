import tkinter as tk
from tkinter import messagebox
import re
from tkinter import *
import ast
from datetime import datetime
import random
###



vuelo_ventana_principal = tk.Toplevel()
vuelo_ventana_principal.title("Vuelos")
vuelo_ventana_principal.geometry("500x700")
vuelo_ventana_principal.config(bg="light blue")
vuelo_ventana_principal.resizable(0, 0)
recuadro_datos = tk.Frame(vuelo_ventana_principal, bg="light yellow", width=480, height=320)
recuadro_datos.grid(row=0, column=0, padx=10, pady=10)
recuadro_datos.grid_propagate(False)



def origen():
    global destino_select
    destino_select = tk.StringVar(value="Seleccione Origen")
    destino = tk.Menubutton(recuadro_datos, text="Origen", relief="sunken")
    destino_sub = tk.Menu(destino, tearoff=0)
    destino.grid(row=0, column=1, padx=10, pady=10)
    destino.config(menu=destino_sub)
                                    ###OPCIONES
    destino_sub.add_radiobutton(label="Santa Marta", variable=destino_select, value="Santa Marta")
    destino_sub.add_radiobutton(label="Medellin", variable=destino_select, value="Medellin")
    destino_sub.add_radiobutton(label="Cali", variable=destino_select, value="Cali")
    destino_sub.add_radiobutton(label="Cartagena", variable=destino_select, value="Cartagena")
    destino_sub.add_radiobutton(label="Bogota", variable=destino_select, value="Bogota")
    mota = tk.Label(recuadro_datos, textvariable=destino_select, bg="light blue", width=15)       ##MUESTRA CIUDAD SELECCIONADA
    mota.grid(row=0, column=2, padx=10, pady=10)
    mota.config(bg="light blue")
    destino.config(menu=destino_sub)
    
    return destino_select
def destino():

    global destino_select_1
    destino_select_1 = tk.StringVar(value="Seleccione Destino")
    destino = tk.Menubutton(recuadro_datos, text="Destino", relief="sunken")
    destino_sub = tk.Menu(destino, tearoff=0)
    destino.grid(row=0, column=3, padx=10, pady=10)
    destino.config(menu=destino_sub)
                                    ###OPCIONES
    destino_sub.add_radiobutton(label="Santa Marta", variable=destino_select_1, value="Santa Marta")
    destino_sub.add_radiobutton(label="Medellin", variable=destino_select_1, value="Medellin")
    destino_sub.add_radiobutton(label="Cali", variable=destino_select_1, value="Cali")
    destino_sub.add_radiobutton(label="Cartagena", variable=destino_select_1, value="Cartagena")
    destino_sub.add_radiobutton(label="Bogota", variable=destino_select_1, value="Bogota")    
    destino.config(menu=destino_sub)
    destino_seleccionado = tk.Label(recuadro_datos, textvariable=destino_select_1, bg="light blue", width=15)
    destino_seleccionado.grid(row=0, column=4, padx=10, pady=10)      
    

    return destino_select_1


dias_validos = [[5, 12, 19, 26],[6, 13, 20, 27]] 

    
papaleta = tk.Label(recuadro_datos, text=f"Por favor, Selecciona un dia\nPara viajar", bg="light blue", width=25)       ##MUESTRA CIUDAD SELECCIONADA
papaleta.grid(row=5, column=2, padx=10, pady=10)
label_miercoles = tk.Label(recuadro_datos, text="Miércoles")
label_miercoles.grid(row = 6, column=2)  # Coloca el label "Miércoles" en la columna 2, fila 3
label_jueves = tk.Label(recuadro_datos, text="Jueves")
label_jueves.grid(row = 6, column= 3)  # Coloca el label "Jueves" en la columna 3, fila 3

dia_seleccionado = tk.StringVar()

dia_anterior = None             ##Pa q siempre simule un valor 

def seleccionar_dia(event, dia, widget):
    global dia_anterior
    global dia_fijado
    if dia_anterior:
        dia_anterior.config(bg="SystemButtonFace")  # Vuelve la casilla que se quito otra vez blanca
    dia_seleccionado.set(dia)
    widget.config(bg="light blue")  ##Lo pone amarillo si se clickea
    dia_anterior = widget  
    dia_fijado = dia

for i, lista_dias in enumerate(dias_validos, start=2):              ##i, lista_dias recorre la matriz
    for j, dia in enumerate(lista_dias, start=1):           ##  igual aqui
        dias_1 = tk.Label(recuadro_datos, text=str(dia), width=1, height=1)
        dias_1.bind("<Button-1>", lambda event, dia=dia, widget=dias_1: seleccionar_dia(event, dia, widget))
        dias_1.grid(column=i, row=j+6, padx=5, pady=1)  ##Pone los días a partir de la fila 6 
        
def verificacion():
    global origen_fijo, destino_fijo
    if destino_select.get() == "Seleccione Origen" or destino_select_1.get() == "Seleccione Destino":
        messagebox.showerror("ERROR! ", "Por favor, seleccione un origen y un destino")
    elif destino_select.get() == destino_select_1.get():
        messagebox.showerror("ERROR! ", "El origen y el destino no pueden ser iguales")
    else:
        origen_fijo = destino_select.get()
        destino_fijo = destino_select_1.get()
        messagebox.showinfo("AVISO! ", "Se verifico el origen y el destino")
        boton_confirmar_dia.config(state="normal")  # Habilita el botón de confirmar fecha



#####################################################################################
'BUSQUEDA DE VUELOS'
destino()
origen()
def espacio_busqueda():
    global recuadro_busqueda
    recuadro_busqueda = tk.Frame(vuelo_ventana_principal, bg="light yellow", width=480, height=320)
    recuadro_busqueda.grid(row=1, column=0, padx=10, pady=10)
    recuadro_busqueda.grid_propagate(False)
    buscador_vuelos()
    vuelos_disponibles()
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
        mota.grid(row=11, column=2, padx=10, pady=10)
        def prueba():
            pass
        siguiente_boton = tk.Button(recuadro_datos, text="Siguiente", relief="flat", command=espacio_busqueda)   ##Boton siguiente##
        siguiente_boton.grid(row=11, column=4, padx=10, pady=10)


verificacion_boton = tk.Button(recuadro_datos, text="Verificar\nOrigen y Destino", relief="flat", command=verificacion)
verificacion_boton.grid(row=5, column=4, padx=10, pady=10)

boton_confirmar_dia = tk.Button(recuadro_datos, text="Confirmar\nFecha", relief="flat", command=fecha_viaje, state="disabled")
boton_confirmar_dia.grid(row=6, column=4, padx=10, pady=10)


def buscador_vuelos():
    global vuelos_encontrados
    with open('DatosVuelos.txt', 'r') as f:         ##ESTE VUELVE LOS RENGLONES LISTAS
        vuelos = [eval(line.strip().strip("'")) for line in f]


    origen_busqueda = origen_fijo                  ###CIUDAD DE ORIGEN TENER EN CUENTA                  
    destino_busqueda = destino_fijo                     ###CIUDAD DE DESTINO TENER EN CUENTA
    fecha_busqueda = f"2024-06-{dia_fijado}"                    ###FECHA DE VIAJE TENER EN CUENTA
    print(origen_fijo, destino_fijo, fecha_busqueda)
                                                    ##ESTE ES EL QUE BUSCA EN LA LISTA DE LOS VUELOS 
    vuelos_encontrados = [vuelo for vuelo in vuelos if vuelo[1] == fecha_busqueda and vuelo[7] == origen_busqueda and vuelo[8] == destino_busqueda]

    for vuelo in vuelos_encontrados:                ##GUIA DE QUE VUELOS ENCONTRO
        print(vuelo)

silla_seleccionada = None
silla_azar1 = None
user = "premium"                        ####SILLAS Y VUELOS   ###
def todo_sillas(codigo_avion, user):
    global ventana_sillas
    ventana_sillas = tk.Toplevel()
    ventana_sillas.title("Seleccion de sillas")         ##ESTA FUNCION RECIBE EL CODIGO DEL VUELO POR POSICION
    ventana_sillas.geometry("650x600")                     ##Y EL TIPO DEL USUARIO
    label_sillas = tk.Label(ventana_sillas, text="Selecciona tu silla", font=("Georgia", 20, "bold"))
    label_sillas.grid()             
    sillas_diamante_1 = ["A5","A6","A7","A8","B5","B6","B7","B8","C5","C6","C7","C8","D5","D6","D7","D8","E5","E6","E7","E8","F5","F6","F7","F8"]
    sillas_aluminio_1 = ["A9","A10","A11","A12","B9","B10","B11","B12","C9","C10","C11","C12","D9","D10","D11","D12","E9","E10","E11","E12","F9","F10","F11","F12"]

    def sillas_premium(ventana_sillas, codigo_avion):
        sillas_ocupadas = []
        filas_sillas = ["A", "B", "C", "D", "E", "F"]               ###
        archivo_sillas = f"SillasOcupadas_{codigo_avion}.txt"           ##ESTE ES EL CREA UN DOCUMENTO PARA EL VUELOS SINO LO TIENE
        with open(archivo_sillas, "a+") as sillas_txt:                  
            sillas_txt.seek(0)
            sillas_ocupadas = sillas_txt.read().splitlines()
    
        def silla_escogida(sitio, posicion, sillas_aluminio_1, sillas_diamante_1):
            global silla_seleccionada
            sillas_premium1 = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4", "D1", "D2", "D3", "D4", "E1", "E2", "E3", "E4", "F1", "F2", "F3", "F4"]
            if not silla_seleccionada:
                if posicion in sillas_premium1:
                    if posicion in sillas_ocupadas:
                        aviso = tk.Toplevel(ventana_sillas)             
                        aviso.title("Aviso")
                        messagebox.showinfo("Aviso", "La silla ya está ocupada.")
                        print(f"La silla {posicion} ya está ocupada.")
                    else:
                        print(f"Silla escogida: {posicion}")                ##PINTA Y ESCRIBE LA SILLA
                        sitio.config(bg="red")
                        sillas_ocupadas.append(posicion)
                        with open(archivo_sillas, "w") as sillas_txt:
                            for asiento in sillas_ocupadas:
                                sillas_txt.write(f"{asiento}\n")
                        silla_seleccionada = True
            else:
                messagebox.showinfo("Aviso", "Ya has seleccionado una silla esta sesion.")
                
        recuadro_sillas = tk.Frame(ventana_sillas, bg='blue')                          #El marco de los asientos
        recuadro_sillas.grid(row=1, column=2,columnspan=5, padx=5, pady=5)  
            
        for i in range(len(filas_sillas)):                          ##Genera las sillas en el marco
            for j in range(1, 13):
                silla_especifica = f"{filas_sillas[i]}{j}" 
                if j == 1:  
                    sitios = tk.Label(recuadro_sillas, text=silla_especifica, width=1, height=1)
                else:
                    sitios = tk.Label(recuadro_sillas, width=1, height=1)               ##ESTOS DEJAN QUE SE ESCOJA LA SILLA
                sitios.bind("<Button-1>", lambda event, sitio=sitios, posicion=silla_especifica: silla_escogida(sitio, posicion, sillas_aluminio_1, sillas_diamante_1))
                
                if silla_especifica in sillas_ocupadas:
                    sitios.config(bg="red")
                if j <= 3:                                          ##Separa en dos columnas las sillas
                    sitios.grid(row=j-1, column= i, padx=5, pady=5)  
                else:                                                   
                    sitios.grid(row=j+1, column=i, padx=5, pady=5)  
        def paquetes_vuelo():
            recuadro_paquetes = tk.Frame(ventana_sillas, bg='white', highlightbackground='light blue',highlightthickness=2)
                            ###El cuadro que enseña los paquetes
            recuadro_paquetes.grid(row=1, column=0, padx=5, pady=5)
            paquetes = tk.Label(recuadro_paquetes, text="PREMIUM\n\n\n\nDIAMANTE\n\n\n\nALUMINIO", font=("Georgia", 20, "bold"))
            paquetes.pack()
            paquetes.config(bg=recuadro_paquetes.cget('bg'))
        paquetes_vuelo()

    def sillas_diamante(ventana_sillas, codigo_avion, ):
        sillas_ocupadas = []
        filas_sillas = ["A", "B", "C", "D", "E", "F"]
        archivo_sillas = f"SillasOcupadas_{codigo_avion}.txt"
        boton_seleccionar = tk.Button(ventana_sillas, text="Seleccionar silla", command=None)
        with open(archivo_sillas, "a+") as sillas_txt:
            sillas_txt.seek(0)
            sillas_ocupadas = sillas_txt.read().splitlines()
    
        def silla_azar(silla_azar1):
            if not silla_seleccionada:
                if sillas_diamante_1:
                    silla_azar1 = random.choice(sillas_diamante_1)
                    sillas_diamante_1.remove(silla_azar1)
                    return silla_azar1
                else:
                    sin_sillas_diamante = tk.Toplevel(ventana_sillas)
                    sin_sillas_diamante.title("Aviso")
                    texto_nosillas_diamante = tk.Label(sin_sillas_diamante, text="No hay mas sillas disponibles en esta clase!", font=("Georgia", 20, "bold"))
                    texto_nosillas_diamante.pack(pady=20)
    
        def silla_aleatoria_agg(silla_azar1):
            sillas_ocupadas.append(silla_azar1)
            with open(archivo_sillas, "a") as sillas_txt:
                sillas_txt.write(f"{silla_azar1}\n")
    
        def actualizar_sillas(silla_azar1):
            for i in range(len(filas_sillas)):
                for j in range(1, 13):
                    silla_especifica = f"{filas_sillas[i]}{j}"
                    sitios = tk.Label(recuadro_sillas, width=1, height=1)
                    if silla_especifica in sillas_ocupadas:
                        sitios.config(bg="red")
                    if j <= 3:
                        sitios.grid(column=i, row=j-1, padx=5, pady=5)
                    else:
                        sitios.grid(column=i, row=j+1, padx=5, pady=5)
    
        recuadro_sillas = tk.Frame(ventana_sillas, bg='blue')
        recuadro_sillas.grid(row=1, column=2,columnspan=5, padx=5, pady=5)
    
        def seleccionar_silla(silla_azar1):
            global silla_seleccionada
            if not silla_seleccionada:
                boton_seleccionar.config(state=tk.DISABLED)
                silla_azar1 = silla_azar(silla_azar1)
                if silla_azar1 is not None:
                    silla_aleatoria_agg(silla_azar1)
                    actualizar_sillas(silla_azar1)
                    silla_seleccionada = True
            else:
                messagebox.showinfo("Aviso", "Ya has seleccionado una silla esta sesion.")
        boton_seleccionar.config(command=lambda: seleccionar_silla(silla_azar1))
        boton_seleccionar.grid(column=2)
        actualizar_sillas(silla_azar1)
        boton_seleccionar.config(state=tk.NORMAL)
    
        def paquetes_vuelo():
            recuadro_paquetes = tk.Frame(ventana_sillas, bg='white', highlightbackground='light blue',highlightthickness=2)
            recuadro_paquetes.grid(row=1, column=0, padx=5, pady=5)
            paquetes = tk.Label(recuadro_paquetes, text="PREMIUM\n\n\n\nDIAMANTE\n\n\n\nALUMINIO", font=("Georgia", 20, "bold"))
            paquetes.pack()
            paquetes.config(bg=recuadro_paquetes.cget('bg'))
        paquetes_vuelo()

    ##########################################################################################################################################
    #####LO MISMO DE LO DE ARRIBA, SOLO SE CAMBIA EL "RANGO" DE LAS SILLAS Y EL NOMBRE DE LA FUNCION, NO MOVER POR EL PUTAS##################

    def sillas_aluminio(ventana_sillas, codigo_avion):
        global silla_azar1  
        sillas_ocupadas = []
        silla_azar1 = None
        filas_sillas = ["A", "B", "C", "D", "E", "F"]
        boton_seleccionar = tk.Button(ventana_sillas, text="Seleccionar silla", command=None)
        
        # Usamos el código del avión para generar un nombre de archivo único
        nombre_archivo = f"SillasOcupadas_{codigo_avion}.txt"
        
        # Abrimos el archivo en modo 'a+' para que se cree si no existe
        with open(nombre_archivo, "a+") as sillas_txt:
            sillas_txt.seek(0)  # Nos aseguramos de que el cursor esté al principio del archivo
            sillas_ocupadas = sillas_txt.read().splitlines()
        
        # El resto del código sigue igual...
        
        def silla_azar(silla_azar1):
            if sillas_aluminio_1:
                silla_azar1 = random.choice(sillas_aluminio_1)
                sillas_aluminio_1.remove(silla_azar1)
                return silla_azar1
            else:
                sin_sillas_diamante = tk.Toplevel(ventana_sillas)
                sin_sillas_diamante.title("Aviso")
                texto_nosillas_diamante = tk.Label(sin_sillas_diamante, text="No hay mas sillas disponibles en esta clase!", font=("Georgia", 20, "bold"))
                texto_nosillas_diamante.pack(pady=20)
    
        def silla_aleatoria_agg(silla_azar1):
            sillas_ocupadas.append(silla_azar1)
            with open(nombre_archivo, "a") as sillas_txt:
                sillas_txt.write(f"{silla_azar1}\n")
    
        def actualizar_sillas(silla_azar1):
            for i in range(len(filas_sillas)):
                for j in range(1, 13):
                    silla_especifica = f"{filas_sillas[i]}{j}"
                    sitios = tk.Label(recuadro_sillas, width=1, height=1)
                    if silla_especifica in sillas_ocupadas:
                        sitios.config(bg="black")
                    if j <= 3:
                        sitios.grid(column=i, row=j-1, padx=5, pady=5)
                    else:
                        sitios.grid(column=i, row=j+1, padx=5, pady=5)
        recuadro_sillas = tk.Frame(ventana_sillas, bg='light blue')
        recuadro_sillas.grid(row=1, column=2,columnspan=5, padx=5, pady=5)
    
        def seleccionar_silla():
            global silla_azar1  
            boton_seleccionar.config(state=tk.DISABLED)
            silla_azar1 = silla_azar(silla_azar1)
            if silla_azar1 is not None:
                silla_aleatoria_agg(silla_azar1)
                actualizar_sillas(silla_azar1)
        boton_seleccionar.config(command=seleccionar_silla) 
        boton_seleccionar.grid(column=2)
        actualizar_sillas(silla_azar1)
        boton_seleccionar.config(state=tk.NORMAL)
    
        def paquetes_vuelo():
            recuadro_paquetes = tk.Frame(ventana_sillas, bg='white', highlightbackground='light blue',highlightthickness=2)
            recuadro_paquetes.grid(row=1, column=0, padx=5, pady=5)
            paquetes = tk.Label(recuadro_paquetes, text="PREMIUM\n\n\n\nDIAMANTE\n\n\n\nALUMINIO", font=("Georgia", 20, "bold"))
            paquetes.grid()
            paquetes.config(bg=recuadro_paquetes.cget('bg'))
        paquetes_vuelo()
    if user == "premium":
        sillas_premium(ventana_sillas, codigo_avion)
    elif user == "diamante":
        sillas_diamante(ventana_sillas, codigo_avion)
    elif user == "aluminio":
        sillas_aluminio(ventana_sillas, codigo_avion)
    ventana_sillas.mainloop()
    

def seleccionar_vuelo(vuelo):
    global costo_aluminio, costo_diamante, coste_premium
    codigo_avion = vuelo[0]
    fecha = vuelo[1]
    hora_salida = vuelo[2]              ##DA LOS VALORES DEL VUEJO QUE SE ESCOJA
    hora_llegada = vuelo[3]
    costo_aluminio = vuelo[4]
    costo_diamante = vuelo[5]
    coste_premium = vuelo[6]
    todo_sillas(codigo_avion, user)

    seleccionar_vuelo_completo(vuelo)

    
   # Inicializar tkinter solo una vez
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Variables globales (si es necesario)
def mostrar_interfaz_opciones():
    # Definir los costos
    costo_aluminio = 100  # Define el costo real
    costo_diamante = 200  # Define el costo real
    coste_premium = 300  # Define el costo real

    # Crear ventana para opciones de vuelo
    vent_clas = tk.Toplevel(root)
    vent_clas.title("Bluesky Airlines - Selección de Clase")
    vent_clas.geometry("1300x600")
    vent_clas.resizable(0, 0)

    # Etiqueta de título
    title = tk.Label(vent_clas, text="Selección de Clase de Vuelo", font=("Arial", 18, "bold"), fg="green")
    title.pack(pady=10)

    # Opciones de selección
    opciones_frame = tk.Frame(vent_clas)
    opciones_frame.pack(pady=10, padx=20, fill="both", expand=True)

    def opcion_alum(frame, titulo, descripcion, costo):
        opcion1 = tk.Frame(frame, bd=2, relief="ridge")
        opcion1.pack(side="left", padx=10, pady=10, fill="both", expand=True)

        titulo_lab = tk.Label(opcion1, text=titulo, font=("Arial", 12, "bold"))
        titulo_lab.pack(pady=5)

        descipto_a = tk.Label(opcion1, text=descripcion, font=("Arial", 10), justify="left")
        descipto_a.pack(pady=5)
        
        cost_al = tk.Label(opcion1, text=f"Costo Total: {costo} COP", font=("Arial", 10, "bold"))
        cost_al.pack(pady=5)

        slect_m = tk.Button(opcion1, text="Seleccionar", command=lambda: select_alum(costo))
        slect_m.pack(pady=5)

    def opcion_diamant(frame, titulo, descripcion, costo):
        opcion_2 = tk.Frame(frame, bd=2, relief="ridge")
        opcion_2.pack(side="left", padx=10, pady=10, fill="both", expand=True)

        tit_d = tk.Label(opcion_2, text=titulo, font=("Arial", 12, "bold"))
        tit_d.pack(pady=5)

        describ_dia = tk.Label(opcion_2, text=descripcion, font=("Arial", 10), justify="left")
        describ_dia.pack(pady=5)
        
        cost_diam = tk.Label(opcion_2, text=f"Costo Total: {costo} COP", font=("Arial", 10, "bold"))
        cost_diam.pack(pady=5)

        selec_ant = tk.Button(opcion_2, text="Seleccionar", command=lambda: select_diamant(costo))
        selec_ant.pack(pady=5)

    def opcion_premi(frame, titulo, descripcion, costo):
        opcion3 = tk.Frame(frame, bd=2, relief="ridge")
        opcion3.pack(side="left", padx=10, pady=10, fill="both", expand=True)

        tiltre = tk.Label(opcion3, text=titulo, font=("Arial", 12, "bold"))
        tiltre.pack(pady=5)

        desc_pre = tk.Label(opcion3, text=descripcion, font=("Arial", 10), justify="left")
        desc_pre.pack(pady=5)
        
        cost_mium = tk.Label(opcion3, text=f"Costo Total: {costo} COP", font=("Arial", 10, "bold"))
        cost_mium.pack(pady=5)

        select_pmu = tk.Button(opcion3, text="Seleccionar", command=lambda: select_premi(costo))
        select_pmu.pack(pady=5)

    # Funciones específicas para cada costo
    def select_alum(costo):
        user1 = "aluminio"
        messagebox.showinfo("Seleccionado", f"Clase de vuelo {user1} seleccionada con costo {costo} COP")

    def select_diamant(costo):
        user2 = "diamante"
        messagebox.showinfo("Seleccionado", f"Clase de vuelo {user2} seleccionada con costo {costo} COP")

    def select_premi(costo):
        user3 = "premium"
        messagebox.showinfo("Seleccionado", f"Clase de vuelo {user3} seleccionada con costo {costo} COP")

    # Opciones de vuelo
    opcion_alum(opciones_frame, "Aluminio", 
        "1 artículo personal (bolso) (Debe caber debajo del asiento)\n"
        "1 equipaje de mano (10 kg)\n"
        "Equipaje de bodega (23 kg)\n"
        "Asiento Economy (Aleatoria - clasificado Aluminio)\n"
        "Cambios de vuelo (No es permitido)\n"
        "Reembolso (No es permitido)", costo_aluminio)

    opcion_diamant(opciones_frame, "Diamante", 
        "1 artículo personal (bolso) (Debe caber debajo del asiento)\n"
        "1 equipaje de bodega (23 kg) (Debe caber en el compartimiento superior)\n"
        "1 equipaje de mano (10 kg) (Entrega el equipaje en el counter)\n"
        "Asiento Economy (Filas específicas disponibles de manera aleatoria)\n"
        "Cambios de vuelo (No es permitido)\n"
        "Reembolso (No es permitido)", costo_diamante)

    opcion_premi(opciones_frame, "Premium", 
        "1 artículo personal (bolso) (Debe caber debajo del asiento)\n"
        "1 equipaje de mano (10 kg) (Debe caber en el compartimiento superior)\n"
        "1 equipaje de bodega (23 kg) (Entrega el equipaje en el counter)\n"
        "Asiento Plus (Sujeto a disponibilidad - clasificado Premium)\n"
        "Cambios de vuelo (Sin cargo por cambio, antes del vuelo)\n"
        "Reembolso (No es permitido)", coste_premium)

def vuelos_disponibles():
    global vuelos_encontrados
    recuadro_busqueda = tk.Toplevel(root)
    recuadro_busqueda.title("Vuelos Disponibles")
    recuadro_busqueda.geometry("800x600")

    seleccionar_vuelo_label = tk.Label(recuadro_busqueda, text="Seleccione un vuelo: ")
    seleccionar_vuelo_label.grid(row=0, column=0, padx=10, pady=10)
    
    if vuelos_encontrados:
        for i, vuelo in enumerate(vuelos_encontrados):
            vuelo_seleccionado = tk.Button(recuadro_busqueda, text=f"Vuelo encontrado: {vuelo[0]} Hora Salida: {vuelo[2]}\nHora Llegada: {vuelo[3]} Fecha: {vuelo[1]}", relief="flat",  highlightbackground="light blue", highlightthickness=2)
            vuelo_seleccionado.grid(row=i+1, column=0, padx=10, pady=10)
            buton_nv = tk.Button(recuadro_busqueda, text="Seleccionar", command=mostrar_interfaz_opciones)
            buton_nv.grid(row=i+1, column=1, padx=10, pady=10)
    else:
        messagebox.showinfo("DISCULPA","No se encontraron vuelos.")

# Ejemplo de cómo llamar a vuelos_disponibles (esto sería parte de otra función en tu programa)
vuelos_disponibles()

# Iniciar el loop principal
root.mainloop()

def seleccionar_vuelo_completo(vuelo):
    print(vuelo)                    ##SIMPLE GUIA NO HACE NADA
    
def abrir_ventana():
    origen()
    destino()                   ## FUNCION QUE SE IMPORTA EN USUARIO PARA EJECUTAR BIEN 
    vuelo_ventana_principal.mainloop()


def precios_paquetes():
    pass

def boton_tiquete(tiquete):
    boton_boleto = tk.Button(ventana_sillas, text="Generar Boleto", command=tiquete)
    boton_boleto.grid(column=2, row=2, padx=5, pady=5)





# Función para avanzar a la siguiente interfaz





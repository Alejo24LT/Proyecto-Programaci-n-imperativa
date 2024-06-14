import tkinter as tk

# Variables globales para los costos iniciales
costo_aluminio = 1000
costo_diamante = 0.9
costo_premium = 0.0000

# Función para actualizar los costos
def actualizar_costos(c_aluminio, c_diamante, c_premium):
    global costo_aluminio, costo_diamante, costo_premium
    costo_aluminio = c_aluminio
    costo_diamante = c_diamante
    costo_premium = c_premium

# Función para avanzar a la siguiente interfaz
def nueva_inter2(ventana_actual, clase, costo):
    # ventana_actual.destroy()
    # Aquí puedes agregar el código para abrir la interfaz siguiente que ya tienes creada.
    # Por ejemplo, si se llama `siguiente_interfaz.py`:
    # from siguiente_interfaz import siguiente_interfaz
    # siguiente_interfaz(clase, costo)

    # Ejemplo de abrir una nueva ventana con la selección
    nueva_ventana = tk.Toplevel(ventana_actual)
    nueva_ventana.title("Confirmación de Selección")
    nueva_ventana.geometry("400x200")

    confirmacion_label = tk.Label(nueva_ventana, text=f"Clase seleccionada: {clase}\nCosto: {costo} COP", font=("Arial", 12))
    confirmacion_label.pack(pady=20)

    nueva_ventana.mainloop()

# Función para mostrar la interfaz de opciones de vuelo
def mostrar_interfaz_opciones():
    global costo_aluminio, costo_diamante, costo_premium
    
    # Crear ventana para opciones de vuelo
    vent_clas = tk.Tk()
    vent_clas.title("Bluesky Airlines - Selección de Clase")
    vent_clas.geometry("800x600")

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
        nueva_inter2(vent_clas, "Aluminio", costo)

    def select_diamant(costo):
        nueva_inter2(vent_clas, "Diamante", costo)

    def select_premi(costo):
        nueva_inter2(vent_clas, "Premium", costo)

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
        "Reembolso (No es permitido)", costo_premium)

    vent_clas.mainloop()

mostrar_interfaz_opciones()



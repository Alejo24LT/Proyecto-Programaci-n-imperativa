import tkinter as tk
from tkinter import StringVar, LEFT, ttk

# Función de validación para el número de tarjeta
def validar_numero_tarjeta(texto):
    try:
        if len(texto) > 16:
            return False
        if not texto.isdigit():
            return False
        if len(texto) > 0 and texto[0] != '1':
            raise ValueError("El número de tarjeta debe comenzar con 1")
        return True
    except ValueError as e:
        print(e)
        return False

# Función de validación para el CVV (3 dígitos)
def validar_cvv(texto):
    if len(texto) > 3 or not texto.isdigit():
        return False
    return True

# Función para abrir la segunda interfaz
def abrir_interfaz_2():
    ventan.destroy()  # Cierra la primera ventana
    ventana_2 = tk.Tk()
    ventana_2.title("Confirmación de Pago")
    ventana_2.geometry("400x300")
    
    # Etiqueta de confirmación
    label = tk.Label(ventana_2, text="¡Pago realizado con éxito!", font=("Arial", 16, "bold"), fg="green")
    label.pack(pady=50)
    
    # Botón para cerrar la segunda ventana
    cerrar_button = tk.Button(ventana_2, text="Cerrar", command=ventana_2.destroy)
    cerrar_button.pack(pady=20)
    
    ventana_2.mainloop()

# Configuración de la aplicación
ventan = tk.Tk()
ventan.title("Bluesky Airlines")
ventan.geometry("400x450")

# Etiqueta de título
title = tk.Label(ventan, text="Welcome to Bluesky Airlines", font=("Arial", 16, "bold"), fg="blue")
title.pack(pady=10)

# Submarco para los datos de la tarjeta
card = tk.Frame(ventan, bd=2, relief="ridge")
card.pack(pady=10, padx=20, fill="x")

card_label = tk.Label(card, text="Datos de la tarjeta", font=("Arial", 14, "bold"))
card_label.pack(pady=10)

# Nombre del titular
hold = tk.Label(card, text="Nombre del titular")
hold.pack(pady=5, padx=10, anchor='w')

card_holder_entry = tk.Entry(card)
card_holder_entry.pack(pady=5, padx=10)

# Número de tarjeta
number_card = tk.Label(card, text="Number of the card")
number_card.pack(pady=5, padx=10, anchor='w')

card_number_var = StringVar()
card_number_entry = tk.Entry(card, textvariable=card_number_var)
card_number_entry.pack(pady=5, padx=10)

# Registrar la función de validación
validate_command = (ventan.register(validar_numero_tarjeta), "%P")
card_number_entry.config(validate="key", validatecommand=validate_command)

expiry_date_frame = tk.Frame(card)
expiry_date_frame.pack(pady=5, padx=10, fill="x")

# Fecha de Expiración
expiry_label = tk.Label(expiry_date_frame, text="Expiration Date")
expiry_label.pack(pady=5, padx=10, anchor='w')

# Opciones para el mes
meses = ["07", "08"]
mes_var = StringVar()
expir_men = ttk.Combobox(expiry_date_frame, textvariable=mes_var, values=meses)
expir_men.pack(side=LEFT, padx=(0, 5))

# Opciones para el año
años_d = ["2024"]
año_s = StringVar()
expiry_yearme = ttk.Combobox(expiry_date_frame, textvariable=año_s, values=años_d)
expiry_yearme.pack(side=LEFT, padx=(0, 5))

# CVV
cvv_lab = tk.Label(expiry_date_frame, text="CVV")
cvv_lab.pack(pady=5, padx=10, anchor='w')

cvv_c = StringVar()
entry_cvv = tk.Entry(expiry_date_frame, textvariable=cvv_c, width=6)

# Registrar la función de validación para el CVV
validate_command_cvv = (ventan.register(validar_cvv), "%P")
entry_cvv.config(validate="key", validatecommand=validate_command_cvv)
entry_cvv.pack(side=LEFT)

# Botón de pago
pay_button = tk.Button(ventan, text="Pagar", command=abrir_interfaz_2)
pay_button.pack(pady=20, padx=10)

# Iniciar la aplicación
ventan.mainloop()












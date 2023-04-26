import random
import string
import tkinter as tk


def generar_contrasena():
    longitud = 12
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena


def generar_contrasena_y_mostrar():
    contrasena = generar_contrasena()
    contrasena_label.config(text=contrasena)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de contraseñas")

# Crear los widgets de la ventana
titulo_label = tk.Label(ventana, text="Generador de contraseñas", font=("Arial", 16))
generar_boton = tk.Button(ventana, text="Generar contraseña", command=generar_contrasena_y_mostrar)
contrasena_label = tk.Label(ventana, text="", font=("Arial", 14), fg="red")

# Colocar los widgets en la ventana
titulo_label.pack(pady=20)
generar_boton.pack(pady=10)
contrasena_label.pack()

# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()

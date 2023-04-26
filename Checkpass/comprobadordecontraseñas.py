from tkinter import *

def es_contrasena_segura(contrasena):
    if len(contrasena) < 8:
        return False
    if not any(char.isdigit() for char in contrasena):
        return False
    if not any(char.isupper() for char in contrasena):
        return False
    if not any(char.islower() for char in contrasena):
        return False
    if not any(char in ['$','#','@'] for char in contrasena):
        return False
    return True

def verificar_contrasena():
    contrasena = entrada_contrasena.get()
    if es_contrasena_segura(contrasena):
        resultado.config(text="La contraseña es segura")
    else:
        resultado.config(text="La contraseña no cumple con los criterios de seguridad")

# Crea la ventana principal
ventana = Tk()
ventana.title("Verificador de contraseña")

# Crea los widgets de la ventana
etiqueta_contrasena = Label(ventana, text="Ingresa tu contraseña:")
entrada_contrasena = Entry(ventana, show="*")
boton_verificar = Button(ventana, text="Verificar", command=verificar_contrasena)
resultado = Label(ventana, text="")

# Coloca los widgets en la ventana
etiqueta_contrasena.pack()
entrada_contrasena.pack()
boton_verificar.pack()
resultado.pack()

# Ejecuta el bucle principal de la interfaz gráfica
ventana.mainloop()

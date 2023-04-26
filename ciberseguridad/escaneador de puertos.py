from tkinter import *
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr1

def escanear_puertos():
    ip = entrada_ip.get()
    resultado.delete('1.0', END)
    for port in range(1, 100):
        packet = IP(dst=ip)/TCP(dport=port, flags='S')
        response = sr1(packet, timeout=1, verbose=0)
        if response:
            if response[TCP].flags == 'SA':
                resultado.insert(END, "Puerto " + str(port) + " abierto\n")
            else:
                resultado.insert(END, "Puerto " + str(port) + " cerrado\n")

# Crea la ventana principal
ventana = Tk()
ventana.title("Escaneo de puertos")

# Crea los widgets de la ventana
etiqueta_ip = Label(ventana, text="Introduce la dirección IP a escanear:")
entrada_ip = Entry(ventana)
boton_escanear = Button(ventana, text="Escanear", command=escanear_puertos)
resultado = Text(ventana)

# Coloca los widgets en la ventana
etiqueta_ip.pack()
entrada_ip.pack()
boton_escanear.pack()
resultado.pack()

# Ejecuta el bucle principal de la interfaz gráfica
ventana.mainloop()

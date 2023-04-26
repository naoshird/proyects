import tkinter as tk

# Declaración de las variables del programa
DINERO_INICIAL = 0
total = 0
pedido = []

margarita = 7.85
jamon_queso = 9.65
cuatro_quesos = 8.95

extra_queso = 1.25
champinones = 0.85
albahaca = 0.5

# Función para calcular la pizza seleccionada
def calcular_pizza(eleccion):
    global dinero, total, pedido
    if eleccion == 1:
        pizza = "Margarita"
        precio = margarita
    elif eleccion == 2:
        pizza = "Jamón y queso"
        precio = jamon_queso
    elif eleccion == 3:
        pizza = "Cuatro quesos"
        precio = cuatro_quesos
    dinero -= precio
    total += precio
    pedido.append(f"{pizza} - {precio}$")
    pizza_seleccionada.set(f"Pizza seleccionada: {pizza} - {precio}$")
    dinero_label.set(f"Dinero restante: {round(dinero,2)}$")
    total_label.set(f"Total a pagar: {total}$")

# Función para calcular el ingrediente extra seleccionado
def calcular_ingrediente_extra(eleccion):
    global dinero, total, pedido
    if eleccion == 1:
        ingrediente = "Extra de queso"
        precio = extra_queso
    elif eleccion == 2:
        ingrediente = "Champiñones"
        precio = champinones
    elif eleccion == 3:
        ingrediente = "Albahaca"
        precio = albahaca
    else:
        ingrediente = "Nada extra"
        precio = 0
    dinero -= precio
    total += precio
    pedido.append(f"{ingrediente} - {precio}$")
    ingrediente_extra_seleccionado.set(f"Ingrediente extra seleccionado: {ingrediente} - {precio}$")
    dinero_label.set(f"Dinero restante: {round(dinero,2)}$")
    total_label.set(f"Total a pagar: {total}$")
    
# Función para imprimir el ticket de pedido
def imprimir_ticket():
    global dinero, total, pedido
    if total <= DINERO_INICIAL:
        ticket = f"\n--- SU PEDIDO ---\nEl total de su pedido es: {total}$. Su cambio: {dinero}$."
        for i in pedido:
            ticket += f"\n-{i}."
        ticket += "\n¡Buen provecho!"
        ticket_label.set(ticket)
    else:
        ticket_label.set("No le llega el dinero para realizar el pedido.")
        
# Crear la ventana principal
root = tk.Tk()
root.title("Pizzería PF")

# Crear los marcos para la interfaz
pizza_frame = tk.LabelFrame(root, text="Selección de pizza")
pizza_frame.pack(padx=10, pady=10, fill="both", expand="True")
ingrediente_frame = tk.LabelFrame(root, text="Selección de ingredientes extra")
ticket_frame = tk.LabelFrame(root, text="Ticket de pedido", padx=10, pady=10)
ticket_frame = tk.LabelFrame(root, text="Ticket de pedido")



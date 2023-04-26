import tkinter as tk
import openai

# Aquí debería establecer su clave de API de OpenAI directamente
openai.api_key = "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"

model_engine = "text-davinci-002"
prompt = "Hello, how are you?"

def get_response():
    # Obtener la respuesta del usuario
    user_input = user_input_entry.get()

    # Concatenar la entrada del usuario con la prompt
    prompt_with_user_input = f"{prompt} {user_input}"

    # Generar respuesta con OpenAI API
    completions = openai.Completion.create(engine=model_engine, prompt=prompt_with_user_input, max_tokens=100)
    message = completions.choices[0].text

    # Mostrar respuesta en la interfaz gráfica
    response_label.config(text=message)

# Crear ventana
window = tk.Tk()
window.title("Chatbot")

# Crear entrada de usuario
user_input_label = tk.Label(window, text="You:")
user_input_label.pack()
user_input_entry = tk.Entry(window)
user_input_entry.pack()

# Crear botón para enviar la entrada del usuario
submit_button = tk.Button(window, text="Send", command=get_response)
submit_button.pack()

# Crear etiqueta para mostrar la respuesta
response_label = tk.Label(window, text="Chatbot:")
response_label.pack()

# Iniciar ventana
window.mainloop()

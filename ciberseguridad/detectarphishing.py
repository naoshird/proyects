import tkinter as tk
from tkinter import ttk
import nltk
import re
import urllib.request
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Descarga los datos de entrenamiento
urllib.request.urlretrieve("https://archive.ics.uci.edu/ml/machine-learning-databases/00327/Training%20Dataset.arff", "phishing.csv")

# Lee los datos de entrenamiento
data = []
with open("phishing.csv", "r") as file:
    for line in file:
        data.append(line.strip().split(","))

# Preprocesa los datos de entrenamiento
for i in range(len(data)):
    data[i][0] = re.sub(r"https?://[^\s]+", "", data[i][0])  # Elimina URLs
    data[i][0] = BeautifulSoup(data[i][0], "lxml").text  # Elimina etiquetas HTML
    data[i][0] = data[i][0].lower()  # Convierte a minúsculas

# Divide los datos de entrenamiento en características y etiquetas
X_train = [d[0] for d in data]
import re
y_train = [int(re.search(r'\d+', d[1]).group()) if len(d) > 1 else 0 for d in data]

# Crea un modelo de clasificación de Naive Bayes
vectorizer = CountVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)
clf = MultinomialNB()
clf.fit(X_train_vectors, y_train)

# Define una función para detectar correos electrónicos de phishing
def detectar_phishing(correo):
    correo = re.sub(r"https?://[^\s]+", "", correo)  # Elimina URLs
    correo = BeautifulSoup(correo, "lxml").text  # Elimina etiquetas HTML
    correo = correo.lower()  # Convierte a minúsculas
    correo_vector = vectorizer.transform([correo])
    resultado = clf.predict(correo_vector)
    if resultado[0] == 1:
        return "Este correo electrónico podría ser phishing"
    else:
        return "Este correo electrónico es legítimo"

# Crea la ventana
ventana = tk.Tk()
ventana.title("Detector de phishing")

# Crea la etiqueta de instrucción
instruccion = ttk.Label(ventana, text="Ingresa el correo electrónico a verificar:")
instruccion.pack()

# Crea la entrada de texto
entrada = ttk.Entry(ventana)
entrada.pack()

# Crea la etiqueta de resultado
resultado = ttk.Label(ventana, text="")
resultado.pack()

# Define la función para verificar el correo electrónico
def verificar():
    correo = entrada.get()
    resultado.configure(text=detectar_phishing(correo))

# Crea el botón de verificación
boton = ttk.Button(ventana, text="Verificar", command=verificar)
boton.pack()

# Función para detener el programa
def detener():
    ventana.after(3000, ventana.destroy)

# Agrega un botón para detener el programa
detener = ttk.Button(ventana, text="Cerrar", command=detener)
detener.pack()

# Ejecuta la ventana
ventana.mainloop()

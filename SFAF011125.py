import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
# -------- CONFIGURACIÓN DE COLORES Y FUENTE --------
COLOR_FONDO = "#747AE8"
COLOR_MENU = "#7690CC"
COLOR_TEXTO = "#FFFFFF"
FUENTE_TITULO = ("Arial", 16, "bold")
FUENTE_TEXTO = ("Arial", 12)

# -------- VENTANA PRINCIPAL --------
root = tk.Tk()
root.title("Bienestar Total")
root.geometry("900x500")
root.config(bg=COLOR_FONDO)

# -------- FRAME MENÚ LATERAL --------
menu_frame = tk.Frame(root, bg=COLOR_MENU, width=200)
menu_frame.pack(side="left", fill="y")

# -------- FRAME CONTENIDO --------
contenido_frame = tk.Frame(root, bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)

# -------- FUNCIÓN PARA CAMBIAR DE PÁGINA --------
def mostrar_pagina(nombre):
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    paginas[nombre]()

# -------- PÁGINAS --------
def pagina_bienvenida():
    tk.Label(contenido_frame, text="📸 Bienvenido al software de detecció de adicción a tomar fotografías 📸", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=30)
    tk.Label(contenido_frame, text="Este test tiene como propósito evaluar los niveles de dependencia  o \n adicción a tomar fotografías, permitiendo reconocer si esta práctica se realiza por gusto,\n necesidad o hábito.Los resultados servirán para fomentar el autocontrol  y el uso responsable de la tecnología.", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=10)
# Imagen de bienvenida
try:
    imagen = PhotoImage(file="descarga.png")
    img_label = tk.Label(contenido_frame, image=imagen, bg="#7690CC")
    img_label.pack(pady=10)
except Exception:
    aviso = tk.Label(contenido_frame, text="La imagen no se encontró", bg="#7690CC", fg="gray")
    aviso.pack()

def pagina_registro():
    tk.Label(contenido_frame, text="📝 Registro de Usuario", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    for campo in ["Nombre", "Edad", "Correo electronico"]:
        tk.Label(contenido_frame, text=f"{campo}:", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack()
        tk.Entry(contenido_frame, width=40).pack(pady=5)

def pagina_test():
    tk.Label(contenido_frame, text="💗 Test de Bienestar", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame, text="Responde las siguientes preguntas para conocer tu nivel de bienestar.",
             wraplength=600, bg=COLOR_FONDO).pack(pady=10)
    tk.Button(contenido_frame, text="Iniciar Test").pack(pady=20)

# -------- DICCIONARIO DE PÁGINAS --------
paginas = {
    "Bienvenida": pagina_bienvenida,
    "Registro": pagina_registro,
    "Test": pagina_test,
}

# -------- BOTONES DE MENÚ LATERAL --------
for nombre in paginas:
    ttk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina(n)).pack(fill="x", pady=5, padx=10)

ttk.Button(menu_frame, text="Salir", command=root.quit).pack(side="bottom", pady=10)

# -------- MOSTRAR PÁGINA INICIAL --------
pagina_bienvenida()

root.mainloop()
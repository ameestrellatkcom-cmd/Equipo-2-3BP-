import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

# -----------------------------
# Funciones de las ventanas
# -----------------------------

# Botón invitado: muestra advertencia
def advertencia_invitado():
    messagebox.showwarning(
        "Advertencia - Modo Invitado",
        "⚠️ Al registrarte como invitado, tus respuestas no se guardarán y no recibirás resultados personalizados.\n"
        "Se recomienda registrarse con un usuario para obtener recomendaciones completas."
    )

# Botón iniciar test normal
def iniciar_test():
    messagebox.showinfo("Registro", "Bienvenido al test de adicciones a tomar fotografías")
    ventanabienv.destroy()  # Cierra la ventana de bienvenida
    # Aquí iría la función para abrir la ventana del test
    print("Abrir ventana de Registro...")  

# -----------------------------
# Ventana de bienvenida
# -----------------------------
ventanabienv = tk.Tk()
ventanabienv.title("Software para detectar adicciones a tomar fotografías")
ventanabienv.config(bg="#3F779D")

# Centrar la ventana en la pantalla
ancho_ventana = 700
alto_ventana = 450
ancho_pantalla = ventanabienv.winfo_screenwidth()
alto_pantalla = ventanabienv.winfo_screenheight()
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)
ventanabienv.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Título de bienvenida
titulo = tk.Label(
    ventanabienv,
    text="BIENVENIDO A MI SOFTWARE DE DETECCIÓN DE ADICCIÓN A TOMAR FOTOGRAFÍAS",
    font=("Arial", 18, "bold"),
    bg="#080708",
    fg="#FAF0FA",
    wraplength=650,
    justify="center",
)
titulo.pack(pady=30)

# Imagen de bienvenida
try:
    imagen = PhotoImage(file="descarga.png")
    img_label = tk.Label(ventanabienv, image=imagen, bg="#7690CC")
    img_label.pack(pady=10)
except Exception:
    aviso = tk.Label(ventanabienv, text="La imagen no se encontró", bg="#7690CC", fg="gray")
    aviso.pack()

# Texto descriptivo
texto = tk.Label(
    ventanabienv,
    text="Este test tiene como proposito evaluar los niveles de dependencia o adiccion a tomar fotografías, permitiendo reconocer si esta practica se realiza por gusto, necesidad o habito. los resultados serviran para fomentar el autocontrol y el uso responsable de la tecnología",
    font=("Arial", 12),
    bg="#7690CC",
    fg="#CEDBF2",
    wraplength=500,
    justify="center",
)
texto.pack(pady=20)

# Botón para iniciar el test
boton_iniciar = tk.Button(
    ventanabienv,
    text="Inicio TEST",
    font=("Arial", 14, "bold"),
    bg="#164A69",
    fg="white",
    relief="raised",
    bd=3,
    padx=20,
    pady=10,
    command=iniciar_test
)
boton_iniciar.pack(side="right", padx=50)

# Botón para ingresar como invitado (solo muestra advertencia)
boton_invitado = tk.Button(
    ventanabienv,
    text="Ingresar como Invitado",
    font=("Arial", 14, "bold"),
    bg="#164A69",
    fg="white",
    relief="raised",
    bd=3,
    padx=20,
    pady=10,
    command=advertencia_invitado
)
boton_invitado.pack(side="left", padx=50)

# Ejecutar la ventana de bienvenida
ventanabienv.mainloop()

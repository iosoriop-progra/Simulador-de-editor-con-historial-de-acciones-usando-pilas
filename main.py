"Achivo: main.py"
#Parte visual del proyecto, su interfaz Gráfica

import tkinter as tk
from tkinter import ttk, messagebox
from editor import TextEditor

class EditorGrafico:
    def __init__(self, root):
        self.root = root
        self.root.title("Ingeniería Proyecto de un editor de Texto ")
        self.root.geometry("750x680")
        self.root.configure(bg="#DFECFA") 

        # Instancia de la lógica (Paso B)
        self.editor_logica = TextEditor()
        
        # El estilo de la pantalla
        self.fuente_principal = ("Century Gothic", 11)
        self.fuente_titulo = ("Century Gothic", 16, "bold")
        self.fuente_mono = ("Consolas", 12) # Para el área de texto
        
        # Paleta de Colores Pastel
        self.AZUL_PASTEL = "#A2D2FF"
        self.AMARILLO_PASTEL = "#FEF9E7"
        self.VERDE_LIMON_PASTEL = "#E8F8F5"
        self.ROJO_PASTEL = "#FADBD8"
        self.GRIS_OSCURO = "#2C3E50"

        # 1. Construir la estructura visual
        self._crear_interfaz()
        
        #  Inicializar la pantalla al arrancar
        self.actualizar_pantalla()

    def _crear_interfaz(self):
        """Define la disposición de los elementos en la ventana."""
        
        main_frame = tk.Frame(self.root, bg="#F0F4F8", padx=25, pady=20)
        main_frame.pack(expand=True, fill="both")

        # ENCABEZADO
        header = tk.Label(main_frame, text="EDITOR DE TEXTO (Isabel Osorio 2890-23-12261)", 
                          font=self.fuente_titulo, bg="#F0F4F8", fg=self.GRIS_OSCURO)
        header.pack(pady=(0, 20))

        # Aqui se va a ingresar el texto
        tk.Label(main_frame, text="Escribe aquí:", font=self.fuente_principal, 
                 bg="#F0F4F8", fg=self.GRIS_OSCURO).pack(anchor="w")
        
        self.input_text = tk.Entry(main_frame, font=self.fuente_principal, 
                                   bg="white", relief="flat", highlightthickness=1)
        self.input_text.config(highlightbackground="#D5DBDB", highlightcolor=self.AZUL_PASTEL)
        self.input_text.pack(fill="x", ipady=10, pady=(5, 15))
        self.input_text.bind("<Return>", lambda e: self.ejecutar_escritura())

        #Los botones estan aquí
        btn_frame = tk.Frame(main_frame, bg="#F0F4F8")
        btn_frame.pack(fill="x", pady=5)

        #Darle confiduracion pa que funcionen
        btn_config = {"relief": "flat", "font": self.fuente_principal, "cursor": "hand2", "padx": 10}

        self.btn_write = tk.Button(btn_frame, text="Agregar Texto", bg=self.VERDE_LIMON_PASTEL,
                                  command=self.ejecutar_escritura, **btn_config)
        self.btn_write.pack(side="left", padx=5)

        self.btn_undo = tk.Button(btn_frame, text="⟲ Deshacer", bg=self.AZUL_PASTEL,
                                 command=self.ejecutar_undo, **btn_config)
        self.btn_undo.pack(side="left", padx=5)

        self.btn_redo = tk.Button(btn_frame, text="⟳ Rehacer", bg=self.AMARILLO_PASTEL,
                                 command=self.ejecutar_redo, **btn_config)
        self.btn_redo.pack(side="left", padx=5)

        # Sección de borrado
        tk.Label(btn_frame, text="Borrar:", bg="#F0F4F8", font=self.fuente_principal).pack(side="left", padx=(15, 2))
        self.delete_count = tk.Spinbox(btn_frame, from_=1, to=100, width=4, font=self.fuente_principal)
        self.delete_count.pack(side="left", padx=5)

        self.btn_delete = tk.Button(btn_frame, text="Borrar Cantidad", bg=self.ROJO_PASTEL,
                                   command=self.ejecutar_borrado, **btn_config)
        self.btn_delete.pack(side="left", padx=5)

        # esta es el area de visualizacion
        tk.Label(main_frame, text="\nContenido en Memoria:", font=self.fuente_principal, 
                 bg="#F0F4F8", fg=self.GRIS_OSCURO).pack(anchor="w")
        
        self.display_area = tk.Text(main_frame, font=self.fuente_mono, height=7, 
                                    bg="white", relief="flat", padx=15, pady=15,
                                    highlightthickness=1, highlightbackground="#D5DBDB")
        self.display_area.pack(fill="both", pady=10)
        self.display_area.config(state="disabled") # Bloqueado para edición directa

        # el registro del historial 
        tk.Label(main_frame, text="Historial de Acciones:", font=self.fuente_principal, 
                 bg="#F0F4F8", fg=self.GRIS_OSCURO).pack(anchor="w")
        
        self.history_list = tk.Listbox(main_frame, font=("Courier New", 10), height=5, 
                                       bg="#FDFEFE", relief="flat", borderwidth=0)
        self.history_list.pack(fill="both", expand=True, pady=(5, 0))

    

    def actualizar_pantalla(self):
        """Mantiene la UI sincronizada con la instancia de TextEditor."""
        # 1. Actualizar el cuadro de texto principal
        self.display_area.config(state="normal")
        self.display_area.delete("1.0", tk.END)
        self.display_area.insert(tk.END, self.editor_logica.show())
        self.display_area.config(state="disabled")

        # 2. Actualizar la lista del historial 
        self.history_list.delete(0, tk.END)
        for accion in reversed(self.editor_logica.get_history()):
            self.history_list.insert(tk.END, f" • {accion}")
        
        # 3. Hacer scroll al inicio del historial para ver lo último
        self.history_list.see(0)

    def ejecutar_escritura(self):
        texto = self.input_text.get()
        exito, msj = self.editor_logica.write(texto)
        if exito:
            self.input_text.delete(0, tk.END)
            self.actualizar_pantalla()
        else:
            messagebox.showwarning("Entrada Inválida", msj)

    def ejecutar_borrado(self):
        try:
            n = int(self.delete_count.get())
            exito, msj = self.editor_logica.delete(n)
            self.actualizar_pantalla()
            if not exito:
                messagebox.showerror("Error de Borrado", msj)
            elif "Aviso" in msj:
                messagebox.showinfo("Aviso", msj)
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número entero.")

    def ejecutar_undo(self):
        exito, msj = self.editor_logica.undo()
        if exito:
            self.actualizar_pantalla()
        else:
            messagebox.showinfo("Undo", msj)

    def ejecutar_redo(self):
        exito, msj = self.editor_logica.redo()
        if exito:
            self.actualizar_pantalla()
        else:
            messagebox.showinfo("Redo", msj)

# Punto de entrada de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    #Le agregue esto para que estuviera centrada la pantalla 
    # y se viera profesional y bonito
    root.eval('tk::PlaceWindow . center')
    app = EditorGrafico(root)
    root.mainloop()

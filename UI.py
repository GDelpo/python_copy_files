# UI.py
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading
import backend  # <--- ACÁ IMPORTAMOS TU OTRO SCRIPT

class AppCopiador:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Archivos")
        self.root.geometry("650x500")

        # Variables
        self.var_txt = tk.StringVar()
        self.var_destino = tk.StringVar()

        # UI
        self._setup_ui()

    def _setup_ui(self):
        # Frame Inputs
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack(fill="x")

        # Input TXT
        tk.Label(frame, text="Listado (.txt):").grid(row=0, column=0, sticky="w")
        tk.Entry(frame, textvariable=self.var_txt, width=50).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Buscar", command=self.buscar_txt).grid(row=0, column=2)

        # Input Destino
        tk.Label(frame, text="Destino:").grid(row=1, column=0, sticky="w", pady=10)
        tk.Entry(frame, textvariable=self.var_destino, width=50).grid(row=1, column=1, padx=5)
        tk.Button(frame, text="Buscar", command=self.buscar_dest).grid(row=1, column=2)

        # Botón Ejecutar
        self.btn_run = tk.Button(self.root, text="PROCESAR LOTE", bg="#007acc", fg="white", 
                                 font=("Arial", 11, "bold"), command=self.ejecutar_thread)
        self.btn_run.pack(pady=10, ipadx=20)

        # Consola Log
        tk.Label(self.root, text="Progreso:").pack(anchor="w", padx=10)
        self.txt_log = scrolledtext.ScrolledText(self.root, height=15, state='disabled')
        self.txt_log.pack(padx=10, pady=5, fill="both", expand=True)

    # --- Helpers UI ---
    def buscar_txt(self):
        f = filedialog.askopenfilename(filetypes=[("Texto", "*.txt")])
        if f: self.var_txt.set(f)

    def buscar_dest(self):
        d = filedialog.askdirectory()
        if d: self.var_destino.set(d)

    def log_ui(self, mensaje):
        """Esta función se la pasamos al backend para que 'imprima' acá"""
        self.txt_log.config(state='normal')
        self.txt_log.insert(tk.END, f"{mensaje}\n")
        self.txt_log.see(tk.END)
        self.txt_log.config(state='disabled')

    # --- Lógica ---
    def ejecutar_thread(self):
        if not self.var_txt.get() or not self.var_destino.get():
            messagebox.showwarning("Atención", "Seleccioná el archivo y el destino primero.")
            return
        
        # Bloqueamos botón y limpiamos log
        self.btn_run.config(state="disabled", text="Trabajando...")
        self.txt_log.config(state='normal')
        self.txt_log.delete(1.0, tk.END)
        self.txt_log.config(state='disabled')

        # Lanzamos el hilo para no congelar la ventana
        threading.Thread(target=self.iniciar_proceso).start()

    def iniciar_proceso(self):
        try:
            # LLAMADA AL BACKEND
            # Fijate que pasamos self.log_ui como argumento 'logger'
            stats = backend.procesar_lote(
                self.var_txt.get(), 
                self.var_destino.get(), 
                logger=self.log_ui
            )
            
            # Mensaje final
            msg = (f"Fin del proceso.\n\n"
                   f"✅ Correctos: {stats['ok']}\n"
                   f"⏭️ Saltados: {stats['skip']}\n"
                   f"❌ Errores: {stats['error']}")
            
            messagebox.showinfo("Reporte", msg)

        except Exception as e:
            self.log_ui(f"ERROR FATAL: {e}")
            messagebox.showerror("Error", str(e))
        
        finally:
            self.btn_run.config(state="normal", text="PROCESAR LOTE")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppCopiador(root)
    root.mainloop()
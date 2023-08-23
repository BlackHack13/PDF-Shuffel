import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from PDF_Shuffel_Logic import PDFShuffler_Logic # Importieren Sie Ihre PDFShuffler_Logic-Klasse

class PDFShufflerGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("PDF Shuffler")
        self.create_ui()

    def create_ui(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.folder_label = ttk.Label(frame, text="Ordner:")
        self.folder_label.grid(row=0, column=0, sticky=tk.W, pady=5)

        self.folder_entry = ttk.Entry(frame, width=40)
        self.folder_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

        self.browse_button = ttk.Button(frame, text="Durchsuchen", command=self.browse_folder)
        self.browse_button.grid(row=0, column=2, sticky=tk.W, pady=5)

        self.mode_label = ttk.Label(frame, text="Modus:")
        self.mode_label.grid(row=1, column=0, sticky=tk.W, pady=5)

        self.mode_combobox = ttk.Combobox(frame, values=["A", "B"], state="readonly")
        self.mode_combobox.grid(row=1, column=1, sticky=tk.W, pady=5)
        self.mode_combobox.set("A")

        self.merge_button = ttk.Button(frame, text="PDFs mischen", command=self.merge_pdfs)
        self.merge_button.grid(row=2, column=0, columnspan=3, pady=20)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        self.folder_entry.delete(0, tk.END)
        self.folder_entry.insert(0, folder_path)

    def merge_pdfs(self):
        folder = self.folder_entry.get()
        mode = self.mode_combobox.get()
        paired_pages_dict = {}  # Dies ist nur ein Platzhalter.

        try:
            mixer = PDFShuffler_Logic(folder)
            mixer.create_shuffled_pdf(mode, paired_pages_dict)
            messagebox.showinfo("Erfolg", "PDFs wurden erfolgreich gemischt!")
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFShufflerGUI(root)
    root.mainloop()

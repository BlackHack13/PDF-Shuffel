import PyPDF2
import random
import os

# Ordner "PDF" öffnen
folder = 'PDF'
pdf_files = [f for f in os.listdir(folder) if f.endswith('.pdf')]

# Neue PDF-Datei erstellen
pdf_writer = PyPDF2.PdfWriter()

# Alle PDF-Dateien durchlaufen und mischen
for pdf_file_name in pdf_files:
    # PDF-Datei öffnen
    with open(os.path.join(folder, pdf_file_name), 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Seiten zufällig mischen
        num_pages = len(pdf_reader.pages)
        pages = list(range(num_pages))
        random.shuffle(pages)

        for page_num in pages:
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

# Zufällig gemischte PDF-Datei speichern
base_name, _ = os.path.splitext(pdf_file_name)
shuffled_pdf_file_name = base_name + '_Gemischt.pdf'
with open(os.path.join(folder, shuffled_pdf_file_name), 'wb') as shuffled_pdf:
    pdf_writer.write(shuffled_pdf)

import PyPDF2
import random
import os

# Ordner "PDF" öffnen
folder = 'PDF'
pdf_files = [f for f in os.listdir(folder) if f.endswith('.pdf')]

# Alle PDF-Dateien durchlaufen und mischen
for pdf_file_name in pdf_files:
    # PDF-Datei öffnen
    pdf_file = open(os.path.join(folder, pdf_file_name), 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Seiten zufällig mischen
    num_pages = len(pdf_reader.pages)
    pages = list(range(num_pages))
    random.shuffle(pages)

    # Neue PDF-Datei erstellen
    pdf_writer = PyPDF2.PdfWriter()
    for page_num in pages:
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)

    # Zufällig gemischte PDF-Datei speichern
    shuffled_pdf_file_name = pdf_file_name.replace('.pdf', '') + '_Gemischt.pdf'
    shuffled_pdf = open(os.path.join(folder, shuffled_pdf_file_name), 'wb')
    pdf_writer.write(shuffled_pdf)

    # Ursprüngliche PDF-Datei schließen
    pdf_file.close()
    shuffled_pdf.close()

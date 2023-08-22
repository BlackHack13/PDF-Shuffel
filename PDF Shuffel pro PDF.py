import PyPDF2
import random
import os

def shuffle_pages_from_pdf(pdf_file_path):
    """Shuffles the pages of a given PDF and returns a PdfWriter object with the shuffled pages."""
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        pages = list(range(num_pages))
        random.shuffle(pages)

        pdf_writer = PyPDF2.PdfWriter()
        for page_num in pages:
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    return pdf_writer

def create_shuffled_pdf(folder):
    """Combines and shuffles pages from all PDFs in the given folder and saves them into a new PDF."""
    pdf_files = [f for f in os.listdir(folder) if f.endswith('.pdf')]
    if not pdf_files:
        print("Keine PDF-Dateien im Ordner gefunden.")
        return
    combined_writer = PyPDF2.PdfWriter()

    for pdf_file_name in pdf_files:
        pdf_writer = shuffle_pages_from_pdf(os.path.join(folder, pdf_file_name))
        for i in range(len(pdf_writer.pages)):
            combined_writer.add_page(pdf_writer.pages[i])

    shuffled_pdf_file_name = 'Alle_Gemischt.pdf'
    with open(os.path.join(folder, shuffled_pdf_file_name), 'wb') as shuffled_pdf:
        combined_writer.write(shuffled_pdf)

create_shuffled_pdf('PDF')

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
        print("Keine PDF-Dateien im angegebenen Ordner gefunden.")
        return

    all_pages = []
    pdf_file_streams = []  # list to keep track of open file streams

    for pdf_file_name in pdf_files:
        pdf_file_stream = open(os.path.join(folder, pdf_file_name), 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file_stream)
        all_pages.extend(pdf_reader.pages)
        pdf_file_streams.append(pdf_file_stream)  # add the open stream to the list

    random.shuffle(all_pages)
    combined_writer = PyPDF2.PdfWriter()
    for page in all_pages:
        combined_writer.add_page(page)

    shuffled_pdf_file_name = 'All_Gemischt.pdf'
    with open(os.path.join(folder, shuffled_pdf_file_name), 'wb') as shuffled_pdf:
        combined_writer.write(shuffled_pdf)

    # Close all the open file streams
    for pdf_file_stream in pdf_file_streams:
        pdf_file_stream.close()

create_shuffled_pdf('PDF')


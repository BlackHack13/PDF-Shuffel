import os
import random
import PyPDF2


class PDFShuffler_Logic:

    def __init__(self, folder):
        self.folder = folder

    def _shuffle_pages_from_pdf(self, pdf_file_path, paired_pages=[]):
        pdf_reader = PyPDF2.PdfReader(pdf_file_path)

        all_pages = list(range(len(pdf_reader.pages)))
        units = []

        for pair in paired_pages:
            if all(p in all_pages for p in pair):
                units.append([(pdf_file_path, p) for p in pair])
                for p in pair:
                    all_pages.remove(p)

        units.extend([[(pdf_file_path, p)] for p in all_pages])
        random.shuffle(units)

        pdf_writer = PyPDF2.PdfWriter()
        for unit in units:
            for _, page_num in unit:
                pdf_writer.add_page(pdf_reader.pages[page_num])

        return pdf_writer, units

    def create_shuffled_pdf(self, mode="A", paired_pages_dict={}):
        pdf_files = [f for f in os.listdir(self.folder) if f.endswith('.pdf')]
        if not pdf_files:
            print("Keine PDF-Dateien im angegebenen Ordner gefunden.")
            return

        combined_writer = PyPDF2.PdfWriter()
        all_units = []

        for pdf_file_name in pdf_files:
            paired_pages_for_this_pdf = paired_pages_dict.get(pdf_file_name, [])
            pdf_writer, units = self._shuffle_pages_from_pdf(os.path.join(self.folder, pdf_file_name),
                                                             paired_pages_for_this_pdf)

            if mode == "A":
                all_units.extend(units)
            elif mode == "B":
                for page in pdf_writer.pages:
                    combined_writer.add_page(page)

        if mode == "A":
            random.shuffle(all_units)
            for unit in all_units:
                for pdf_file_path, page_num in unit:
                    pdf_reader = PyPDF2.PdfReader(pdf_file_path)
                    combined_writer.add_page(pdf_reader.pages[page_num])

        shuffled_pdf_file_name = 'Alle_Gemischt.pdf'
        with open(os.path.join(self.folder, shuffled_pdf_file_name), 'wb') as shuffled_pdf:
            combined_writer.write(shuffled_pdf)


# Beispiel zur Verwendung:
mixer = PDFShuffler_Logic('PDF')

paired_pages = {
    'Verständnisfragen_1.pdf': [[4, 5], [9, 10]],
    'Verständnisfragen_2.pdf': [[0, 1]]}

mixer.create_shuffled_pdf(mode="A", paired_pages_dict=paired_pages)
# mixer.create_shuffled_pdf(mode="B", paired_pages_dict=paired_pages)

# Modus A: Behält die Paare bei, kombiniert Seiten aus allen PDFs, mischt und speichert in einer PDF.
# Modus B: Behält die Paare bei, mischt die Seiten innerhalb jeder PDF und kombiniert dann in der ursprünglichen Reihenfolge.
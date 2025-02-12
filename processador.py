import pytesseract
from PIL import Image
from docx import Document
from fpdf import FPDF

# Definir o caminho do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def save_text_as_pdf(text, output_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(output_path)

def save_text_as_word(text, output_path):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)

def process_image_to_document(image_path, output_format="pdf"):
    text = extract_text_from_image(image_path)
    if output_format == "pdf":
        save_text_as_pdf(text, "output.pdf")
    elif output_format == "word":
        save_text_as_word(text, "output.docx")
    else:
        raise ValueError("Formato inválido. Use 'pdf' ou 'word'.")

# Exemplo de uso:
# process_image_to_document("imagem.jpg", "pdf")
# process_image_to_document("imagem.jpg", "word")

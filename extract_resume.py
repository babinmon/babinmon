
import pdfplumber

pdf_path = 'Babin Mon S R - Resume 23i207.pdf'

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)

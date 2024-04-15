# Pre-processing Step
"""

!pip install tika
!pip install spacy

!pip install tika python-docx

from tika import parser
from docx import Document
import os

def extract_text_from_pdf(pdf_file):
    parsed_pdf = parser.from_file(pdf_file)
    text_content = parsed_pdf['content']
    text_content = " ".join(text_content.strip().split())

    return text_content

def save_to_plain_text(text_content, output_dir, filename):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_file = os.path.join(output_dir, filename + ".txt")

    with open(output_file, "w") as file:
        file.write(text_content)

def convert_ppt_to_text_files(pdf_file, output_dir):
    text_content = extract_text_from_pdf(pdf_file)
    filename = os.path.splitext(os.path.basename(pdf_file))[0]
    save_to_plain_text(text_content, output_dir, filename)

if __name__ == "__main__":
    pdf_file = "/content/slides03.pdf" #Path to the input files
    output_dir = "output"              #Path to the output folder/file
    convert_ppt_to_text_files(pdf_file, output_dir)
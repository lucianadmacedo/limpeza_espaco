import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Initialize an empty string to store extracted text
    extracted_text = ""

    # Iterate through pages
    for page_number in range(pdf_document.page_count):
        # Get the page
        page = pdf_document[page_number]

        # Extract text from the page
        text = page.get_text()

        # Append the extracted text to the result string
        extracted_text += text

    # Close the PDF document
    pdf_document.close()

    return extracted_text

def save_to_txt(text, output_path):
    # Save the extracted text to a TXT file
    with open(output_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)


pdf_path = "/Users/lucianadiasdemacedo/Downloads/AGARESP-2270174-2023-11-16.pdf"
output_txt_path = "/Users/lucianadiasdemacedo/Downloads/AGARESP-2270174-2023-11-16_extracted_python.txt"

extracted_text = extract_text_from_pdf(pdf_path)
save_to_txt(extracted_text, output_txt_path)

print(f"Text extracted from PDF and saved to {output_txt_path}")
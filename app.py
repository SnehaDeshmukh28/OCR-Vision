import streamlit as st
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os

# Set Tesseract path if needed (update with your actual path)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\TesseractOCR\tesseract.exe'

# Function to perform OCR on images
def ocr_image(image):
    return pytesseract.image_to_string(image)

# Function to perform OCR on PDFs
def ocr_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)
    return text

# Streamlit app
def main():
    st.title("OCR Application")
    st.write("Upload an image, PDF, or document to extract text.")

    uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg", "pdf"])

    if uploaded_file is not None:
        file_type = uploaded_file.type
        if "image" in file_type:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True, width=200)
            st.write("Extracted Text:")
            st.write(ocr_image(image))
        elif "pdf" in file_type:
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.write("Extracted Text:")
            st.write(ocr_pdf("temp.pdf"))
            os.remove("temp.pdf")
        else:
            st.error("Unsupported file type. Please upload a PNG, JPG, JPEG, or PDF file.")

if __name__ == "__main__":
    main()

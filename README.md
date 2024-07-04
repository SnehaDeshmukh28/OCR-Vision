# OCR Application

This is a simple OCR (Optical Character Recognition) application built using Streamlit and Tesseract. The application allows users to upload images or PDF files and extracts text from them.

## Features

- Upload and process images (PNG, JPG, JPEG).
- Upload and process PDF files.
- Display the uploaded image or PDF.
- Extract and display text from the uploaded files using Tesseract OCR.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- `pip` package installer

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/your-username/ocr-application.git
   cd ocr-application
   ```

2. **Install the required packages**:

   ```sh
   pip install -r requirements.txt
   ```

3. **Install Tesseract**:

   ### For Windows:
   - Download Tesseract from the [Tesseract at UB Mannheim page](https://github.com/UB-Mannheim/tesseract/wiki).
   - Run the installer and follow the instructions to install Tesseract.
   - Add Tesseract to your system's PATH:
     - Open the Start menu and search for "Environment Variables".
     - Click on "Edit the system environment variables".
     - In the System Properties window, click on the "Environment Variables" button.
     - In the Environment Variables window, find the `Path` variable under System variables, and click "Edit".
     - Click "New" and add the path to the Tesseract executable (e.g., `C:\Program Files\Tesseract-OCR`).

   ### For macOS:
   - Install Homebrew (if you haven't already):
     ```sh
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Install Tesseract using Homebrew:
     ```sh
     brew install tesseract
     ```

   ### For Linux (Ubuntu/Debian):
   - Install Tesseract using APT:
     ```sh
     sudo apt update
     sudo apt install tesseract-ocr
     ```

4. **Verify Tesseract Installation**:
   ```sh
   tesseract --version
   ```

## Usage

1. **Run the Streamlit application**:
   ```sh
   streamlit run app.py
   ```

2. **Upload a file**:
   - Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).
   - Upload an image (PNG, JPG, JPEG) or PDF file.
   - The uploaded file will be displayed on the page.
   - The extracted text will be shown below the uploaded file.

## Project Structure

```
ocr-application/
│
├── app.py                   # Main application file
├── requirements.txt         # Python package dependencies
└── README.md                # Project README file
```

## Dependencies

- streamlit
- pytesseract
- pillow
- pdf2image

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Pillow](https://python-pillow.org/)
- [pdf2image](https://github.com/Belval/pdf2image)

from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader

def main():
    load_dotenv()
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬")

    # Upload PDF
    pdf = st.file_uploader("Upload your PDF", type=["pdf"])
    
    # Extract text from PDF
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        st.write(text)

if __name__ == '__main__':
    main()
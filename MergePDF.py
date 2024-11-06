import PyPDF2
import streamlit as st

# Streamlit app title
st.title("PDF Merger")

# File uploader to allow multiple files
uploaded_files = st.file_uploader("Upload PDF files to merge", type="pdf", accept_multiple_files=True)

if uploaded_files:
    # Create a PdfMerger object
    final_pdf = PyPDF2.PdfMerger()

    # Iterate over each uploaded file and append it to the PdfMerger object
    for uploaded_file in uploaded_files:
        final_pdf.append(uploaded_file)

    # Save the merged PDF to a new file in memory
    with open("merged-pdf.pdf", "wb") as output_pdf:
        final_pdf.write(output_pdf)
        final_pdf.close()
        
    # Provide a download button for the merged PDF
    with open("merged-pdf.pdf", "rb") as file:
        st.download_button(
            label="Download Merged PDF",
            data=file,
            file_name="merged-pdf.pdf",
            mime="application/pdf"
        )


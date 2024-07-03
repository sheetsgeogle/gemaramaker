import streamlit as st
import os
import requests
from PyPDF2 import PdfMerger
from io import BytesIO

# Streamlit app title
st.title("PDF Merger")

# Input fields for start and end numbers
start = st.number_input("Start Number", min_value=1, value=1414)
end = st.number_input("End Number", min_value=1, value=1474)

# Button to trigger the merging process
if st.button("Merge PDFs"):
    # Initialize a PdfMerger object
    merger = PdfMerger()
    
    # Loop through the range and download each PDF
    for i in range(start, end + 1):
        # Define the URL pattern based on the number of digits in the current page number
        url_pattern = f"https://daf-yomi.com/Data/UploadedFiles/DY_Page/{{:0{len(str(i))}d}}.pdf"
        url = url_pattern.format(i)
        response = requests.get(url)
        if response.status_code == 200:
            pdf_bytes = BytesIO(response.content)
            merger.append(pdf_bytes)
    
    # Write the merged PDF to a BytesIO object
    merged_pdf = BytesIO()
    merger.write(merged_pdf)
    merger.close()
    
    # Seek to the beginning of the BytesIO object
    merged_pdf.seek(0)
    
    # Provide a download button for the merged PDF
    st.download_button(
        label="Download Merged PDF",
        data=merged_pdf,
        file_name="merged_document.pdf",
        mime="application/pdf"
    )

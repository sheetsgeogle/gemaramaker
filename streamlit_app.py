import streamlit as st
import os
import requests
from PyPDF2 import PdfMerger
from io import BytesIO

# Streamlit app title
st.title("Gemara Library")

# Options for different types
option = st.selectbox(
    "Select Gemara Type:",
    ["Standard", "Artscroll", "Mesivta", "Koren"]
)

# Dropdown for Mesechta selection
mesechta = st.selectbox(
    "Select Mesechta:",
    ["Berachot", "Shabbat", "Eruvin", "Pesachim", "Yoma", "Sukkah", "Beitzah", "Rosh Hashanah", "Taanit", "Megillah", "Moed Katan", "Chagigah", "Yevamot", "Ketubot", "Nedarim", "Nazir", "Sotah", "Gittin", "Kiddushin", "Baba Kama", "Baba Metsia", "Baba Batra", "Sanhedrin", "Makkot", "Shevuot", "Avodah Zarah", "Horayot", "Zevachim", "Menachot", "Chullin", "Bechorot", "Arachin", "Temurah", "Keritot", "Meilah", "Kinnim", "Midot", "Kinnim", "Tamid", "Midos"]
)

# Input fields for start and end numbers
start = st.number_input("Start Number", min_value=1, value=1414)
end = st.number_input("End Number", min_value=1, value=1474)

# Function to generate PDF URL based on selected options
def generate_pdf_url(option, mesechta, page_number):
    base_url = {
        "Artscroll": "https://example.com/artsroll/{mesechta}/{page_number}.pdf",
        "Mesivta": "https://example.com/mesivta/{mesechta}/{page_number}.pdf",
        "Koren": "https://example.com/koren/{mesechta}/{page_number}.pdf",
        "Standard": "https://example.com/standard/{mesechta}/{page_number}.pdf"
    }
    return base_url[option].format(mesechta=mesechta, page_number=page_number)

# Button to trigger the merging process
if st.button("View Merged PDFs"):
    # Initialize a PdfMerger object
    merger = PdfMerger()
    
    # Loop through the range and download each PDF
    for i in range(start, end + 1):
        url = generate_pdf_url(option, mesechta, i)
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
    
    # Provide a view button for the merged PDF
    st.download_button(
        label="View PDF 📄",
        data=merged_pdf,
        file_name="merged_document.pdf",
        mime="application/pdf"
    )

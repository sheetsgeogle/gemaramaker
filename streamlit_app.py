import streamlit as st

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
    [
        "ברכות", "כריתות", "הוריות", "מגילה", "סנהדרין", "תענית", "מועד קטן",
        "סוטה", "ערכין", "מכות", "שבת", "קידושין", "חגיגה", "בבא מציעא",
        "בבא קמא", "עבודה זרה", "תמורה", "נידה", "יבמות", "ראש השנה",
        "פסחים", "גיטין", "בכורות", "שבועות", "מנחות", "כתובות", "יומא",
        "עירובין", "ביצה", "חולין", "סוכה", "זבחים", "תמיד", "בבא בתרא",
        "נזיר", "מעילה", "נדרים"
    ]
)

# URL patterns for different Gemara types and Mesechtot
url_patterns = {
    "Standard": {
        "ברכות": "https://example.com/standard/berachot.pdf",
        # Add more URLs here...
    },
    "Artscroll": {
        "ברכות": "https://example.com/artscroll/berachot.pdf",
        # Add more URLs here...
    },
    "Mesivta": {
        "ברכות": "https://example.com/mesivta/berachot.pdf",
        # Add more URLs here...
    },
    "Koren": {
        "ברכות": "https://example.com/koren/berachot.pdf",
        # Add more URLs here...
    }
}

# Generate the URL based on the selected options
if option in url_patterns and mesechta in url_patterns[option]:
    pdf_url = url_patterns[option][mesechta]
    # Create a button to open the PDF URL
    st.markdown(
        f"""
        <a href="{pdf_url}" target="_blank" style="
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            color: black;
            background-color: white;
            border: 2px solid #D6D6D9;
            border-radius: 10px;
            text-align: center;
            text-decoration: none;
        ">Open PDF</a>
        """,
        unsafe_allow_html=True
    )
else:
    st.write("The selected Gemara type and Mesechta combination is not available.")

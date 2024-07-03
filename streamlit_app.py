import streamlit as st
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
    [
        "ברכות", "כריתות", "הוריות", "מגילה", "סנהדרין", "תענית", "מועד קטן",
        "סוטה", "ערכין", "מכות", "שבת", "קידושין", "חגיגה", "בבא מציעא",
        "בבא קמא", "עבודה זרה", "תמורה", "נידה", "יבמות", "ראש השנה",
        "פסחים", "גיטין", "בכורות", "שבועות", "מנחות", "כתובות", "יומא",
        "עירובין", "ביצה", "חולין", "סוכה", "זבחים", "תמיד", "בבא בתרא",
        "נזיר", "מעילה", "נדרים"
    ]
)

# Input field for page range
page_range = st.slider("Select Page Range", min_value=1, max_value=100, value=(1, 10))

# URL patterns for different Gemara types and Mesechtot
url_patterns = {
    "Standard": {
        "ברכות": "https://example.com/standard/berachot/{page_number}.pdf",
        "כריתות": "https://example.com/standard/keritot/{page_number}.pdf",
        "הוריות": "https://example.com/standard/horayot/{page_number}.pdf",
        "מגילה": "https://example.com/standard/megillah/{page_number}.pdf",
        "סנהדרין": "https://example.com/standard/sanhedrin/{page_number}.pdf",
        "תענית": "https://example.com/standard/taanit/{page_number}.pdf",
        "מועד קטן": "https://example.com/standard/moed_katan/{page_number}.pdf",
        "סוטה": "https://example.com/standard/sotah/{page_number}.pdf",
        "ערכין": "https://example.com/standard/erukhin/{page_number}.pdf",
        "מכות": "https://example.com/standard/makkot/{page_number}.pdf",
        "שבת": "https://example.com/standard/shabbat/{page_number}.pdf",
        "קידושין": "https://example.com/standard/kiddushin/{page_number}.pdf",
        "חגיגה": "https://example.com/standard/chagigah/{page_number}.pdf",
        "בבא מציעא": "https://example.com/standard/baba_metzia/{page_number}.pdf",
        "בבא קמא": "https://example.com/standard/baba_kamma/{page_number}.pdf",
        "עבודה זרה": "https://example.com/standard/avodah_zarah/{page_number}.pdf",
        "תמורה": "https://example.com/standard/temurah/{page_number}.pdf",
        "נידה": "https://example.com/standard/niddah/{page_number}.pdf",
        "יבמות": "https://example.com/standard/yevamot/{page_number}.pdf",
        "ראש השנה": "https://example.com/standard/rosh_hashanah/{page_number}.pdf",
        "פסחים": "https://example.com/standard/psachim/{page_number}.pdf",
        "גיטין": "https://example.com/standard/gittin/{page_number}.pdf",
        "בכורות": "https://example.com/standard/bechorot/{page_number}.pdf",
        "שבועות": "https://example.com/standard/shevuot/{page_number}.pdf",
        "מנחות": "https://example.com/standard/menachot/{page_number}.pdf",
        "כתובות": "https://example.com/standard/ketubot/{page_number}.pdf",
        "יומא": "https://example.com/standard/yoma/{page_number}.pdf",
        "עירובין": "https://example.com/standard/eruvin/{page_number}.pdf",
        "ביצה": "https://example.com/standard/beitzah/{page_number}.pdf",
        "חולין": "https://example.com/standard/chullin/{page_number}.pdf",
        "סוכה": "https://example.com/standard/sukkah/{page_number}.pdf",
        "זבחים": "https://example.com/standard/zevachim/{page_number}.pdf",
        "תמיד": "https://example.com/standard/tamid/{page_number}.pdf",
        "בבא בתרא": "https://example.com/standard/baba_batra/{page_number}.pdf",
        "נזיר": "https://example.com/standard/nazir/{page_number}.pdf",
        "מעילה": "https://example.com/standard/meilah/{page_number}.pdf",
        "נדרים": "https://example.com/standard/nedarim/{page_number}.pdf"
    },
    "Artscroll": {
        "ברכות": "https://example.com/artscroll/berachot/{page_number}.pdf",
        "כריתות": "https://example.com/artscroll/keritot/{page_number}.pdf",
        "הוריות": "https://example.com/artscroll/horayot/{page_number}.pdf",
        "מגילה": "https://example.com/artscroll/megillah/{page_number}.pdf",
        "סנהדרין": "https://example.com/artscroll/sanhedrin/{page_number}.pdf",
        "תענית": "https://example.com/artscroll/taanit/{page_number}.pdf",
        "מועד קטן": "https://example.com/artscroll/moed_katan/{page_number}.pdf",
        "סוטה": "https://example.com/artscroll/sotah/{page_number}.pdf",
        "ערכין": "https://example.com/artscroll/erukhin/{page_number}.pdf",
        "מכות": "https://example.com/artscroll/makkot/{page_number}.pdf",
        "שבת": "https://example.com/artscroll/shabbat/{page_number}.pdf",
        "קידושין": "https://example.com/artscroll/kiddushin/{page_number}.pdf",
        "חגיגה": "https://example.com/artscroll/chagigah/{page_number}.pdf",
        "בבא מציעא": "https://example.com/artscroll/baba_metzia/{page_number}.pdf",
        "בבא קמא": "https://example.com/artscroll/baba_kamma/{page_number}.pdf",
        "עבודה זרה": "https://example.com/artscroll/avodah_zarah/{page_number}.pdf",
        "תמורה": "https://example.com/artscroll/temurah/{page_number}.pdf",
        "נידה": "https://example.com/artscroll/niddah/{page_number}.pdf",
        "יבמות": "https://example.com/artscroll/yevamot/{page_number}.pdf",
        "ראש השנה": "https://example.com/artscroll/rosh_hashanah/{page_number}.pdf",
        "פסחים": "https://example.com/artscroll/psachim/{page_number}.pdf",
        "גיטין": "https://example.com/artscroll/gittin/{page_number}.pdf",
        "בכורות": "https://example.com/artscroll/bechorot/{page_number}.pdf",
        "שבועות": "https://example.com/artscroll/shevuot/{page_number}.pdf",
        "מנחות": "https://example.com/artscroll/menachot/{page_number}.pdf",
        "כתובות": "https://example.com/artscroll/ketubot/{page_number}.pdf",
        "יומא": "https://example.com/artscroll/yoma/{page_number}.pdf",
        "עירובין": "https://example.com/artscroll/eruvin/{page_number}.pdf",
        "ביצה": "https://example.com/artscroll/beitzah/{page_number}.pdf",
        "חולין": "https://example.com/artscroll/chullin/{page_number}.pdf",
        "סוכה": "https://example.com/artscroll/sukkah/{page_number}.pdf",
        "זבחים": "https://example.com/artscroll/zevachim/{page_number}.pdf",
        "תמיד": "https://example.com/artscroll/tamid/{page_number}.pdf",
        "בבא בתרא": "https://example.com/artscroll/baba_batra/{page_number}.pdf",
        "נזיר": "https://example.com/artscroll/nazir/{page_number}.pdf",
        "מעילה": "https://example.com/artscroll/meilah/{page_number}.pdf",
        "נדרים": "https://example.com/artscroll/nedarim/{page_number}.pdf"
    },
    "Mesivta": {
        "ברכות": "https://example.com/mesivta/berachot/{page_number}.pdf",
        "כריתות": "https://example.com/mesivta/keritot/{page_number}.pdf",
        "הוריות": "https://example.com/mesivta/horayot/{page_number}.pdf",
        "מגילה": "https://example.com/mesivta/megillah/{page_number}.pdf",
        "סנהדרין": "https://example.com/mesivta/sanhedrin/{page_number}.pdf",
        "תענית": "https://example.com/mesivta/taanit/{page_number}.pdf",
        "מועד קטן": "https://example.com/mesivta/moed_katan/{page_number}.pdf",
        "סוטה": "https://example.com/mesivta/sotah/{page_number}.pdf",
        "ערכין": "https://example.com/mesivta/erukhin/{page_number}.pdf",
        "מכות": "https://example.com/mesivta/makkot/{page_number}.pdf",
        "שבת": "https://example.com/mesivta/shabbat/{page_number}.pdf",
        "קידושין": "https://example.com/mesivta/kiddushin/{page_number}.pdf",
        "חגיגה": "https://example.com/mesivta/chagigah/{page_number}.pdf",
        "בבא מציעא": "https://example.com/mesivta/baba_metzia/{page_number}.pdf",
        "בבא קמא": "https://example.com/mesivta/baba_kamma/{page_number}.pdf",
        "עבודה זרה": "https://example.com/mesivta/avodah_zarah/{page_number}.pdf",
        "תמורה": "https://example.com/mesivta/temurah/{page_number}.pdf",
        "נידה": "https://example.com/mesivta/niddah/{page_number}.pdf",
        "יבמות": "https://example.com/mesivta/yevamot/{page_number}.pdf",
        "ראש השנה": "https://example.com/mesivta/rosh_hashanah/{page_number}.pdf",
        "פסחים": "https://example.com/mesivta/psachim/{page_number}.pdf",
        "גיטין": "https://example.com/mesivta/gittin/{page_number}.pdf",
        "בכורות": "https://example.com/mesivta/bechorot/{page_number}.pdf",
        "שבועות": "https://example.com/mesivta/shevuot/{page_number}.pdf",
        "מנחות": "https://example.com/mesivta/menachot/{page_number}.pdf",
        "כתובות": "https://example.com/mesivta/ketubot/{page_number}.pdf",
        "יומא": "https://example.com/mesivta/yoma/{page_number}.pdf",
        "עירובין": "https://example.com/mesivta/eruvin/{page_number}.pdf",
        "ביצה": "https://example.com/mesivta/beitzah/{page_number}.pdf",
        "חולין": "https://example.com/mesivta/chullin/{page_number}.pdf",
        "סוכה": "https://example.com/mesivta/sukkah/{page_number}.pdf",
        "זבחים": "https://example.com/mesivta/zevachim/{page_number}.pdf",
        "תמיד": "https://example.com/mesivta/tamid/{page_number}.pdf",
        "בבא בתרא": "https://example.com/mesivta/baba_batra/{page_number}.pdf",
        "נזיר": "https://example.com/mesivta/nazir/{page_number}.pdf",
        "מעילה": "https://example.com/mesivta/meilah/{page_number}.pdf",
        "נדרים": "https://example.com/mesivta/nedarim/{page_number}.pdf"
    },
    "Koren": {
        "ברכות": "https://example.com/koren/berachot/{page_number}.pdf",
        "כריתות": "https://example.com/koren/keritot/{page_number}.pdf",
        "הוריות": "https://example.com/koren/horayot/{page_number}.pdf",
        "מגילה": "https://example.com/koren/megillah/{page_number}.pdf",
        "סנהדרין": "https://example.com/koren/sanhedrin/{page_number}.pdf",
        "תענית": "https://example.com/koren/taanit/{page_number}.pdf",
        "מועד קטן": "https://example.com/koren/moed_katan/{page_number}.pdf",
        "סוטה": "https://example.com/koren/sotah/{page_number}.pdf",
        "ערכין": "https://example.com/koren/erukhin/{page_number}.pdf",
        "מכות": "https://example.com/koren/makkot/{page_number}.pdf",
        "שבת": "https://example.com/koren/shabbat/{page_number}.pdf",
        "קידושין": "https://example.com/koren/kiddushin/{page_number}.pdf",
        "חגיגה": "https://example.com/koren/chagigah/{page_number}.pdf",
        "בבא מציעא": "https://example.com/koren/baba_metzia/{page_number}.pdf",
        "בבא קמא": "https://example.com/koren/baba_kamma/{page_number}.pdf",
        "עבודה זרה": "https://example.com/koren/avodah_zarah/{page_number}.pdf",
        "תמורה": "https://example.com/koren/temurah/{page_number}.pdf",
        "נידה": "https://example.com/koren/niddah/{page_number}.pdf",
        "יבמות": "https://example.com/koren/yevamot/{page_number}.pdf",
        "ראש השנה": "https://example.com/koren/rosh_hashanah/{page_number}.pdf",
        "פסחים": "https://example.com/koren/psachim/{page_number}.pdf",
        "גיטין": "https://example.com/koren/gittin/{page_number}.pdf",
        "בכורות": "https://example.com/koren/bechorot/{page_number}.pdf",
        "שבועות": "https://example.com/koren/shevuot/{page_number}.pdf",
        "מנחות": "https://example.com/koren/menachot/{page_number}.pdf",
        "כתובות": "https://example.com/koren/ketubot/{page_number}.pdf",
        "יומא": "https://example.com/koren/yoma/{page_number}.pdf",
        "עירובין": "https://example.com/koren/eruvin/{page_number}.pdf",
        "ביצה": "https://example.com/koren/beitzah/{page_number}.pdf",
        "חולין": "https://example.com/koren/chullin/{page_number}.pdf",
        "סוכה": "https://example.com/koren/sukkah/{page_number}.pdf",
        "זבחים": "https://example.com/koren/zevachim/{page_number}.pdf",
        "תמיד": "https://example.com/koren/tamid/{page_number}.pdf",
        "בבא בתרא": "https://example.com/koren/baba_batra/{page_number}.pdf",
        "נזיר": "https://example.com/koren/nazir/{page_number}.pdf",
        "מעילה": "https://example.com/koren/meilah/{page_number}.pdf",
        "נדרים": "https://example.com/koren/nedarim/{page_number}.pdf"
    }
}

# Button to trigger the merging process
if st.button("View Merged PDFs"):
    start, end = page_range
    # Initialize a PdfMerger object
    merger = PdfMerger()
    
    # Fetch the URL pattern for the selected Gemara type and Mesechta
    if option in url_patterns and mesechta in url_patterns[option]:
        url_pattern = url_patterns[option][mesechta]
    else:
        st.error("Invalid selection for Gemara Type or Mesechta.")
        st.stop()

    # Loop through the page range and download each PDF
    for i in range(start, end + 1):
        url = url_pattern.format(page_number=i)
        response = requests.get(url)
        if response.status_code == 200:
            pdf_bytes = BytesIO(response.content)
            merger.append(pdf_bytes)
        else:
            st.warning(f"Failed to fetch page {i}. URL: {url}")
    
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

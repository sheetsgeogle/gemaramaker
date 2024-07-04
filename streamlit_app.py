import streamlit as st
import streamlit_toggle as stt  # Import the custom toggle switch library
from datetime import datetime

# Streamlit app title
st.title("Gemara Library")

# Dropdown for Gemara Type and Mesechta
option = st.selectbox(
    "Select Gemara Type:",
    ["Standard", "Artscroll", "Mesivta", "Koren"]
)

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

# Daf Yomi toggle
daf_yomi_toggle = stt.st_toggle_switch(
    label='Daf Yomi (On/Off)',
    default_value=False,  # Default to Off
    label_after=True,
    inactive_color='#780c21',  # Red when Off
    active_color='#0c7822',  # Green when On
    track_color='#0c4c78'  # Blue track color
)

if daf_yomi_toggle:
    # Calculate the current day's Daf Yomi page number
    today = datetime.now().date()
    start_date = datetime(2024, 7, 3).date()  # Starting date for Daf Yomi pages
    page_number = (today - start_date).days + 3276  # Calculate page number

    # Generate the URL for Daf Yomi
    pdf_url = f"https://daf-yomi.com/Data/UploadedFiles/DY_Page/{page_number}.pdf"

    # Hide Gemara Type and Mesechta selectors
    st.markdown("<style> .stSelectbox { display: none; } </style>", unsafe_allow_html=True)

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
        ">Open Daf Yomi PDF</a>
        """,
        unsafe_allow_html=True
    )
else:
    # URL patterns for different Gemara types and Mesechtot
    url_patterns = {
        "Standard": {
            "ברכות": "https://example.com/standard/berachot.pdf",
            "כריתות": "https://example.com/standard/keritot.pdf",
            "הוריות": "https://example.com/standard/horayot.pdf",
            "מגילה": "https://example.com/standard/megillah.pdf",
            "סנהדרין": "https://example.com/standard/sanhedrin.pdf",
            "תענית": "https://example.com/standard/taanit.pdf",
            "מועד קטן": "https://example.com/standard/moed_katan.pdf",
            "סוטה": "https://example.com/standard/sotah.pdf",
            "ערכין": "https://example.com/standard/erukhin.pdf",
            "מכות": "https://example.com/standard/makkot.pdf",
            "שבת": "https://example.com/standard/shabbat.pdf",
            "קידושין": "https://example.com/standard/kiddushin.pdf",
            "חגיגה": "https://example.com/standard/chagigah.pdf",
            "בבא מציעא": "https://example.com/standard/baba_metzia.pdf",
            "בבא קמא": "https://example.com/standard/baba_kamma.pdf",
            "עבודה זרה": "https://example.com/standard/avodah_zarah.pdf",
            "תמורה": "https://example.com/standard/temurah.pdf",
            "נידה": "https://example.com/standard/niddah.pdf",
            "יבמות": "https://example.com/standard/yevamot.pdf",
            "ראש השנה": "https://example.com/standard/rosh_hashanah.pdf",
            "פסחים": "https://example.com/standard/psachim.pdf",
            "גיטין": "https://example.com/standard/gittin.pdf",
            "בכורות": "https://example.com/standard/bechorot.pdf",
            "שבועות": "https://example.com/standard/shevuot.pdf",
            "מנחות": "https://example.com/standard/menachot.pdf",
            "כתובות": "https://example.com/standard/ketubot.pdf",
            "יומא": "https://example.com/standard/yoma.pdf",
            "עירובין": "https://example.com/standard/eruvin.pdf",
            "ביצה": "https://example.com/standard/beitzah.pdf",
            "חולין": "https://example.com/standard/chullin.pdf",
            "סוכה": "https://example.com/standard/sukkah.pdf",
            "זבחים": "https://example.com/standard/zevachim.pdf",
            "תמיד": "https://example.com/standard/tamid.pdf",
            "בבא בתרא": "https://example.com/standard/baba_batra.pdf",
            "נזיר": "https://example.com/standard/nazir.pdf",
            "מעילה": "https://example.com/standard/meilah.pdf",
            "נדרים": "https://example.com/standard/nedarim.pdf"
        },
        "Artscroll": {
            "ברכות": "https://example.com/artscroll/berachot.pdf",
            "כריתות": "https://example.com/artscroll/keritot.pdf",
            "הוריות": "https://example.com/artscroll/horayot.pdf",
            "מגילה": "https://example.com/artscroll/megillah.pdf",
            "סנהדרין": "https://example.com/artscroll/sanhedrin.pdf",
            "תענית": "https://example.com/artscroll/taanit.pdf",
            "מועד קטן": "https://example.com/artscroll/moed_katan.pdf",
            "סוטה": "https://example.com/artscroll/sotah.pdf",
            "ערכין": "https://example.com/artscroll/erukhin.pdf",
            "מכות": "https://example.com/artscroll/makkot.pdf",
            "שבת": "https://example.com/artscroll/shabbat.pdf",
            "קידושין": "https://example.com/artscroll/kiddushin.pdf",
            "חגיגה": "https://example.com/artscroll/chagigah.pdf",
            "בבא מציעא": "https://example.com/artscroll/baba_metzia.pdf",
            "בבא קמא": "https://example.com/artscroll/baba_kamma.pdf",
            "עבודה זרה": "https://example.com/artscroll/avodah_zarah.pdf",
            "תמורה": "https://example.com/artscroll/temurah.pdf",
            "נידה": "https://example.com/artscroll/niddah.pdf",
            "יבמות": "https://example.com/artscroll/yevamot.pdf",
            "ראש השנה": "https://example.com/artscroll/rosh_hashanah.pdf",
            "פסחים": "https://example.com/artscroll/psachim.pdf",
            "גיטין": "https://example.com/artscroll/gittin.pdf",
            "בכורות": "https://example.com/artscroll/bechorot.pdf",
            "שבועות": "https://example.com/artscroll/shevuot.pdf",
            "מנחות": "https://example.com/artscroll/menachot.pdf",
            "כתובות": "https://example.com/artscroll/ketubot.pdf",
            "יומא": "https://example.com/artscroll/yoma.pdf",
            "עירובין": "https://example.com/artscroll/eruvin.pdf",
            "ביצה": "https://example.com/artscroll/beitzah.pdf",
            "חולין": "https://example.com/artscroll/chullin.pdf",
            "סוכה": "https://example.com/artscroll/sukkah.pdf",
            "זבחים": "https://example.com/artscroll/zevachim.pdf",
            "תמיד": "https://example.com/artscroll/tamid.pdf",
            "בבא בתרא": "https://example.com/artscroll/baba_batra.pdf",
            "נזיר": "https://example.com/artscroll/nazir.pdf",
            "מעילה": "https://example.com/artscroll/meilah.pdf",
            "נדרים": "https://example.com/artscroll/nedarim.pdf"
        },
        "Mesivta": {
            "ברכות": "https://example.com/mesivta/berachot.pdf",
            "כריתות": "https://example.com/mesivta/keritot.pdf",
            "הוריות": "https://example.com/mesivta/horayot.pdf",
            "מגילה": "https://example.com/mesivta/megillah.pdf",
            "סנהדרין": "https://example.com/mesivta/sanhedrin.pdf",
            "תענית": "https://example.com/mesivta/taanit.pdf",
            "מועד קטן": "https://example.com/mesivta/moed_katan.pdf",
            "סוטה": "https://example.com/mesivta/sotah.pdf",
            "ערכין": "https://example.com/mesivta/erukhin.pdf",
            "מכות": "https://example.com/mesivta/makkot.pdf",
            "שבת": "https://example.com/mesivta/shabbat.pdf",
            "קידושין": "https://example.com/mesivta/kiddushin.pdf",
            "חגיגה": "https://example.com/mesivta/chagigah.pdf",
            "בבא מציעא": "https://example.com/mesivta/baba_metzia.pdf",
            "בבא קמא": "https://example.com/mesivta/baba_kamma.pdf",
            "עבודה זרה": "https://example.com/mesivta/avodah_zarah.pdf",
            "תמורה": "https://example.com/mesivta/temurah.pdf",
            "נידה": "https://example.com/mesivta/niddah.pdf",
            "יבמות": "https://example.com/mesivta/yevamot.pdf",
            "ראש השנה": "https://example.com/mesivta/rosh_hashanah.pdf",
            "פסחים": "https://example.com/mesivta/psachim.pdf",
            "גיטין": "https://example.com/mesivta/gittin.pdf",
            "בכורות": "https://example.com/mesivta/bechorot.pdf",
            "שבועות": "https://example.com/mesivta/shevuot.pdf",
            "מנחות": "https://example.com/mesivta/menachot.pdf",
            "כתובות": "https://example.com/mesivta/ketubot.pdf",
            "יומא": "https://example.com/mesivta/yoma.pdf",
            "עירובין": "https://example.com/mesivta/eruvin.pdf",
            "ביצה": "https://example.com/mesivta/beitzah.pdf",
            "חולין": "https://example.com/mesivta/chullin.pdf",
            "סוכה": "https://example.com/mesivta/sukkah.pdf",
            "זבחים": "https://example.com/mesivta/zevachim.pdf",
            "תמיד": "https://example.com/mesivta/tamid.pdf",
            "בבא בתרא": "https://example.com/mesivta/baba_batra.pdf",
            "נזיר": "https://example.com/mesivta/nazir.pdf",
            "מעילה": "https://example.com/mesivta/meilah.pdf",
            "נדרים": "https://example.com/mesivta/nedarim.pdf"
        },
        "Koren": {
            "ברכות": "https://example.com/koren/berachot.pdf",
            "כריתות": "https://example.com/koren/keritot.pdf",
            "הוריות": "https://example.com/koren/horayot.pdf",
            "מגילה": "https://example.com/koren/megillah.pdf",
            "סנהדרין": "https://example.com/koren/sanhedrin.pdf",
            "תענית": "https://example.com/koren/taanit.pdf",
            "מועד קטן": "https://example.com/koren/moed_katan.pdf",
            "סוטה": "https://example.com/koren/sotah.pdf",
            "ערכין": "https://example.com/koren/erukhin.pdf",
            "מכות": "https://example.com/koren/makkot.pdf",
            "שבת": "https://example.com/koren/shabbat.pdf",
            "קידושין": "https://example.com/koren/kiddushin.pdf",
            "חגיגה": "https://example.com/koren/chagigah.pdf",
            "בבא מציעא": "https://example.com/koren/baba_metzia.pdf",
            "בבא קמא": "https://example.com/koren/baba_kamma.pdf",
            "עבודה זרה": "https://example.com/koren/avodah_zarah.pdf",
            "תמורה": "https://example.com/koren/temurah.pdf",
            "נידה": "https://example.com/koren/niddah.pdf",
            "יבמות": "https://example.com/koren/yevamot.pdf",
            "ראש השנה": "https://example.com/koren/rosh_hashanah.pdf",
            "פסחים": "https://example.com/koren/psachim.pdf",
            "גיטין": "https://example.com/koren/gittin.pdf",
            "בכורות": "https://example.com/koren/bechorot.pdf",
            "שבועות": "https://example.com/koren/shevuot.pdf",
            "מנחות": "https://example.com/koren/menachot.pdf",
            "כתובות": "https://example.com/koren/ketubot.pdf",
            "יומא": "https://example.com/koren/yoma.pdf",
            "עירובין": "https://example.com/koren/eruvin.pdf",
            "ביצה": "https://example.com/koren/beitzah.pdf",
            "חולין": "https://example.com/koren/chullin.pdf",
            "סוכה": "https://example.com/koren/sukkah.pdf",
            "זבחים": "https://example.com/koren/zevachim.pdf",
            "תמיד": "https://example.com/koren/tamid.pdf",
            "בבא בתרא": "https://example.com/koren/baba_batra.pdf",
            "נזיר": "https://example.com/koren/nazir.pdf",
            "מעילה": "https://example.com/koren/meilah.pdf",
            "נדרים": "https://example.com/koren/nedarim.pdf"
        }
    }

    # Construct the PDF URL based on selected type and mesechta
    pdf_url = url_patterns.get(option, {}).get(mesechta, "https://example.com/404.pdf")

    # Show Gemara Type and Mesechta selectors
    st.markdown("<style> .stSelectbox { display: block; } </style>", unsafe_allow_html=True)

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
        ">Open Gemara PDF</a>
        """,
        unsafe_allow_html=True
    )

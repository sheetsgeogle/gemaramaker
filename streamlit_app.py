import streamlit as st
import streamlit_toggle as stt
from datetime import datetime

# Streamlit app title
st.title("Gemara Library")

# Custom CSS to create a rounded rectangle border around the entire page
st.markdown("""
    <style>
        .main {
            padding: 1em;
            border: 2px solid #D6D6D9;
            border-radius: 15px;
            margin: 0 auto;
            max-width: 1200px;
            background-color: #f9f9f9;
        }
        .stButton>button {
            border-radius: 10px;
        }
        .stSelectbox {
            border-radius: 10px;
        }
        .extra-buttons {
            display: flex;
            gap: 10px;
            margin-top: 10px;
        }
        .extra-buttons a {
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            color: black;
            background-color: white;
            border: 2px solid #D6D6D9;
            border-radius: 10px;
            text-align: center;
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

# Container for the app
with st.container():
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

    # Toggle switch for Daf Yomi
    daf_yomi = stt.st_toggle_switch(
        label='Daf Yomi (On/Off)',
        default_value=False,
        label_after=True,
        inactive_color='#780c21',
        active_color='#0c7822',
        track_color='#0c4c78'
    )

    if daf_yomi:
        # Generate Daf Yomi URL
        today = datetime.now()
        page_number = 3276 + (today - datetime(2024, 7, 3)).days
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
            ">Open PDF</a>
            """,
            unsafe_allow_html=True
        )
    else:
        # URL patterns for different Gemara types and Mesechtot
        url_patterns = {
            "Standard": {
                "ברכות": "https://example.com/standard/berachot.pdf",
                "כריתות": "https://example.com/standard/keritut.pdf",
                "הוריות": "https://example.com/standard/horiot.pdf",
                "מגילה": "https://example.com/standard/megila.pdf",
                "סנהדרין": "https://example.com/standard/sanhedrin.pdf",
                "תענית": "https://example.com/standard/taanit.pdf",
                "מועד קטן": "https://example.com/standard/moed_katan.pdf",
                "סוטה": "https://example.com/standard/sota.pdf",
                "ערכין": "https://example.com/standard/erchin.pdf",
                "מכות": "https://example.com/standard/makkot.pdf",
                "שבת": "https://example.com/standard/shabbat.pdf",
                "קידושין": "https://example.com/standard/kidushin.pdf",
                "חגיגה": "https://example.com/standard/chagiga.pdf",
                "בבא מציעא": "https://example.com/standard/baba_metzia.pdf",
                "בבא קמא": "https://example.com/standard/baba_kama.pdf",
                "עבודה זרה": "https://example.com/standard/avoda_zara.pdf",
                "תמורה": "https://example.com/standard/tmura.pdf",
                "נידה": "https://example.com/standard/nida.pdf",
                "יבמות": "https://example.com/standard/yebamot.pdf",
                "ראש השנה": "https://example.com/standard/rosh_hashana.pdf",
                "פסחים": "https://example.com/standard/psachim.pdf",
                "גיטין": "https://example.com/standard/gitin.pdf",
                "בכורות": "https://example.com/standard/bekhorot.pdf",
                "שבועות": "https://example.com/standard/shvuot.pdf",
                "מנחות": "https://example.com/standard/menachot.pdf",
                "כתובות": "https://example.com/standard/ketubot.pdf",
                "יומא": "https://example.com/standard/yoma.pdf",
                "עירובין": "https://example.com/standard/eruvin.pdf",
                "ביצה": "https://example.com/standard/beitsa.pdf",
                "חולין": "https://example.com/standard/chullin.pdf",
                "סוכה": "https://example.com/standard/suka.pdf",
                "זבחים": "https://example.com/standard/zebahim.pdf",
                "תמיד": "https://example.com/standard/tamid.pdf",
                "בבא בתרא": "https://example.com/standard/baba_batra.pdf",
                "נזיר": "https://example.com/standard/nazir.pdf",
                "מעילה": "https://example.com/standard/meila.pdf",
                "נדרים": "https://example.com/standard/nedarim.pdf"
            },
            "Artscroll": {
                "ברכות": "https://example.com/artscroll/berachot.pdf",
                "כריתות": "https://example.com/artscroll/keritut.pdf",
                "הוריות": "https://example.com/artscroll/horiot.pdf",
                "מגילה": "https://example.com/artscroll/megila.pdf",
                "סנהדרין": "https://example.com/artscroll/sanhedrin.pdf",
                "תענית": "https://example.com/artscroll/taanit.pdf",
                "מועד קטן": "https://example.com/artscroll/moed_katan.pdf",
                "סוטה": "https://example.com/artscroll/sota.pdf",
                "ערכין": "https://example.com/artscroll/erchin.pdf",
                "מכות": "https://example.com/artscroll/makkot.pdf",
                "שבת": "https://example.com/artscroll/shabbat.pdf",
                "קידושין": "https://example.com/artscroll/kidushin.pdf",
                "חגיגה": "https://example.com/artscroll/chagiga.pdf",
                "בבא מציעא": "https://example.com/artscroll/baba_metzia.pdf",
                "בבא קמא": "https://example.com/artscroll/baba_kama.pdf",
                "עבודה זרה": "https://example.com/artscroll/avoda_zara.pdf",
                "תמורה": "https://example.com/artscroll/tmura.pdf",
                "נידה": "https://example.com/artscroll/nida.pdf",
                "יבמות": "https://example.com/artscroll/yebamot.pdf",
                "ראש השנה": "https://example.com/artscroll/rosh_hashana.pdf",
                "פסחים": "https://example.com/artscroll/psachim.pdf",
                "גיטין": "https://example.com/artscroll/gitin.pdf",
                "בכורות": "https://example.com/artscroll/bekhorot.pdf",
                "שבועות": "https://example.com/artscroll/shvuot.pdf",
                "מנחות": "https://example.com/artscroll/menachot.pdf",
                "כתובות": "https://example.com/artscroll/ketubot.pdf",
                "יומא": "https://example.com/artscroll/yoma.pdf",
                "עירובין": "https://example.com/artscroll/eruvin.pdf",
                "ביצה": "https://example.com/artscroll/beitsa.pdf",
                "חולין": "https://example.com/artscroll/chullin.pdf",
                "סוכה": "https://example.com/artscroll/suka.pdf",
                "זבחים": "https://example.com/artscroll/zebahim.pdf",
                "תמיד": "https://example.com/artscroll/tamid.pdf",
                "בבא בתרא": "https://example.com/artscroll/baba_batra.pdf",
                "נזיר": "https://example.com/artscroll/nazir.pdf",
                "מעילה": "https://example.com/artscroll/meila.pdf",
                "נדרים": "https://example.com/artscroll/nedarim.pdf"
            },
            "Mesivta": {
                "ברכות": "https://example.com/mesivta/berachot.pdf",
                "כריתות": "https://example.com/mesivta/keritut.pdf",
                "הוריות": "https://example.com/mesivta/horiot.pdf",
                "מגילה": "https://example.com/mesivta/megila.pdf",
                "סנהדרין": "https://example.com/mesivta/sanhedrin.pdf",
                "תענית": "https://example.com/mesivta/taanit.pdf",
                "מועד קטן": "https://example.com/mesivta/moed_katan.pdf",
                "סוטה": "https://example.com/mesivta/sota.pdf",
                "ערכין": "https://example.com/mesivta/erchin.pdf",
                "מכות": "https://example.com/mesivta/makkot.pdf",
                "שבת": "https://example.com/mesivta/shabbat.pdf",
                "קידושין": "https://example.com/mesivta/kidushin.pdf",
                "חגיגה": "https://example.com/mesivta/chagiga.pdf",
                "בבא מציעא": "https://example.com/mesivta/baba_metzia.pdf",
                "בבא קמא": "https://example.com/mesivta/baba_kama.pdf",
                "עבודה זרה": "https://example.com/mesivta/avoda_zara.pdf",
                "תמורה": "https://example.com/mesivta/tmura.pdf",
                "נידה": "https://example.com/mesivta/nida.pdf",
                "יבמות": "https://example.com/mesivta/yebamot.pdf",
                "ראש השנה": "https://example.com/mesivta/rosh_hashana.pdf",
                "פסחים": "https://example.com/mesivta/psachim.pdf",
                "גיטין": "https://example.com/mesivta/gitin.pdf",
                "בכורות": "https://example.com/mesivta/bekhorot.pdf",
                "שבועות": "https://example.com/mesivta/shvuot.pdf",
                "מנחות": "https://example.com/mesivta/menachot.pdf",
                "כתובות": "https://example.com/mesivta/ketubot.pdf",
                "יומא": "https://example.com/mesivta/yoma.pdf",
                "עירובין": "https://example.com/mesivta/eruvin.pdf",
                "ביצה": "https://example.com/mesivta/beitsa.pdf",
                "חולין": "https://example.com/mesivta/chullin.pdf",
                "סוכה": "https://example.com/mesivta/suka.pdf",
                "זבחים": "https://example.com/mesivta/zebahim.pdf",
                "תמיד": "https://example.com/mesivta/tamid.pdf",
                "בבא בתרא": "https://example.com/mesivta/baba_batra.pdf",
                "נזיר": "https://example.com/mesivta/nazir.pdf",
                "מעילה": "https://example.com/mesivta/meila.pdf",
                "נדרים": "https://example.com/mesivta/nedarim.pdf"
            },
            "Koren": {
                "ברכות": "https://example.com/koren/berachot.pdf",
                "כריתות": "https://example.com/koren/keritut.pdf",
                "הוריות": "https://example.com/koren/horiot.pdf",
                "מגילה": "https://example.com/koren/megila.pdf",
                "סנהדרין": "https://example.com/koren/sanhedrin.pdf",
                "תענית": "https://example.com/koren/taanit.pdf",
                "מועד קטן": "https://example.com/koren/moed_katan.pdf",
                "סוטה": "https://example.com/koren/sota.pdf",
                "ערכין": "https://example.com/koren/erchin.pdf",
                "מכות": "https://example.com/koren/makkot.pdf",
                "שבת": "https://example.com/koren/shabbat.pdf",
                "קידושין": "https://example.com/koren/kidushin.pdf",
                "חגיגה": "https://example.com/koren/chagiga.pdf",
                "בבא מציעא": "https://example.com/koren/baba_metzia.pdf",
                "בבא קמא": "https://example.com/koren/baba_kama.pdf",
                "עבודה זרה": "https://example.com/koren/avoda_zara.pdf",
                "תמורה": "https://example.com/koren/tmura.pdf",
                "נידה": "https://example.com/koren/nida.pdf",
                "יבמות": "https://example.com/koren/yebamot.pdf",
                "ראש השנה": "https://example.com/koren/rosh_hashana.pdf",
                "פסחים": "https://example.com/koren/psachim.pdf",
                "גיטין": "https://example.com/koren/gitin.pdf",
                "בכורות": "https://example.com/koren/bekhorot.pdf",
                "שבועות": "https://example.com/koren/shvuot.pdf",
                "מנחות": "https://example.com/koren/menachot.pdf",
                "כתובות": "https://example.com/koren/ketubot.pdf",
                "יומא": "https://example.com/koren/yoma.pdf",
                "עירובין": "https://example.com/koren/eruvin.pdf",
                "ביצה": "https://example.com/koren/beitsa.pdf",
                "חולין": "https://example.com/koren/chullin.pdf",
                "סוכה": "https://example.com/koren/suka.pdf",
                "זבחים": "https://example.com/koren/zebahim.pdf",
                "תמיד": "https://example.com/koren/tamid.pdf",
                "בבא בתרא": "https://example.com/koren/baba_batra.pdf",
                "נזיר": "https://example.com/koren/nazir.pdf",
                "מעילה": "https://example.com/koren/meila.pdf",
                "נדרים": "https://example.com/koren/nedarim.pdf"
            }
        }

        # Generate the URL based on selected type and Mesechta
        selected_url = url_patterns.get(option, {}).get(mesechta, "#")

        # Create a button to open the selected URL
        st.markdown(
            f"""
            <a href="{selected_url}" target="_blank" style="
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

        # Show "Drive" and "View" buttons
        st.markdown(
            """
            <div class="extra-buttons">
                <a href="https://example.com/drive" target="_blank">Drive</a>
                <a href="https://example.com/view" target="_blank">View</a>
            </div>
            """,
            unsafe_allow_html=True
        )

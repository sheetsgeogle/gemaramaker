import streamlit as st
import streamlit_toggle as stt
from datetime import datetime

# Streamlit app title
st.title("Gemara Library")

# Custom CSS to adjust button and element styling
st.markdown("""
    <style>
        .main {
            padding: 1em;
            border: none;  /* Removed the rounded rectangle border */
            background-color: #f9f9f9;
        }
        .stButton>button {
            border-radius: 5px; /* Adjusted button border radius */
        }
        .stSelectbox {
            border-radius: 5px; /* Adjusted select box border radius */
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
            border-radius: 5px; /* Adjusted button border radius */
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

    # URL patterns for different Gemara types, Mesechtot, and extra buttons
    url_patterns = {
        "Standard": {
            "ברכות": {"drive": "https://drive.google.com/drive/folders/1", "view": "https://example.com/standard/berachot_view"},
            "כריתות": {"drive": "https://drive.google.com/drive/folders/2", "view": "https://example.com/standard/keritut_view"},
            "הוריות": {"drive": "https://drive.google.com/drive/folders/3", "view": "https://example.com/standard/horyot_view"},
            "מגילה": {"drive": "https://drive.google.com/drive/folders/4", "view": "https://example.com/standard/megila_view"},
            "סנהדרין": {"drive": "https://drive.google.com/drive/folders/5", "view": "https://example.com/standard/sanhedrin_view"},
            "תענית": {"drive": "https://drive.google.com/drive/folders/6", "view": "https://example.com/standard/taanit_view"},
            "מועד קטן": {"drive": "https://drive.google.com/drive/folders/7", "view": "https://example.com/standard/moed_katan_view"},
            "סוטה": {"drive": "https://drive.google.com/drive/folders/8", "view": "https://example.com/standard/sota_view"},
            "ערכין": {"drive": "https://drive.google.com/drive/folders/9", "view": "https://example.com/standard/erchin_view"},
            "מכות": {"drive": "https://drive.google.com/drive/folders/10", "view": "https://example.com/standard/makot_view"},
            "שבת": {"drive": "https://drive.google.com/drive/folders/11", "view": "https://example.com/standard/shabbat_view"},
            "קידושין": {"drive": "https://drive.google.com/drive/folders/12", "view": "https://example.com/standard/kidushin_view"},
            "חגיגה": {"drive": "https://drive.google.com/drive/folders/13", "view": "https://example.com/standard/chagiga_view"},
            "בבא מציעא": {"drive": "https://drive.google.com/drive/folders/14", "view": "https://example.com/standard/baba_metzia_view"},
            "בבא קמא": {"drive": "https://drive.google.com/drive/folders/15", "view": "https://example.com/standard/baba_kama_view"},
            "עבודה זרה": {"drive": "https://drive.google.com/drive/folders/16", "view": "https://example.com/standard/avoda_zara_view"},
            "תמורה": {"drive": "https://drive.google.com/drive/folders/17", "view": "https://example.com/standard/tmura_view"},
            "נידה": {"drive": "https://drive.google.com/drive/folders/18", "view": "https://example.com/standard/nida_view"},
            "יבמות": {"drive": "https://drive.google.com/drive/folders/19", "view": "https://example.com/standard/yebamot_view"},
            "ראש השנה": {"drive": "https://drive.google.com/drive/folders/20", "view": "https://example.com/standard/rosh_hashana_view"},
            "פסחים": {"drive": "https://drive.google.com/drive/folders/21", "view": "https://example.com/standard/pesachim_view"},
            "גיטין": {"drive": "https://drive.google.com/drive/folders/22", "view": "https://example.com/standard/gittin_view"},
            "בכורות": {"drive": "https://drive.google.com/drive/folders/23", "view": "https://example.com/standard/bechorot_view"},
            "שבועות": {"drive": "https://drive.google.com/drive/folders/24", "view": "https://example.com/standard/shavuot_view"},
            "מנחות": {"drive": "https://drive.google.com/drive/folders/25", "view": "https://example.com/standard/minhot_view"},
            "כתובות": {"drive": "https://drive.google.com/drive/folders/26", "view": "https://example.com/standard/ketubot_view"},
            "יומא": {"drive": "https://drive.google.com/drive/folders/27", "view": "https://example.com/standard/yoma_view"},
            "עירובין": {"drive": "https://drive.google.com/drive/folders/28", "view": "https://example.com/standard/eruvin_view"},
            "ביצה": {"drive": "https://drive.google.com/drive/folders/29", "view": "https://example.com/standard/beitza_view"},
            "חולין": {"drive": "https://drive.google.com/drive/folders/30", "view": "https://example.com/standard/chullin_view"},
            "סוכה": {"drive": "https://drive.google.com/drive/folders/31", "view": "https://example.com/standard/sukkah_view"},
            "זבחים": {"drive": "https://drive.google.com/drive/folders/32", "view": "https://example.com/standard/zebachim_view"},
            "תמיד": {"drive": "https://drive.google.com/drive/folders/33", "view": "https://example.com/standard/tamid_view"},
            "בבא בתרא": {"drive": "https://drive.google.com/drive/folders/34", "view": "https://example.com/standard/baba_batra_view"},
            "נזיר": {"drive": "https://drive.google.com/drive/folders/35", "view": "https://example.com/standard/nazir_view"},
            "מעילה": {"drive": "https://drive.google.com/drive/folders/36", "view": "https://example.com/standard/meilah_view"},
            "נדרים": {"drive": "https://drive.google.com/drive/folders/37", "view": "https://example.com/standard/nedarim_view"}
        },
        "Artscroll": {
            "ברכות": {"drive": "https://drive.google.com/drive/folders/38", "view": "https://example.com/artscroll/berachot_view"},
            "כריתות": {"drive": "https://drive.google.com/drive/folders/39", "view": "https://example.com/artscroll/keritut_view"},
            "הוריות": {"drive": "https://drive.google.com/drive/folders/40", "view": "https://example.com/artscroll/horyot_view"},
            "מגילה": {"drive": "https://drive.google.com/drive/folders/41", "view": "https://example.com/artscroll/megila_view"},
            "סנהדרין": {"drive": "https://drive.google.com/drive/folders/42", "view": "https://example.com/artscroll/sanhedrin_view"},
            "תענית": {"drive": "https://drive.google.com/drive/folders/43", "view": "https://example.com/artscroll/taanit_view"},
            "מועד קטן": {"drive": "https://drive.google.com/drive/folders/44", "view": "https://example.com/artscroll/moed_katan_view"},
            "סוטה": {"drive": "https://drive.google.com/drive/folders/45", "view": "https://example.com/artscroll/sota_view"},
            "ערכין": {"drive": "https://drive.google.com/drive/folders/46", "view": "https://example.com/artscroll/erchin_view"},
            "מכות": {"drive": "https://drive.google.com/drive/folders/47", "view": "https://example.com/artscroll/makot_view"},
            "שבת": {"drive": "https://drive.google.com/drive/folders/48", "view": "https://example.com/artscroll/shabbat_view"},
            "קידושין": {"drive": "https://drive.google.com/drive/folders/49", "view": "https://example.com/artscroll/kidushin_view"},
            "חגיגה": {"drive": "https://drive.google.com/drive/folders/50", "view": "https://example.com/artscroll/chagiga_view"},
            "בבא מציעא": {"drive": "https://drive.google.com/drive/folders/51", "view": "https://example.com/artscroll/baba_metzia_view"},
            "בבא קמא": {"drive": "https://drive.google.com/drive/folders/52", "view": "https://example.com/artscroll/baba_kama_view"},
            "עבודה זרה": {"drive": "https://drive.google.com/drive/folders/53", "view": "https://example.com/artscroll/avoda_zara_view"},
            "תמורה": {"drive": "https://drive.google.com/drive/folders/54", "view": "https://example.com/artscroll/tmura_view"},
            "נידה": {"drive": "https://drive.google.com/drive/folders/55", "view": "https://example.com/artscroll/nida_view"},
            "יבמות": {"drive": "https://drive.google.com/drive/folders/56", "view": "https://example.com/artscroll/yebamot_view"},
            "ראש השנה": {"drive": "https://drive.google.com/drive/folders/57", "view": "https://example.com/artscroll/rosh_hashana_view"},
            "פסחים": {"drive": "https://drive.google.com/drive/folders/58", "view": "https://example.com/artscroll/pesachim_view"},
            "גיטין": {"drive": "https://drive.google.com/drive/folders/59", "view": "https://example.com/artscroll/gittin_view"},
            "בכורות": {"drive": "https://drive.google.com/drive/folders/60", "view": "https://example.com/artscroll/bechorot_view"},
            "שבועות": {"drive": "https://drive.google.com/drive/folders/61", "view": "https://example.com/artscroll/shavuot_view"},
            "מנחות": {"drive": "https://drive.google.com/drive/folders/62", "view": "https://example.com/artscroll/minhot_view"},
            "כתובות": {"drive": "https://drive.google.com/drive/folders/63", "view": "https://example.com/artscroll/ketubot_view"},
            "יומא": {"drive": "https://drive.google.com/drive/folders/64", "view": "https://example.com/artscroll/yoma_view"},
            "עירובין": {"drive": "https://drive.google.com/drive/folders/65", "view": "https://example.com/artscroll/eruvin_view"},
            "ביצה": {"drive": "https://drive.google.com/drive/folders/66", "view": "https://example.com/artscroll/beitza_view"},
            "חולין": {"drive": "https://drive.google.com/drive/folders/67", "view": "https://example.com/artscroll/chullin_view"},
            "סוכה": {"drive": "https://drive.google.com/drive/folders/68", "view": "https://example.com/artscroll/sukkah_view"},
            "זבחים": {"drive": "https://drive.google.com/drive/folders/69", "view": "https://example.com/artscroll/zebachim_view"},
            "תמיד": {"drive": "https://drive.google.com/drive/folders/70", "view": "https://example.com/artscroll/tamid_view"},
            "בבא בתרא": {"drive": "https://drive.google.com/drive/folders/71", "view": "https://example.com/artscroll/baba_batra_view"},
            "נזיר": {"drive": "https://drive.google.com/drive/folders/72", "view": "https://example.com/artscroll/nazir_view"},
            "מעילה": {"drive": "https://drive.google.com/drive/folders/73", "view": "https://example.com/artscroll/meilah_view"},
            "נדרים": {"drive": "https://drive.google.com/drive/folders/74", "view": "https://example.com/artscroll/nedarim_view"}
        },
        "Mesivta": {
            "ברכות": {"drive": "https://drive.google.com/drive/folders/75", "view": "https://example.com/mesivta/berachot_view"},
            "כריתות": {"drive": "https://drive.google.com/drive/folders/76", "view": "https://example.com/mesivta/keritut_view"},
            "הוריות": {"drive": "https://drive.google.com/drive/folders/77", "view": "https://example.com/mesivta/horyot_view"},
            "מגילה": {"drive": "https://drive.google.com/drive/folders/78", "view": "https://example.com/mesivta/megila_view"},
            "סנהדרין": {"drive": "https://drive.google.com/drive/folders/79", "view": "https://example.com/mesivta/sanhedrin_view"},
            "תענית": {"drive": "https://drive.google.com/drive/folders/80", "view": "https://example.com/mesivta/taanit_view"},
            "מועד קטן": {"drive": "https://drive.google.com/drive/folders/81", "view": "https://example.com/mesivta/moed_katan_view"},
            "סוטה": {"drive": "https://drive.google.com/drive/folders/82", "view": "https://example.com/mesivta/sota_view"},
            "ערכין": {"drive": "https://drive.google.com/drive/folders/83", "view": "https://example.com/mesivta/erchin_view"},
            "מכות": {"drive": "https://drive.google.com/drive/folders/84", "view": "https://example.com/mesivta/makot_view"},
            "שבת": {"drive": "https://drive.google.com/drive/folders/85", "view": "https://example.com/mesivta/shabbat_view"},
            "קידושין": {"drive": "https://drive.google.com/drive/folders/86", "view": "https://example.com/mesivta/kidushin_view"},
            "חגיגה": {"drive": "https://drive.google.com/file/d/1iGb2-0IL3m-tdHlk7qglIwvvsd_p6a-J/view?usp=sharing", "view": "https://ia600408.us.archive.org/24/items/13_20240704/%D7%92%D7%9E%D7%A8%D7%90%20%D7%9E%D7%AA%D7%99%D7%91%D7%AA%D7%90%2013%20%D7%97%D7%92%D7%99%D7%92%D7%94.pdf"},
            "בבא מציעא": {"drive": "https://drive.google.com/drive/folders/88", "view": "https://example.com/mesivta/baba_metzia_view"},
            "בבא קמא": {"drive": "https://drive.google.com/drive/folders/89", "view": "https://example.com/mesivta/baba_kama_view"},
            "עבודה זרה": {"drive": "https://drive.google.com/drive/folders/90", "view": "https://example.com/mesivta/avoda_zara_view"},
            "תמורה": {"drive": "https://drive.google.com/drive/folders/91", "view": "https://example.com/mesivta/tmura_view"},
            "נידה": {"drive": "https://drive.google.com/drive/folders/92", "view": "https://example.com/mesivta/nida_view"},
            "יבמות": {"drive": "https://drive.google.com/drive/folders/93", "view": "https://example.com/mesivta/yebamot_view"},
            "ראש השנה": {"drive": "https://drive.google.com/drive/folders/94", "view": "https://example.com/mesivta/rosh_hashana_view"},
            "פסחים": {"drive": "https://drive.google.com/drive/folders/95", "view": "https://example.com/mesivta/pesachim_view"},
            "גיטין": {"drive": "https://drive.google.com/drive/folders/96", "view": "https://example.com/mesivta/gittin_view"},
            "בכורות": {"drive": "https://drive.google.com/drive/folders/97", "view": "https://example.com/mesivta/bechorot_view"},
            "שבועות": {"drive": "https://drive.google.com/drive/folders/98", "view": "https://example.com/mesivta/shavuot_view"},
            "מנחות": {"drive": "https://drive.google.com/drive/folders/99", "view": "https://example.com/mesivta/minhot_view"},
            "כתובות": {"drive": "https://drive.google.com/drive/folders/100", "view": "https://example.com/mesivta/ketubot_view"},
            "יומא": {"drive": "https://drive.google.com/drive/folders/101", "view": "https://example.com/mesivta/yoma_view"},
            "עירובין": {"drive": "https://drive.google.com/drive/folders/102", "view": "https://example.com/mesivta/eruvin_view"},
            "ביצה": {"drive": "https://drive.google.com/drive/folders/103", "view": "https://example.com/mesivta/beitza_view"},
            "חולין": {"drive": "https://drive.google.com/drive/folders/104", "view": "https://example.com/mesivta/chullin_view"},
            "סוכה": {"drive": "https://drive.google.com/drive/folders/105", "view": "https://example.com/mesivta/sukkah_view"},
            "זבחים": {"drive": "https://drive.google.com/drive/folders/106", "view": "https://example.com/mesivta/zebachim_view"},
            "תמיד": {"drive": "https://drive.google.com/drive/folders/107", "view": "https://example.com/mesivta/tamid_view"},
            "בבא בתרא": {"drive": "https://drive.google.com/drive/folders/108", "view": "https://example.com/mesivta/baba_batra_view"},
            "נזיר": {"drive": "https://drive.google.com/drive/folders/109", "view": "https://example.com/mesivta/nazir_view"},
            "מעילה": {"drive": "https://drive.google.com/drive/folders/110", "view": "https://example.com/mesivta/meilah_view"},
            "נדרים": {"drive": "https://drive.google.com/drive/folders/111", "view": "https://example.com/mesivta/nedarim_view"}
        },
        "Koren": {
            "ברכות": {"drive": "https://drive.google.com/drive/folders/112", "view": "https://example.com/koren/berachot_view"},
            "כריתות": {"drive": "https://drive.google.com/drive/folders/113", "view": "https://example.com/koren/keritut_view"},
            "הוריות": {"drive": "https://drive.google.com/drive/folders/114", "view": "https://example.com/koren/horyot_view"},
            "מגילה": {"drive": "https://drive.google.com/drive/folders/115", "view": "https://example.com/koren/megila_view"},
            "סנהדרין": {"drive": "https://drive.google.com/drive/folders/116", "view": "https://example.com/koren/sanhedrin_view"},
            "תענית": {"drive": "https://drive.google.com/drive/folders/117", "view": "https://example.com/koren/taanit_view"},
            "מועד קטן": {"drive": "https://drive.google.com/drive/folders/118", "view": "https://example.com/koren/moed_katan_view"},
            "סוטה": {"drive": "https://drive.google.com/drive/folders/119", "view": "https://example.com/koren/sota_view"},
            "ערכין": {"drive": "https://drive.google.com/drive/folders/120", "view": "https://example.com/koren/erchin_view"},
            "מכות": {"drive": "https://drive.google.com/drive/folders/121", "view": "https://example.com/koren/makot_view"},
            "שבת": {"drive": "https://drive.google.com/drive/folders/122", "view": "https://example.com/koren/shabbat_view"},
            "קידושין": {"drive": "https://drive.google.com/drive/folders/123", "view": "https://example.com/koren/kidushin_view"},
            "חגיגה": {"drive": "https://drive.google.com/drive/folders/124", "view": "https://example.com/koren/chagiga_view"},
            "בבא מציעא": {"drive": "https://drive.google.com/drive/folders/125", "view": "https://example.com/koren/baba_metzia_view"},
            "בבא קמא": {"drive": "https://drive.google.com/drive/folders/126", "view": "https://example.com/koren/baba_kama_view"},
            "עבודה זרה": {"drive": "https://drive.google.com/drive/folders/127", "view": "https://example.com/koren/avoda_zara_view"},
            "תמורה": {"drive": "https://drive.google.com/drive/folders/128", "view": "https://example.com/koren/tmura_view"},
            "נידה": {"drive": "https://drive.google.com/drive/folders/129", "view": "https://example.com/koren/nida_view"},
            "יבמות": {"drive": "https://drive.google.com/drive/folders/130", "view": "https://example.com/koren/yebamot_view"},
            "ראש השנה": {"drive": "https://drive.google.com/drive/folders/131", "view": "https://example.com/koren/rosh_hashana_view"},
            "פסחים": {"drive": "https://drive.google.com/drive/folders/132", "view": "https://example.com/koren/pesachim_view"},
            "גיטין": {"drive": "https://drive.google.com/drive/folders/133", "view": "https://example.com/koren/gittin_view"},
            "בכורות": {"drive": "https://drive.google.com/drive/folders/134", "view": "https://example.com/koren/bechorot_view"},
            "שבועות": {"drive": "https://drive.google.com/drive/folders/135", "view": "https://example.com/koren/shavuot_view"},
            "מנחות": {"drive": "https://drive.google.com/drive/folders/136", "view": "https://example.com/koren/minhot_view"},
            "כתובות": {"drive": "https://drive.google.com/drive/folders/137", "view": "https://example.com/koren/ketubot_view"},
            "יומא": {"drive": "https://drive.google.com/drive/folders/138", "view": "https://example.com/koren/yoma_view"},
            "עירובין": {"drive": "https://drive.google.com/drive/folders/139", "view": "https://example.com/koren/eruvin_view"},
            "ביצה": {"drive": "https://drive.google.com/drive/folders/140", "view": "https://example.com/koren/beitza_view"},
            "חולין": {"drive": "https://drive.google.com/drive/folders/141", "view": "https://example.com/koren/chullin_view"},
            "סוכה": {"drive": "https://drive.google.com/drive/folders/142", "view": "https://example.com/koren/sukkah_view"},
            "זבחים": {"drive": "https://drive.google.com/drive/folders/143", "view": "https://example.com/koren/zebachim_view"},
            "תמיד": {"drive": "https://drive.google.com/drive/folders/144", "view": "https://example.com/koren/tamid_view"},
            "בבא בתרא": {"drive": "https://drive.google.com/drive/folders/145", "view": "https://example.com/koren/baba_batra_view"},
            "נזיר": {"drive": "https://drive.google.com/drive/folders/146", "view": "https://example.com/koren/nazir_view"},
            "מעילה": {"drive": "https://drive.google.com/drive/folders/147", "view": "https://example.com/koren/meilah_view"},
            "נדרים": {"drive": "https://drive.google.com/drive/folders/148", "view": "https://example.com/koren/nedarim_view"}
        }
    }

# Initialize Streamlit app
st.title('Talmud Texts Links')

# Dropdown for selecting publisher
publisher = st.selectbox("Select Publisher", ["ArtScroll", "Mesivta", "Koren"])

# Dropdown for selecting tractate
tractate = st.selectbox("Select Tractate", list(data[publisher].keys()))

# Display links based on selected publisher and tractate
if publisher and tractate:
    links = data[publisher][tractate]
    st.subheader(f"Links for {tractate}")
    st.write(f"[Drive Link]({links['drive']})")
    st.write(f"[View Link]({links['view']})")

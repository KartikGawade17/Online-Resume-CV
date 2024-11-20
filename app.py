from pathlib import Path

import streamlit as st
from PIL import Image

#income and expense tracker using machine learning or deep learing

current_dir = Path("D:\online cv").parent if "D:\online cv" in locals() else Path.cwd()
css_file = current_dir / "main.css"
resume_file = current_dir / "assets" / "resume.pdf" 
profile_pic = current_dir / "assets" / "hero.jpg"


PAGE_TITLE = "Digital CV | Kartik Gawade"
PAGE_ICON = ":wave:"
NAME = "Kartik Gawade"
DESCRIPTION = """
Data Science Enthusiast seeking to gain hands-on experience in data science,.Data Analytics and Machine Learning.
"""
EMAIL = "kartikgawadeds17@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/kartik-gawade-023b24300/",
    "GitHub": "https://github.com/KartikGawade17",
    "Whatsapp": "https://wa.me/qr/DNS3X2PKR7UJJ1",
}

PROJECTS = {
    "🏆 Toxic Comment Analyzer - Gradio app and Deep learning",
    "🏆 Crime Against Women (2019 - 2022) - Analytics, Power BI",
    "🏆 Adventure Works Report (2020 - 2022) - Analytics Project, Power BI, Excel",
    "🏆 Insurance price prediction - Machine Learning (Supervised), Regression",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
if resume_file.exists():
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
        print("Resume file read successfully!")
else:
    print(f"Error: Resume file not found at {resume_file}")
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.Image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Education")
st.write("---")
st.write(
    """
- ✔️ Sindhudurg Sainik School | S.S.C. | Sindhudurg, Maharashtra | Jun 2013 – Mar 2019
- ✔️ Sindhudurg Sainik School | H.S.C. | Sindhudurg, Maharashtra | Jun 2019 – Mar 2021 
- ✔️ KES Shroff College | BSc Data Science | Mumbai, India | Jul 2021 – May 2024
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, Machine Learning, Deep Learning
- 📊 Data Visulization: PowerBi
- 📚 Modeling: linear regression, decision tree, Random Forest
- 🗄️ Databases: MySQL
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
st.write(
    """
- 🏆 Toxic Comment Analyzer - Gradio app and Deep learning
- 🏆 Crime Against Women (2019 - 2022) - Analytics, Power BI
- 🏆 Adventure Works Report (2020 - 2022) - Analytics Project, Power BI, Excel
- 🏆 Insurance price prediction - Machine Learning (Supervised), Regression
"""
)

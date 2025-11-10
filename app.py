from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent
css_file = current_dir / "main.css"
resume_file = current_dir / "Kartik_Updated_resume.pdf"
profile_pic = current_dir / "profile-pic (1).png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio | Kartik Gawade"
PAGE_ICON = "💼"
NAME = "Kartik Gawade"
DESCRIPTION = """
Data Science Enthusiast | M.Sc. Artificial Intelligence Student | Passionate about Data Analytics & Machine Learning.
"""
EMAIL = "kartikgawadeds17@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/kartik-gawade-023b24300",
    "GitHub": "https://github.com/KartikGawade17",
}
PROJECTS = [
    "🏆 UFC Fight Outcome Prediction — Machine Learning model with 84.17% accuracy trained on data scraped from the official UFC Stats website; deployed using Streamlit.",
    "🏆 Crime Hotspot Analysis (India) — AI-based system predicting regional safety scores using NCRB data (2019–2023).",
    "🏆 Crime Against Women (2019–2022) — Analytical Power BI dashboard using NCRB data to identify trends and patterns in reported cases.",
    "🏆 Adventure Works Report (2020–2022) — Power BI dashboard visualizing product, customer, and sales insights.",
]

# --- PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# --- SIDEBAR (Personal Info) ---
with st.sidebar:
    st.image(profile_pic, width=150)
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫", EMAIL)
    for platform, link in SOCIAL_MEDIA.items():
        st.markdown(f"[{platform}]({link})")
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

# --- MAIN CONTENT ---
st.title("📊 My Portfolio")
st.write("---")

# --- EDUCATION ---
st.subheader("🎓 Education")
st.write(
    """
- KES’s Shroff College, Mumbai — **M.Sc. Artificial Intelligence** | 2024 – Present  
- KES’s Shroff College, Mumbai — **B.Sc. Data Science** | 2021 – 2024  
- Sindhudurg Sainik School — **H.S.C. & S.S.C.** | 2013 – 2021
"""
)

# --- SKILLS ---
st.subheader("🧠 Technical Skills")
st.write(
    """
- **Programming:** Python (Pandas, NumPy, Scikit-learn, TensorFlow), SQL  
- **Data Visualization:** Power BI, Excel, Matplotlib  
- **Databases:** MySQL, PostgreSQL  
- **Machine Learning:** Linear Regression, Decision Trees, Random Forest, Classification Models  
- **Tools:** Git, Streamlit, Jupyter Notebook
"""
)

# --- CERTIFICATIONS ---
st.subheader("📜 Certifications")
st.write(
    """
- Microsoft (Azure Data Fundamentals) | DP-900 | Score: 835/1000  
- Oracle Certified (Data Foundation) | Score: 83%  
- Python Bootcamp | Udemy  
- Python for Machine Learning | Great Learning  
- Power BI Desktop & Business Intelligence | Udemy
"""
)

# --- PROJECTS ---
st.subheader("🚀 Projects")
for project in PROJECTS:
    st.write(project)

# --- CONTACT INFO ---
st.write("---")
st.subheader("📩 Get in Touch")
st.write("If you’d like to collaborate or discuss data-driven projects, feel free to reach out!")
st.write("📧", EMAIL)
for platform, link in SOCIAL_MEDIA.items():
    st.markdown(f"[{platform}]({link})")

st.write("---")
st.caption("© 2025 Kartik Gawade | Built with Streamlit")

from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(r"D:\online cv") if Path(r"D:\online cv").exists() else Path.cwd()
css_file = current_dir / "main.css"
resume_file = current_dir / "resume.pdf"
profile_pic_path = current_dir / "hero.jpg"

PAGE_TITLE = "Digital CV | Kartik Gawade"
PAGE_ICON = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Debug paths
print(f"CSS File Path: {css_file} | Exists: {css_file.exists()}")
print(f"Resume File Path: {resume_file} | Exists: {resume_file.exists()}")
print(f"Profile Picture Path: {profile_pic_path} | Exists: {profile_pic_path.exists()}")

# Load CSS
if css_file.exists():
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
else:
    st.error("CSS file not found.")

# Load Resume
if resume_file.exists():
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
else:
    st.error("Resume file not found.")

# Load Profile Picture
try:
    if profile_pic_path.exists():
        profile_pic = Image.open(profile_pic_path)
    else:
        raise FileNotFoundError("Profile picture not found.")
except Exception as e:
    st.error(f"Error loading profile picture: {e}")

# Hero Section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)
with col2:
    st.title("Kartik Gawade")
    st.write("Data Science Enthusiast...")
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name="resume.pdf",
        mime="application/octet-stream",
    )


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

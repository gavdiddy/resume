from pathlib import Path

import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resumePDF.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


PAGE_TITLE = "Resume | Gavin Winot"
PAGE_ICON= ":wave:"
NAME = "Gavin Winot"
DESCRIPTION = """
Data Analyst, degree from Eastern Connecticut State University
"""
EMAIL = "winotg@my.easternct.edu"
SOCIAL_MEDIA={
    "Instagram": "https://www.instagram.com/",
    "Twitter": "https://twitter.com/",
    "Facebook": "https://facebook.com/",
    "YouTube":"https://youtube.com/",
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📜 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(EMAIL)

cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- 4 years of coding experience
- Degree in computer science from Eastern Connecticut State University
- Over a decade of experience working on a team
- Strong background in math and computers
"""
)

st.write("#")
st.subheader("Skills")
st.write(
    """
- Javascript, Python, HTML
- All microsoft formats(Word, Powerpoint, Excel, etc)
- Calculus and Statistics
- Teamwork and working with others
"""
)

st.write("#")
st.subheader("Previous Work")
st.write("---")

st.write("Computer Science student at ECSU 2022-2025")
st.write("""Taking classes such as web development, computer architecture, python courses and javascript courses
         """
         )
st.write("#")
st.write("Fedex 2021-Present")
st.write(
    """Worked as a package handler at FedEx for several years, a job that requires hard work, team work and consistency
    """
)




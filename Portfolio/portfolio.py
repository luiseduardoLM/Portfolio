import streamlit as st
import streamlit_shadcn_ui as ui

resume_file ="Documentos/cv.pdf"
resume_file_name = "cv.pdf"

layout = "centered"
page_title = "Portfolio | Luis Eduardo Martínez"
page_icon = ""
name="Luis Eduardo Martínez Gudiño"
description=""
email="luiseduardo@ciencias.unam.mx"

social_media = {
    "LinkedIn":"https://www.linkedin.com/in/luis-eduardo-mart%C3%ADnez-gudi%C3%B1o-a498a120b/",
    "GitHub":"https://github.com/luiseduardoLM"
}

#Config de la pagina
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    
#Links Redes Sociales
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    with cols[index]:
        ui.link_button(text=platform, url=link, key=f"link_btn{platform}")

# Cabecera
cols1 = st.columns(1) # Realmente no hace ponerlo en forma de lista, ya que s una simple columna
with cols1[0]:
    st.title(name)
    st.write(description)
    st.download_button(
        label="Descargar CV",
        data=PDFbyte,
        file_name=resume_file_name
    )
    st.write(email)
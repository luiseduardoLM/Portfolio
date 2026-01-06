import streamlit as st
import streamlit_shadcn_ui as ui

# Guarda el pdf 
resume_file ="Documentos/cv.pdf"
resume_file_name = "cv.pdf"

# Guarda el css
css_file = "styles/main.css"

layout = "centered"
page_title = "Portfolio | Luis Eduardo Martínez"
page_icon = "💻"
name="Luis Eduardo Martínez Gudiño"
description=""
email="luiseduardo@ciencias.unam.mx"

social_media = {
    "LinkedIn":"https://www.linkedin.com/in/luis-eduardo-mart%C3%ADnez-gudi%C3%B1o-a498a120b/",
    "GitHub":"https://github.com/luiseduardoLM"
}

proyectos = {
    "Primer proyecto":"Link",
    "Segundo proyecto":"Link",
    "Tercer proyecto":"Link"
}
#Config de la pagina
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

# Cargar css y pdf

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

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
    
    
# Proyectos

st.write("##")
st.subheader("Proyectos")
st.write("---")

for project, link in proyectos.items():
    st.write(f"[{project}]({link})")


# Habilidades tenicas

st.write("##")
st.subheader("Habilidades tecnicas")
st.write("---")
st.write(
"""        
- Programación: Python, R
- Base datos: MySQL, PostgreSQL   
- Visualización: Power BI
- Paquetería Office: Excel, Word

"""         
)


# Experiencia

st.write("##")
st.subheader("Experiencia")
st.write("---")

# Servicio Social

st.write(" Servicio Social: Instituto de Geofísica, UNAM")
st.write("5/2025 - Presente")
st.write(
"""
- ▶  Capacitación en herramientas tecnológicas y ciencia de datos.
- ▶  Apoyo en la generación y revisión de materiales académicos.
- ▶  Revisión, análisis y visualización de bases de datos.

"""      
)
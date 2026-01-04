import streamlit as st
import streamlit_shadcn_ui as ui

layout = "centered"
page_title = "Portfolio | Luis Eduardo Martínez"
page_icon = ""

social_media = {
    "LinkedIn":"https://www.linkedin.com/in/luis-eduardo-mart%C3%ADnez-gudi%C3%B1o-a498a120b/",
    "GitHub":"https://github.com/luiseduardoLM"
}

#Config de la pagina
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

#Links Redes Sociales
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    with cols[index]:
        ui.link_button(text=platform, url=link, key=f"link_btn{platform}")

# Cabecera
cols1 = st.columns(1)
with cols1:
    
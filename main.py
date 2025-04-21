#from rembg import remove
#from PIL import Image

#caminho_entrada = 'image2.jpg'
#caminho_saida = 'image1_ok.png'

#entrada = Image.open(caminho_entrada)
#saida = remove(entrada)

#saida.save(caminho_saida) 

import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="Removedor de Fundo", page_icon="🖼️")

st.title("🖼️ Removedor de Fundo de Imagens")
st.write("Faça upload de uma imagem e veja o fundo ser removido automaticamente!")

# Upload da imagem
imagem_enviada = st.file_uploader("Escolha uma imagem", type=["png", "jpg", "jpeg"])

if imagem_enviada is not None:
    # Exibe imagem original
    imagem_original = Image.open(imagem_enviada).convert("RGBA")
    st.subheader("Imagem Original")
    st.image(imagem_original, use_column_width=True)

    # Remove fundo
    with st.spinner("Removendo fundo..."):
        imagem_sem_fundo = remove(imagem_original)

    # Exibe imagem modificada
    st.subheader("Imagem sem fundo")
    st.image(imagem_sem_fundo, use_column_width=True)

    # Botão para download
    img_bytes = io.BytesIO()
    imagem_sem_fundo.save(img_bytes, format="PNG")
    st.download_button(
        label="📥 Baixar imagem sem fundo",
        data=img_bytes.getvalue(),
        file_name="imagem_sem_fundo.png",
        mime="image/png"
    )

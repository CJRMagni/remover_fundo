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
import requests
from io import BytesIO

st.set_page_config(page_title="Remover Fundo", layout="centered")

st.title("🖼️ Removedor de Fundo de Imagens")

# Pega a URL da imagem pela query string
query_params = st.experimental_get_query_params()
img_url = query_params.get("img_url", [None])[0]

if not img_url:
    st.info("Adicione `?img_url=SUA_IMAGEM` na URL para remover o fundo.")
    st.stop()

st.write("🔗 URL da imagem recebida:")
st.code(img_url)

try:
    st.write("📥 Baixando imagem...")
    response = requests.get(img_url)
    response.raise_for_status()

    input_image = Image.open(BytesIO(response.content)).convert("RGBA")
    st.image(input_image, caption="Imagem original", use_column_width=True)

    st.write("✂️ Removendo fundo...")
    output_image = remove(input_image)

    st.image(output_image, caption="Imagem sem fundo", use_column_width=True)

    # Gerar botão para download da imagem
    buf = BytesIO()
    output_image.save(buf, format="PNG")
    buf.seek(0)

    st.download_button("📥 Baixar imagem sem fundo", buf, file_name="sem_fundo.png", mime="image/png")

except Exception as e:
    st.error(f"Erro ao processar imagem: {e}")

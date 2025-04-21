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

st.title("🔍 Remoção de Fundo de Imagem")

# Pega parâmetros da URL (como ?img_url=https://...)
params = st.experimental_get_query_params()
img_url = params.get("img_url", [None])[0]

if img_url:
    st.write(f"📡 URL recebida: {img_url}")

    try:
        res = requests.get(img_url)
        res.raise_for_status()

        image = Image.open(BytesIO(res.content)).convert("RGBA")
        st.image(image, caption="📸 Imagem Original")

        output = remove(image)
        st.image(output, caption="✅ Imagem sem fundo")

    except Exception as e:
        st.error(f"❌ Erro ao processar imagem: {e}")
else:
    st.info("ℹ️ Passe a URL da imagem na barra de endereços: `?img_url=https://...`")
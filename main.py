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

st.title("Remover Fundo de Imagem")

# Recebe a URL da imagem via query string
img_url = st.experimental_get_query_params().get("img_url", [None])[0]

if img_url:
    try:
        # Baixa a imagem da URL fornecida
        response = requests.get(img_url)
        if response.status_code != 200:
            raise Exception(f"Erro ao baixar imagem: {response.status_code}")

        # Converte a imagem para formato adequado
        img = Image.open(BytesIO(response.content)).convert("RGBA")
        st.image(img, caption="Imagem Original", use_column_width=True)

        # Remove o fundo
        img_sem_fundo = remove(img)
        st.image(img_sem_fundo, caption="Imagem sem fundo", use_column_width=True)
        st.success("✅ Imagem processada com sucesso!")

    except Exception as e:
        st.error(f"Erro ao processar imagem: {e}")
else:
    st.info("ℹ️ Por favor, forneça uma URL de imagem válida.")



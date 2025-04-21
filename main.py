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

st.set_page_config(page_title="Remover Fundo via URL")

st.title("🖼️ Removedor de Fundo (por URL)")

# Logs visuais
st.subheader("🧪 Logs do processo")

# Pega a URL da imagem via query param
params = st.experimental_get_query_params()
img_url = params.get("img", [None])[0]

if img_url:
    st.write(f"🔗 URL recebida: {img_url}")
    print(f"[LOG] URL recebida: {img_url}")

    try:
        st.write("📥 Baixando imagem da internet...")
        print("[LOG] Baixando imagem da URL...")

        response = requests.get(img_url)
        if response.status_code != 200:
            raise Exception(f"Erro ao baixar imagem. Código: {response.status_code}")

        st.write("📷 Convertendo imagem...")
        img = Image.open(BytesIO(response.content)).convert("RGBA")
        st.image(img, caption="Imagem original")
        print("[LOG] Imagem carregada com sucesso.")

        st.write("🧼 Removendo fundo...")
        img_sem_fundo = remove(img)
        print("[LOG] Fundo removido com sucesso.")

        st.image(img_sem_fundo, caption="Imagem sem fundo")
        st.success("✅ Imagem processada com sucesso!")

    except Exception as e:
        st.error(f"Erro ao processar imagem: {e}")
        print(f"[ERRO] {e}")

else:
    st.info("ℹ️ Adicione uma imagem via URL no parâmetro ?img=...")
    st.code("Exemplo: https://seu-app.streamlit.app/?img=https://exemplo.com/imagem.jpg")
    print("[LOG] Nenhuma URL recebida.")


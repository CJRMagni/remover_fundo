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

# Inicia o app e adiciona log no console
print("[INFO] Iniciando o app Streamlit...")

st.set_page_config(page_title="Remover Fundo", layout="centered")
st.title("🖼️ Removedor de Fundo de Imagens via URL")

# Captura da URL da imagem via query string
query_params = st.experimental_get_query_params()
img_url = query_params.get("img_url", [None])[0]

if not img_url:
    print("[INFO] URL não fornecida! Solicitação para o usuário.")
    st.warning("🔗 Adicione `?img_url=URL_DA_IMAGEM` na barra de endereço.")
    st.stop()

print(f"[INFO] URL recebida: {img_url}")
st.write("URL recebida:")
st.code(img_url)

try:
    print("[INFO] Baixando imagem...")
    st.write("📥 Baixando imagem...")

    response = requests.get(img_url)
    response.raise_for_status()

    content_type = response.headers.get("Content-Type", "")
    print(f"[INFO] Content-Type da resposta: {content_type}")
    st.write(f"🔍 Content-Type: {content_type}")

    if "image" not in content_type:
        raise ValueError("A URL não retornou uma imagem válida.")

    print("[INFO] Abrindo a imagem...")
    image = Image.open(BytesIO(response.content)).convert("RGBA")
    st.image(image, caption="Imagem original", use_column_width=True)

    print("[INFO] Removendo fundo...")
    st.write("✂️ Removendo fundo...")

    output_image = remove(image)

    print("[INFO] Fundo removido com sucesso.")
    st.image(output_image, caption="Imagem com fundo removido", use_column_width=True)

    buf = BytesIO()
    output_image.save(buf, format="PNG")
    buf.seek(0)

    print("[INFO] Preparando botão de download...")
    st.download_button("📥 Baixar imagem sem fundo", buf, file_name="sem_fundo.png", mime="image/png")

except Exception as e:
    print(f"[ERROR] Erro ao processar imagem: {e}")
    st.error(f"❌ Erro ao processar imagem: {e}")
    st.exception(e)


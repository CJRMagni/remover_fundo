#from rembg import remove
#from PIL import Image

#caminho_entrada = 'image2.jpg'
#caminho_saida = 'image1_ok.png'

#entrada = Image.open(caminho_entrada)
#saida = remove(entrada)

#saida.save(caminho_saida) 

from flask import Flask, request, send_file, jsonify
from rembg import remove
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    img_url = request.args.get('img_url')
    if not img_url:
        return '''
            <h2>Envie uma imagem com fundo para remover</h2>
            Exemplo: ?img_url=https://site.com/imagem.jpg
        '''

    try:
        print(f"[INFO] Baixando imagem de: {img_url}")
        r = requests.get(img_url)
        r.raise_for_status()

        input_image = Image.open(BytesIO(r.content)).convert("RGBA")

        print(f"[INFO] Removendo fundo...")
        output_image = remove(input_image)

        print(f"[INFO] Fundo removido com sucesso")

        buf = BytesIO()
        output_image.save(buf, format="PNG")
        buf.seek(0)

        return send_file(buf, mimetype='image/png')
    
    except Exception as e:
        print(f"[ERRO] {str(e)}")
        return f"❌ Erro: {str(e)}"

from rembg import remove
from PIL import Image

caminho_entrada = 'image2.jpg'
caminho_saida = 'image1_ok.png'

entrada = Image.open(caminho_entrada)
saida = remove(entrada)

saida.save(caminho_saida)

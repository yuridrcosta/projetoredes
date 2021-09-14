from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

FONT_FILE = 'font/DancingScript.ttf'

def getTemporaryId(person,text):
    return f'F{len(person)}T{len(text)}'

def writeMessageInImage(person,text,text_color):
    """Gera uma imagem com a frase desejada e a foto do filósofo desejado."""

    img = Image.open(f'images/{person}.png')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_FILE, 16)

    if text_color=='BRANCO':
        color = (255,255,255)
    elif text_color == 'PRETO':
        color = (255,255,255)
    elif text_color == 'VERMELHO':
        color = (255,0,0)
    elif text_color == 'AZUL':
        color = (0,0,255)
    elif text_color == 'VERDE':
        color = (0,255,0)

    draw.text((20, 40),text,color,font=font) 

    img.save(f"serverside_IMG_{getTemporaryId(person,text)}.png")
    print('Imagem gerada!')
   
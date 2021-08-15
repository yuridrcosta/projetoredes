import cv2

def getTemporaryId(person,text):
    return f'F{str(len(person))}T{str(len(text))}{text.strip(' ')[0]}'

def writeMessageInImage(person,text):
    """Gera uma imagem com a frase desejada e a foto do filósofo desejado."""

    img = cv2.imread(f'images/{person}.png')

    cv2.putText(img,text,(20,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7,(255,255,255),1)

    cv2.imwrite(f"serverside_IMG_{getTemporaryId(person,text)}.png",img)
    print('Imagem gerada!')
   
def parseProtocol(response):
    """
    COMANDO
    PARAMETRO1:VALUE
    TEXTO
    TEXTO
    TEXTO
    (LINHA VAZIA)
    """
    valid_commands={'IMAGE'}
    valid_person = {'BILL GATES',"CHURCHILL","TIRINGA",'KANT'}
    
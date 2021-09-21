import re

def parseProtocol(response):
    """
    COMANDO
    PESSOA:VALUE
    COR DO TEXTO:VALUE
    TEXTO
    TEXTO
    TEXTO
    (LINHA VAZIA)
    """

    status = '200 OK'
    valid_commands={'IMAGEM'}
    valid_person = {'BILL GATES',"CHURCHILL","TIRINGA",'KANT'}
    valid_color={"BRANCO","VERMELHO","PRETO","AZUL","VERDE"}
    
    splitted_response = response.split("\n")

    client_command = splitted_response[0]
    person = splitted_response[1].split(':')[1]
    color = splitted_response[2].split(':')[1]

    if client_command not in valid_commands:
        message = None
        person = None
        color = None
        status = '400 Comando inválido'
        return person, message, status,color
    
    if person not in valid_person:
        message = None
        person = None
        color = None
        status = '401 Pessoa não disponível'
        return person, message, status,color

    if color not in valid_color:
        message = None
        person = None
        color = None
        status = '402 Cor não disponível'
        return person, message, status,color
    
    message = ''
    for i in range(3,len(splitted_response)):
        message = message + splitted_response[i] + '\n'
    
    person = person.split(' ')[0].lower()

    return person, message, status,color
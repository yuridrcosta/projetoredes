import re

def parseProtocol(response):
    """
    COMANDO
    PESSOA:VALUE
    TEXTO
    TEXTO
    TEXTO
    (LINHA VAZIA)
    """

    status = '200 OK'
    valid_commands={'IMAGEM'}
    valid_person = {'BILL GATES',"CHURCHILL","TIRINGA",'KANT'}
    
    splitted_response = response.split("\n")

    client_command = splitted_response[0]

    if client_command not in valid_commands:
        message = None
        person = None
        status = '400 Comando inválido'
        return person, message, status
    
    person = splitted_response[1].split(':')[1]
    
    if person not in valid_person:
        message = None
        person = None
        status = '401 Pessoa não disponível'
        return person, message, status
    
    message = ''
    for i in range(2,len(splitted_response)):
        message = message + splitted_response[i] + '\n'
    
    person = person.split(' ')[0].lower()

    return person, message, status
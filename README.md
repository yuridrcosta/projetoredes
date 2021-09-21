# Projeto para disciplina Redes de Computadores 
## Curso de Engenharia de Computação da Universidade Federal de Alagoas (UFAL)
### Grupo
**Alunos:** João Paulo Agostinho da Silva (jpas@ic.ufal.br) - Yuri Dimitri Ramos Costa (ydrc@ic.ufal.br) <br/>
<br/>

### Principais funcionalidades da aplicação

Para a nossa aplicação, utilizamos um protocolo de comunicação contendo um único comando (IMAGEM) e 2 parâmetros (PESSOA e COR DO TEXTO). Utilizamos da arquitetura cliente-servidor com o protocolo de transmissão TCP. O objetivo final da aplicação é gerar no servidor e receber no cliente imagens cômicas contendo frases desejadas. A imagem é composta por uma foto de uma personalidade famosa ao lado de uma mensagem.  <br/>

![image](https://user-images.githubusercontent.com/38661715/134221764-ecf5bb7f-fea9-4a73-b1a4-34d67d6c7b98.png)

![capa](https://user-images.githubusercontent.com/38661715/134221920-2ead72d7-c114-43ee-acd2-9cfe223dfea2.png)

 O protocolo segue a seguinte estrutura:
 ````
  IMAGEM
  PESSOA:ESCOLHA1
  COR DO TEXTO:COR1
  TEXTO1
  TEXTO2
  ...
  TEXTO N
  (Linha vazia)
 ````
 
 ## Requisitos e Instalação
 
 **Requerimentos:** Para a utilização é necessário a linguagem de programação **Python 3** com o gerenciador de pacotes **pip**. O download de ambos pode ser feito por meio da página https://www.python.org/. Caso o método de download do código seja utilizando o sistema de versionamento Git, será necesário tê-lo instalado. A seguinte página contém instruções para a instalação do git: https://git-scm.com/downloads  
 
 ### Download do código em ZIP
 
 É possível obter o código clicando em **code** na parte superior da página no github em seguida clicando em **Download ZIP**. Feito o download, extraia esse arquivo na pasta desejada no computador.
 
### Download do código via clonagem do repositório

Por meio do terminal, acesse a pasta onde deseja colocar o projeto e digite o seguinte comando:

````
git clone https://github.com/yuridrcosta/projetoredes.git
````

### Obtenção dos pacotes necessários

Acesse o diretório contendo o projeto. Para o linux, é possível acessar por meio do seguinte comando:
````
cd projetoredes
````
Em seguida instale os pacotes necessários por meio do seguinte comando:
````
pip install -r requirements.txt
````
ou
````
pip install Pillow
````

### Iniciando o servidor

Para iniciar o servidor utilize o seguinte comando:
````
python3 server.py
````
![image](https://user-images.githubusercontent.com/38661715/134238879-9ad35917-20c9-4381-8ab0-d87ebdab99cc.png)

### Iniciando um cliente

````
python3 client.py
````
Em seguida a seguinte mensagem será apresentada:

![image](https://user-images.githubusercontent.com/38661715/134238966-44e2bb78-5104-41ea-88c6-a37ffc435e38.png)

## Informações adicionais

- Durante a conexão com o servidor, o cliente pode inserir o protocolo ou se desconectar. Para desconectar deve-se digitar “!SAIR”.
- O protocolo é formado pelos seguintes campos: comando, pessoa, cor do texto e linha vazia. Cada campo é seguido de uma quebra de linha.
-- Como a única funcionalidade de nossa aplicação é gerar imagem. O campo comando só aceita a entrada imagem. E, respeitando o seguinte formato:
````
IMAGEM
````
- Em pessoa são possíveis as seguintes opções:
````
PESSOA:BILL GATES
PESSOA:CHURCHILL
PESSOA:TIRINGA
PESSOA:KANT
````
- Em cor do texto são possíveis as seguintes opções:
````
COR DO TEXTO:BRANCO
COR DO TEXTO:VERMELHO
COR DO TEXTO:PRETO
COR DO TEXTO:AZUL
COR DO TEXTO:VERDE
````
- O campo da mensagem pode utilizar várias linhas. Porém, a linha vazia é entendida como o fim da mensagem.
- Se algum dos campos for preenchido incorretamente, o erro específico será exibido.
- Se todos os campos forem preenchidos corretamente, será necessário nomear a imagem (somente pelo lado do cliente, no lado do servidor um nome automático é gerado para a imagem). 




 

#Manipulando texto
#copilot: disable

#Manipulando Texto

#CADEIA DE TEXTO (STRING)
#frase = 'CURSO EM VIDEO PYTHON'
#FATIAMENTO DE STRING
#len serve para mostrar as caracteras da string
########################## ANALISE #############################################################
#len(frase) resultado: 21
#frase.count('o') com count voce pede para contar quantas vezes o "o" aparece 
#frse.find('deo') assim ele vai achar a letras q precisamos e ele mostara o numero q essa frase esteja
#'CURSO' in frase assim ele vai analizar a frase dita

########################## TRANSFORMAÇAO ############################################################

#frase.relace('python', 'Android') trocar ele vai achar a palavra 'python' e vai trocar por 'android'
#frase.upper() vai dexar a frase em maiusculo
#frase.capitalize() joga todos para minusculo menos a Primeira letra
#frase.title() ele analiza quantas palavras tem e coloca em minusculo
#frase.strip() ele vai remover os espaços no começo da frase e no final os espaços inuteis e posso complementar com frase.rstrip o r é de right ent ele so vai tirar os espaços da direita, lemrando que o l é de left 

########################## DIVISAO ############################################################

#frase.split() ele vai dividir a frase em palavras e vai criar uma lista com as palavras separadas 
#'-'.join(frase) ele vai juntar as palavras e colocar o que eu quiser entre elas

########################## PRATICA ###########################################################
    #C U R S O   E M    V I  D  E  O      P  Y  T  H  O  N
    #1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21

frase = 'Sua Impressora Térmica Parou de Funcionar'
print(frase.upper())

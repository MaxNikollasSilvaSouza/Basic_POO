def Respostas(texto):  
    resposta = ''  
    while resposta != 's' and resposta != 'n':
        resposta =input(f'{texto} ? s/n\n').lower()
    
    return resposta

def valor_tranferencia(valor):
    liberar = False
    resposta = 0
    while liberar == False:
        try:
            resposta = float(input('Quanto deseja transferir ? '))
            liberar = True

        except:
            print()
        
    
    return resposta
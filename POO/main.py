import Resposta
from classes import Extensoes as ex
from classes import conta_bancaria as cb

print('Olá! Seja muito bem vindo!\n')

resposta =Resposta.Respostas('Você tem cadastro')
  
if resposta == 'n':
    ex.cadastrar()

resposta = Resposta.Respostas('Você deseja realizar uma transferência')

if resposta == 's':
    obj = cb(input('Por favor, informe seu CPF: '))
    trasnferir = Resposta.valor_tranferencia('')
    
    if obj._banco.lower() == 'itau':
        taxa = obj.bradesco(trasnferir)
        obj.itau(trasnferir)
        destino = input('Informe o cpf de quem irá receber: ')
        obj.salvar(trasnferir,destino,taxa)
        obj.printar_valores()
        print("Tranferência realizada, obrigado por utilizar nossos serviços.")
    elif obj._banco.lower() == 'bradesco':
        taxa = obj.bradesco(trasnferir)
        destino = input('Informe o cpf de quem irá receber: ')
        obj.salvar(trasnferir,destino,taxa)
        obj.printar_valores()
        print("Tranferência realizada, obrigado por utilizar nossos serviços.")
    else:
        print('Opção não válida, transferência cancelada!')

else:
    print('Foi um prazer atende-lo!')
    exit()



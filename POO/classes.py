import json
import pandas as pd
import ast


class conta_bancaria:
    
   #OKAY
    def __init__(self,cpf):
        
        self._cpf = cpf
        
        ja_cadastrado = False
        f = open("banco.txt","r")
        try:
            jsonString = f.readline()
            self.jsonObject =json.loads(jsonString)
            #print(type(self.jsonObject))
            for cppf in self.jsonObject:
                teste = self.jsonObject[cppf]['CPF']
                if str(self._cpf) ==  teste:
                    ja_cadastrado = True
                    self._titular = self.jsonObject[cppf]['NOME']
                    self._saldo = self.jsonObject[cppf]['SALDO']
                    self._banco = self.jsonObject[cppf]['BANCO']
            
            if ja_cadastrado == False:
                print("Você ainda não está cadastrado, Se cadastre e depois realize a transferência.")
                exit()

        except:
            print()

        #print(self.jsonObject)     
   
    #OKAY
    def printar_valores(self):
        print(f'{self._titular}, seu saldo atual é de {self._saldo}')
   
    #OKAY
    def itau(self,valor):
        try:
            taxa = valor*0.01
            total = valor+taxa
            if float(self._saldo) >= float(total):
               saldo = float(self._saldo)-float(total)
               self._saldo = str(saldo)
               return taxa
            else:
                print('Saldo insuficiente!')
                #NOOOOOOOOOOO
                #conta_bancaria.printar_valores()
        except:
            print()
            
    #OKAY
    def bradesco(self,valor):
        try:
            taxa = (valor*0.05)+5
            total = float(valor+taxa)
            if float(self._saldo) >= float(total):
                saldo = float(self._saldo)-float(total)
                self._saldo = str(saldo)
                return taxa
            else:
                print('Saldo insuficiente!')

             
        except:
            print()
    
    #OKAY
    def salvar(self,transferencia, destino,taxa):
        
        try:
            for cppf in self.jsonObject:
                teste = self.jsonObject[cppf]['CPF']
                if str(destino) ==  teste:
                    self.jsonObject[cppf]['SALDO']= float(self.jsonObject[cppf]['SALDO']) + float(transferencia)
                   # print(self.jsonObject[cppf])
                if str(self._cpf) == teste:
                    subtrair = taxa + transferencia
                    self.jsonObject[cppf]['SALDO']=float(self.jsonObject[cppf]['SALDO']) - float(subtrair)
                   # print(self.jsonObject[cppf])
                    self._titular = self.jsonObject[cppf]['NOME']
                    self._saldo = self.jsonObject[cppf]['SALDO']
        
        
        
            jsonFile =  open('banco.txt','w+')
            json.dump(self.jsonObject,jsonFile)
            jsonFile.close()
        except:
            print('Não foi possível realizar a tranferência.')


#OKAY
class Extensoes:
    def cadastrar():
        lcpf = input("\nInsira seu CPF: ")
        lnome = input("\nInsira seu nome: ")
        lbanco =input("\nQual é o seu banco? ")
        lsaldo = input("\nRealize seu primeiro depósito. ")
        jsonObject={}
        
        f = open("banco.txt","r")
        #print (f.readline())

        try:
            jsonString = f.readline()
            jsonObject =json.loads(jsonString)
            #print(type(jsonObject))
        except:
            print()
    
        ja_cadastrado = False
      
        #print(jsonObject)
        try:
            for cppf in jsonObject:
                teste = jsonObject[cppf]['CPF']
                if str(lcpf) ==  teste:
                    ja_cadastrado = True
        except:
            print()
                        
        #SALVANDO PESSOAS OK!
        if ja_cadastrado == False:
           
            jsonObject[str(len(jsonObject))]={'CPF':f'{lcpf}', 'NOME':f'{lnome}', 'SALDO':float(lsaldo), 'BANCO':lbanco}
            print(jsonObject[str(len(jsonObject)-1)])
            #print (jsonObject)
            jsonFile =  open('banco.txt','w+')
            json.dump(jsonObject,jsonFile)
            jsonFile.close()
            print('CPF cadastrado!')

        else:
            print('CPF já existe no sistema!')

     

# vamos mudar o diretório para o host
# iremos configurar pedindo para o usuário colocar o input dos sites
#iremos configurar a DNS de forma que o arquivo possa mapear
import os
os.chdir('/etc')

def config(valor):
    while True:
        user=input('insira os sites (q para sair):')
        
        if user == 'q':
            break
        else:
            valor.append(user)
        with open('hosts','r') as arquivo:
            sites= arquivo.read()
    
        for valores in valor:
            pass
       
        with open('hosts','w') as novo_arq:
            novo_arq.write(f'{sites}\n')    
            novo_arq.write(f'{ip()} \t')    
            novo_arq.write(valores)

def ip(endereco='0.0.0.0'):
        return endereco
config(list())
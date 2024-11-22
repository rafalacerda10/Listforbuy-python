from modelos.Compras import Compra
from modelos.Compras import Compras
import os


#______________________________________ Funções dentro _____________________________________________________________

# Adicionar Compra
def adicionar_Compra():
    os.system('cls')
    print('Adicionar uma compra:')
    nome_produto = input('Nome do produto: ')
    categoria = input('Categoria ')
    preco = float(input('Preço unitário: '))
    
    compra = Compra(nome_produto, categoria, preco)
    Compras.append(compra)
    
    print('Compra adicionada com sucesso.')
    input('Pressione ENTER para voltar ao menu...')
    os.system('cls')

# Remover Compra
def remover_Compra():
    os.system('cls')
    if len(Compras) == 0:
        print('Nenhuma compra registrada.')
        input('Pressione ENTER para voltar ao menu...')
        return
    
    print('Compras registradas: \n')
    for i, compra in enumerate(Compras):
        print(f'{i+1}. {compra}')
    
    print('\n')
    print('Qual compra deseja remover?')
    numero_compra = int(input('Número da compra: '))
    
    if numero_compra <= 0 or numero_compra > len(Compras):
        print('Compra inválida.')
        input('Pressione ENTER para voltar ao menu...')
        return
    
    del Compras[numero_compra - 1]
    print('Compra removida com sucesso.')
    input('Pressione ENTER para voltar ao menu...')
    os.system('cls')

#Listar Compras
def listar_compras():
        os.system('cls')
        if len(Compras) == 0:
            print('Nenhuma compra registrada.')
            input('Pressione ENTER para voltar ao menu...')
            return
        
        print('Compras registradas: \n')
        for compra in Compras:
            print(compra)
        input('\n Pressione ENTER para voltar ao menu...')

def finalizandoApp():
    #Função encerrando app
    os.system('cls')
    print('\n')
    print('Saindo da lista de compras...')
    print('\n')
    os.system('pause')
    os.system('cls')
    exit()




    #Função para adicionar compra
    print('\n')
    print('Adicionar uma compra:')
    nome = input('Nome: ')
    preco = input('Preço: ')
    try:
        Compra.objects.create(nome=nome, preco=preco)
        print('Compra adicionada com sucesso.')
    except:
        print('Não foi possível adicionar a compra.')
    print('\n')
    os.system('pause')
    os.system('cls')




# ___________________________________________________________ Sistema _____________________________________________

def escolhaOpcao ():
    #Função para escolher opção do menu
    while True:
        print('Escolha uma opção:')
        print('1. Adicionar uma compra')
        print('2. Remover uma compra')
        print('3. Listar compras')
        print('4. Sair')
        escolha = input('Digite a opção: ')

        if escolha == '4':
            ## Saindo app 
            finalizandoApp()
        elif escolha == '3':
            ## Listando compras
            listar_compras()
        elif escolha == '2':
            remover_Compra()
            ## Removendo compra
            # todo: Implementar função para remover uma compra
        elif escolha == '1':
            adicionar_Compra()
            ## Adicionando compra
            # todo: Implementar função para adicionar uma compra
        else:
            print('Opção inválida. Tente novamente.')















if __name__ == "__main__":
    ## Criar um loop para ficar rodando o app
    print('\n')
    print('Bem Vindo a lista de compras')
    print('\n')
    escolhaOpcao()


    
  
    




# Lista de compras
compras = []
mouse = Compra('mouse','informatica',80)
keyboard = Compra('teclado','informatica',100)



# Adicionando compras à lista
compras.append(mouse)
compras.append(keyboard)

for compra in compras:
    print(f'Nome: {compra.nome}, Categoria: {compra.categoria}, Preço: {compra.valor} \n')

    

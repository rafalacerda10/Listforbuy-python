import os


Tarefas = []

#___________Funções App_______________________________________________________________________
#Função para sair do while e limpar os ultimos comandos - opção 4
def finalzarApp():
    print('Saindo do app...')
    os.system('cls')
    exit()

#Função para adicionar uma tarefa - opção 1
def adicionarTarefa():
    os.system('cls')
    print('Adicionar uma tarefa:')
    tarefa = input('Digite a tarefa: ')
    Tarefas.append(tarefa)
    print('Tarefa adicionada com sucesso!')
    input('Pressione ENTER para voltar ao menu...')
    os.system('cls')

# Função remover tarefa - opção 2
def removendoTarefa():
    os.system('cls')
    print('Remover uma tarefa:')
    index = int(input('Digite o índice da tarefa a remover: '))
    if index < len(Tarefas):
        tarefa_removida = Tarefas.pop(index)
        print(f'Tarefa removida: {tarefa_removida}')
    else:
        print('Índice inválido.')
    input('Pressione ENTER para voltar ao menu...')
    os.system('cls')

def listarTarefas():
    os.system('cls')
    print('Listar tarefas:')
    if len(Tarefas) == 0:
        print('Nenhuma tarefa adicionada.')
    else:
        for index, tarefa in enumerate(Tarefas):
            print(f'{index+1}. {tarefa}')
    input('Pressione ENTER para voltar ao menu...')
    os.system('cls')

#Função para listar tarefas - opção 3



## Inicio Sistema _________________________________________________________________________







def __main__():
    os.system('cls')
    print('Bem Vindo ao  todolist-app')

if __name__ == "__main__":
    ## Criar um loop para ficar rodando o app
    print('Bem Vindo ao  todolist-app')
    print('\n')
    
    ## Loop para escolher as opções do app
    while True:
        print('Escolha uma opção:')
        print('1. Adicionar uma tarefa')
        print('2. Remover uma tarefa')
        print('3. Listar tarefas')
        print('4. Sair')
        escolha = input('Digite a opção: ')

        if escolha == '4':
            ## Saindo app 
            finalzarApp()

        elif escolha == '3':
            ## Listando tarefas
            listarTarefas()
            
        elif escolha == '2':
            ## Removendo tarefa
            removendoTarefa()
        
        elif escolha == '1':
            ## Adicionando tarefa
            adicionarTarefa()



    
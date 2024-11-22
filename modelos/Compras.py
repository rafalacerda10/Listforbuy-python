###
    # Nome
    # Categora
    # Valor
Compras =[]

class Compra():
    def __init__(self, nome, categoria, valor):
        self.nome = nome
        self.categoria = categoria
        self.valor = valor
    
    def __str__(self):
        return f'Nome: {self.nome}, Categoria: {self.categoria}, Valor: {self.valor}'
    
    def adicionar_compra(self, nome, categoria, valor):
        self.nome = nome
        self.categoria = categoria
        self.valor = valor
        Compras.append(self)
        print('Compra adicionada com sucesso!')
        input('Pressione ENTER para voltar ao menu...')
    
    def remover_compra(self, nome):
        for compra in Compras:
            if compra.nome == nome:
                Compras.remove(compra)
                print('Compra removida com sucesso!')
                input('Pressione ENTER para voltar ao menu...')
                return
        
        print('Compra não encontrada.')
        input('Pressione ENTER para voltar ao menu...')
    
    


    
    


###
    # Nome
    # Categora
    # Valor
Compras = []

class Compra():
    def __init__(self, nome, categoria, valor):
        self.nome = nome
        self.categoria = categoria
        self.valor = valor
    
    def __str__(self):
        return f'Nome: {self.nome}, Categoria: {self.categoria}, Valor: {self.valor}'
    
    


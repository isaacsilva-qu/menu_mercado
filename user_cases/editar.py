from repositorio import banco
from user_cases.adicionar import adicionarProduto
from user_cases.buscar import buscarPorCodigo

def editarProduto(codigo, nome, categoria, preco):
    produto = buscarPorCodigo(codigo)
    if produto:
        produto['nome'] = nome
        produto['categoria'] = categoria
        produto['preco'] = preco
        print('Dados alterados com sucesso!')
    else:
        print('Produto não encontrado!')

from repositorio import banco
from user_cases.adicionar import adicionarProduto
from user_cases.buscar import buscarPorCodigo

def deletarProduto(codigo: int):
    produto = buscarPorCodigo(codigo)
    if produto:
        banco.remove(produto)
        print('Produto removido com sucesso!')
    else:
        print('Produto não encontrado!')

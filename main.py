from user_cases.adicionar import adicionarProduto
from user_cases.adicionar import adicionarProduto
from user_cases.buscar import buscarPorCodigo
from user_cases.editar import editarProduto
from user_cases.listar import listarProdutos
from user_cases.deletar import deletarProduto

def menu():
    while True:
        print('---- BEM VINDO AO MENU ----')
        print('1 - Adicionar produto')
        print('2 - Editar produto')
        print('3 - Buscar produto')
        print('4 - Deletar produto')
        print('5 - Listar todos os produto')
        print('Outros - Sair')

        opcao = int(input('Selecione uma opção: '))
        if opcao == '1':
            nome = input('Digite o nome do produto: ')
            categoria = input('Digite a categoria do produto: ')
            preco = float(input('Digite o preço do produto: '))
            adicionarProduto(nome, categoria, preco)

        elif opcao == '2':
            codigo = int(input('Digite o código do produto'))
            nome = input('Digite o nome do produto: ')
            categoria = input('Digite a categoria do produto: ')
            preco = float(input('Digite o preço do produto: '))
            editarProduto(codigo, nome, categoria, preco)

        elif opcao == '3':
            codigo = int(input('Digite o código do produto'))
            buscarPorCodigo(codigo)

        elif opcao == '4':
            codigo = int(input('Digite o código do produto'))
            deletarProduto(codigo)

        elif opcao == '5':
            listarProdutos()

        else:
            break
menu()

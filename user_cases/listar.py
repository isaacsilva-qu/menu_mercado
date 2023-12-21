from repositorio import banco
from user_cases.adicionar import adicionarProduto

def listarProdutos():
    print("--- Lista de Produtos ---")
    for produto in banco:
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: {produto['preco']}")

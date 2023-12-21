from repositorio import banco
from user_cases.adicionar import adicionarProduto

def buscarPorCodigo(codigo: int) -> dict or None:
    for produto in banco:
        if codigo == produto['codigo']:
            return produto
    return None

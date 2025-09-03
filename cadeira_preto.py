#stuff

#oq é um cabeçalho dentro de um arquivo python, pra q serve, qual a diferença do cabeçalho para a docstring

# o cabeçalho
# Ele serve como um cartão de visitas para o seu código, dando uma visão geral rápida e essencial para quem o ler.
# um comentário que tem infos como, nome de quem criou, data de edição descrição, nome de licensa e etc.
# o cabeçalho fica no geral no topo do codigo e não está necessariamente vinculado a uma função.

# docstring
# a docstring é uma especie de explicação sobre a função na qual ela se encontra, o escopo dela e explicar essa função e é possivel acessar até mesmo
#em tempo de execução com "nomedafuncao.doc"


#######################################################################

# formate o cabeçalho deste arquivo

# implemente as funções abaixo e coloque as docstrings

def maximo(nums):
    """oque faz
    oque recebe
    oque retorna"""
    # TODO: percorra a lista guardando o maior atual
    ...

def e_par(n: int) -> bool:
    """ ... """
    # TODO: retorne se n é par
    ...
def fatorial(n: int) -> int:
    """   ...  """
    # TODO: implemente de forma iterativa (sem recursão)
    ...
import re

def limpa_texto(s: str) -> str:
    """..."""
    # TODO: converta s para minúsculo e remova pontuações como ,.;:!?'"()-_
    ...

def conta_vogais(s: str) -> int:
    """....."""
    # TODO: conte as vogais simples
    ...

def palindromo(s: str) -> bool:
    """..."""
    # TODO: normalizar (minúsculo, remover não alfanumérico) e comparar com o reverso
    ...

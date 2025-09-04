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
    """
    Retorna o maior número de uma lista de números.

    Args:
        nums (list): Lista de números (int ou float).

    Returns:
        int/float: O maior número da lista.
    """
    if not nums:
        return None
    maior = nums[0]
    for num in nums:
        if num > maior:
            maior = num
    return maior
    ...


def e_par(n: int) -> bool:
    """
    Verifica se um número é par.

    Args:
        n (int): Número a ser verificado.

    Returns:
        bool: True se n for par, False caso contrário.
    """
    return n % 2 == 0
    ...


def fatorial(n: int) -> int:
    """
    Calcula o fatorial de um número de forma iterativa.

    Args:
        n (int): Número não-negativo.

    Returns:
        int: Fatorial de n.
    """
    if n < 0:
        raise ValueError("n deve ser não-negativo")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
    ...
import re


def limpa_texto(s: str) -> str:
    """
    Converte o texto para minúsculo e remove pontuações.

    Args:
        s (str): Texto a ser limpo.

    Returns:
        str: Texto normalizado sem pontuações.
    """
    s = s.lower()
    return re.sub(r'[^\w\s]', '', s)
    ...


def conta_vogais(s: str) -> int:
    """
    Conta o número de vogais em uma string.

    Args:
        s (str): Texto de entrada.

    Returns:
        int: Quantidade de vogais (a, e, i, o, u) no texto.
    """
    s = s.lower()
    return sum(1 for char in s if char in "aeiou")

    ...


def palindromo(s: str) -> bool:
    """
    Verifica se uma string é um palíndromo.

    Args:
        s (str): Texto de entrada.

    Returns:
        bool: True se s for um palíndromo, False caso contrário.
    """
    s = re.sub(r'[^a-z0-9]', '', s.lower())
    return s == s[::-1]
    ...

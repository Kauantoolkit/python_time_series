# teste_funcoes.py

# Importa todas as funções do arquivo cadeira_preto.py
from cadeira_preto import maximo, e_par, fatorial, limpa_texto, conta_vogais, palindromo

# Testando maximo
numeros = [10, 5, 8, 23, 1]
print("Maior número:", maximo(numeros))

# Testando e_par
print("É par 4?", e_par(4))
print("É par 7?", e_par(7))

# Testando fatorial
print("Fatorial de 5:", fatorial(5))

# Testando limpa_texto
texto = "Olá, mundo! Python é incrível."
print("Texto limpo:", limpa_texto(texto))

# Testando conta_vogais
print("Número de vogais:", conta_vogais(texto))

# Testando palindromo
palavra = "A man, a plan, a canal: Panama"
print(f"'{palavra}' é palíndromo?", palindromo(palavra))

palavra = "rust é incrivel, mas costumo desengripante"
print(f"'{palavra}' é palíndromo?", palindromo(palavra))


##################################################
## AULA 1 - 10 ago 2026                         ##
##################################################

# comando de teste
print("Hello, World!")

# O símbolo # cria um comentário de uma única linha.
# O Python ignora tudo o que estiver depois do símbolo #.
# Comentários ajudam a explicar o raciocínio do programa.

'''
As três aspas podem registrar um texto em várias linhas.

Quando aparecem logo abaixo da definição de uma função,
classe ou módulo, formam uma docstring, isto é, uma
documentação interna do código.

Embora sejam usadas informalmente como comentários de bloco,
as três aspas criam uma string. Portanto, não são exatamente
o mesmo que comentários iniciados por #.
'''

# ATALHOS ÚTEIS NO VS CODE

# Comentar um bloco: Ctrl + K + C

# Descomentar um bloco: Ctrl + K + U

# Abrir ou fechar o terminal integrado: Ctrl + J; também é possível abrir o terminal pelo menu: Terminal > New Terminal

# Para deixar o Auto Save sempre ativado:
# 1. Abra o menu File, ou Arquivo.
# 2. Clique em Auto Save, ou Salvamento Automático.


# ------------------------------------------------------------
# VARIÁVEIS E TIPOS DE DADOS
# ------------------------------------------------------------

# Uma variável é um nome associado a um valor armazenado na memória do computador durante a execução do programa.

# Estrutura:
# nome_da_variavel = valor

# O sinal = realiza uma atribuição. Isso significa que o valor da direita será armazenado na variável escrita à esquerda.

nome = "Maria"           # str: texto, isto é, uma cadeia de caracteres
idade = 30               # int: número inteiro
preco = 19.99            # float: número com casas decimais
esta_matriculada = True  # bool: valor lógico, True ou False
notas = [8.0, 7.5]       # list: coleção ordenada e modificável
aluno = ("Maria", 30)    # tuple: coleção ordenada e imutável
disciplinas = {"Python", "Lógica"}  # set: conjunto sem elementos repetidos
cadastro = {"nome": "Maria", "idade": 30}  # dict: pares de chave e valor

# A função type() permite consultar o tipo de um dado.
print(type(nome))
print(type(idade))
print(type(preco))


# MÃO NA MASSA: BOLETIM

# Cada nota fica armazenada em uma variável diferente.
nota_1 = 2
nota_2 = 4

# A média é calculada e armazenada em uma terceira variável.
media = (nota_1 + nota_2) / 2

print("===== RESULTADO =====")

print(f"Primeira nota: {nota_1:.1f}")
print(f"Segunda nota: {nota_2:.1f}")
print(f"Média: {media:.1f}")
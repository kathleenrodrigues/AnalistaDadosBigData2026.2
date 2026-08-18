#Desafio 1: Ordenação de Três Números

# Entrada dos 3 números inteiros
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

# Identificando o menor número
if n1 <= n2 and n1 <= n3:
  menor = n1
  if n2 <= n3:
    meio = n2
    maior = n3
  else:
    meio = n3
    maior = n2

# Identificando se n2 é o menor
elif n2 <= n1 and n2 <= n3:
  menor = n2
  if n1 <= n3:
    meio = n1
    maior = n3
  else:
    meio = n3
    maior = n1

# Caso n3 seja o menor
else:
  menor = n3
  if n1 <= n2:
    meio = n1
    maior = n2
  else:
    meio = n2
    maior = n1

# Exibindo os números em ordem crescente
print(f"Ordem crescente: {menor}, {meio}, {maior}")



#------------------------------------------------------------------


#Desafio 2: Cálculo de Média e Status do Estudante

numero01 = float(input("Digite a primeira nota: "))
numero02 = float(input("Digite a segunda nota: "))
numero03 = float(input("Digite a terceira nota: "))
numero04 = float(input("Digite a quarta nota: "))

soma = numero01 + numero02 + numero03 + numero04

media = soma/4

print ("Sua média final é:", media)

if media >= 7:
    print ("aprovado!")

elif 5 <= media <= 7:
    print("Recuperação")

else: 
    print("Reprovado")

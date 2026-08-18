#calculadora

# numero1 = 6
# numero2 = 3

# soma = (numero1 + numero2)
# subtracao = (numero1 - numero2)
# divisao = (numero1 / numero2)
# multiplacacao = (numero1 * numero2)
# modulo = (numero1 % numero2)

# print("resultado da Soma é",soma,".")
# print("resultado da subtracao é",subtracao,".")
# print("resultado da divisao é",soma,".")
# print("resultado da multiplicacao é",soma,".")
# print("resultado da Soma é",soma,".")



# continuação 14/08/2026

# x = 15
# y = 20

# print ("x é maior que y?", x > y)
# print ("x é igual a y?", x == y)

## lógica e condicionais ##

#1

# cnh = True
# bebidinha = False 
#             #true    #true       
# posso_dirigir = cnh and not bebidinha 
# print(posso_dirigir)

#2

# busaum = True
# trenzin = True

# venho_pra_aula = busaum or trenzin
# print(venho_pra_aula)

#3

locomocao = "celtinha"
choveu = True

if choveu and locomocao== 'moto':
    resultado = "Tô todo molhado :("
elif not choveu and locomocao== 'moto':
    resultado = "Tô seco :)"

else:
    resultado = "Tô seco :)"

print(resultado)
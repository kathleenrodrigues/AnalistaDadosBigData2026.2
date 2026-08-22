# nome = input("Informe seu nome:")

# if nome=="Pyetro":
#     resultado="Pyetro presente!"
# elif nome== "Phellipe":
#     resultado="Phellipe presente!"


# #-----------------------------------------------------
# #visão if
#mes = int(input("Informe o mês de nascimento em N°:"))

# if mes==1:
#     signo="Aquário"
# elif mes==2:
#     signo="Peixes"
# elif mes==3:
#     signo="Áries"
# elif mes==4:
#     signo="Touro"
# elif mes==5:
#     signo="Gêmeos"
# elif mes==6:
#     signo="Câncer"
# elif mes==7:
#     signo="Leão"
# elif mes==8:
#     signo="Virgem"
# elif mes==9:
#     signo="Libra"
# elif mes==10:
#     signo="Escorpião"
# elif mes==11:
#     signo="Sagitário"
# else:
#     signo="Capricónio"

# print(f"Seu signo é {signo}.")



#---------------------------------------------------
#visão match case

# match mes:
#     case 1:
#         signo="Áquario"
#     case 2:
#         signo="Áries"
#     case 3:
#         signo="Touro"
#     case 4:
#         signo="Gêmeos"
#     case 5:
#         signo="Câncer"
#     case _:
#         signo="Número de mês inválido"

# print(f"{signo}.")

#--------------------------------------------------------------

#Atividades

POTENCIA = 3
largura = int(input("Informe a Largura em m²:"))
comprimento = int(input("Informe o Comprimento em m²:"))

multiplicacao = largura * comprimento  #largura x comprimento
total = (multiplicacao / POTENCIA)
print("multiplicação é",multiplicacao,".")
print("base para lâmpada",total,".")

if total == 3:
    lampadas= 1
elif total >= 6:
    lampadas= 2
elif total >= 9:
    lampadas= 3
elif total >= 12:
    lampadas= 4
elif total >= 15:
    lampadas= 5
elif total >= 18:
    lampadas= 6
else :
    lampadas= "Valor quebrado"

print(f"A quantidade de lâmpadas necessárias para esté comodo é {lampadas}.")




#ATIVIDADE 04

codigo = int(input("Informe o código do produto:"))

codigo = int(input("Informe o número do produto:"))

match codigo:

    case 1:
        codigo= "Sul"
    case 2:
        codigo= "Norte"
    case 3:
        codigo= "Leste"
    case 4:
        codigo= "Oeste"
    case 5:
        codigo= "Nordeste"
    case 6:
        codigo= "Nordeste"
    case 7:
        codigo= "Sudeste"
    case 8:
        codigo= "Sudeste"
    case 9:
        codigo= "Sudeste"
    case 10:
        codigo= "Centro-Oeste"
    case 11:
        codigo= "Noroeste"
    case _:
        codigo="Produto Importado"

print(f"{região}.")




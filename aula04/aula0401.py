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

# POTENCIA = 3
# largura = int(input("Informe a Largura em m²:"))
# comprimento = int(input("Informe o Comprimento em m²:"))

# multiplicacao = largura * comprimento  #largura x comprimento
# total = (multiplicacao / POTENCIA)
# print("multiplicação é",multiplicacao,".")
# print("base para lâmpada",total,".")

# if total == 3:
#     lampadas= 1
# elif total >= 6:
#     lampadas= 2
# elif total >= 9:
#     lampadas= 3
# elif total >= 12:
#     lampadas= 4
# elif total >= 15:
#     lampadas= 5
# elif total >= 18:
#     lampadas= 6
# else :
#     lampadas= "Valor quebrado"

# print(f"A quantidade de lâmpadas necessárias para esté comodo é {lampadas}.")




# #ATIVIDADE 04

# codigo = int(input("Informe o código do produto:"))

# codigo = int(input("Informe o número do produto:"))

# match codigo:

#     case 1:
#         codigo= "Sul"
#     case 2:
#         codigo= "Norte"
#     case 3:
#         codigo= "Leste"
#     case 4:
#         codigo= "Oeste"
#     case 5:
#         codigo= "Nordeste"
#     case 6:
#         codigo= "Nordeste"
#     case 7:
#         codigo= "Sudeste"
#     case 8:
#         codigo= "Sudeste"
#     case 9:
#         codigo= "Sudeste"
#     case 10:
#         codigo= "Centro-Oeste"
#     case 11:
#         codigo= "Noroeste"
#     case _:
#         codigo="Produto Importado"

# print(f"{região}.")



#01
import math

try:
    potencia_lampada = float(input("Digite a potência da lâmpada (W): "))
    largura = float(input("Digite a largura do cômodo (m): "))
    comprimento = float(input("Digite o comprimento do cômodo (m): "))

    if potencia_lampada <= 0 or largura <= 0 or comprimento <= 0:
        print("Valores informados devem ser maiores que zero.")
    else:
        area = largura * comprimento
        potencia_total_necessaria = area * 3  # 3W por m²
        
        
        lampadas_por_potencia = math.ceil(potencia_total_necessaria / potencia_lampada)
        
        
        bocais_necessarios = math.ceil(area / 3)
        
        
        lampadas_finais = min(lampadas_por_potencia, bocais_necessarios)

        print(f"\nÁrea do cômodo: {area:.2f} m²")
        print(f"Bocais disponíveis: {bocais_necessarios}")
        print(f"Número de lâmpadas necessárias: {lampadas_finais}")

except ValueError:
    print("Entrada inválida. Digite apenas números.")

#02 

import math

try:
    comprimento = float(input("Digite o comprimento da cozinha (m): "))
    largura = float(input("Digite a largura da cozinha (m): "))
    altura = float(input("Digite a altura da cozinha (m): "))

    if comprimento <= 0 or largura <= 0 or altura <= 0:
        print("Todas as dimensões devem ser maiores que zero.")
    else:
        
        area_paredes = 2 * (comprimento * altura) + 2 * (largura * altura)
        caixas_necessarias = math.ceil(area_paredes / 1.5)

        print(f"\nÁrea total das paredes: {area_paredes:.2f} m²")
        print(f"Quantidade de caixas de azulejos necessárias: {caixas_necessarias}")

except ValueError:
    print("Entrada inválida. Digite apenas números.")


#03 
PRECO_COMBUSTIVEL = 6.15

try:
    km_inicio = float(input("Marcação do odômetro no início do dia (km): "))
    km_fim = float(input("Marcação do odômetro no final do dia (km): "))
    litros_gastos = float(input("Litros de combustível gastos: "))
    valor_recebido = float(input("Valor total recebido dos passageiros (R$): "))

    if km_fim < km_inicio:
        print("A marcação final deve ser maior ou igual à marcação inicial.")
    elif litros_gastos <= 0:
        print("O consumo de combustível deve ser maior que zero para calcular a média.")
    else:
        distancia_total = km_fim - km_inicio
        media_consumo = distancia_total / litros_gastos
        custo_combustivel = litros_gastos * PRECO_COMBUSTIVEL
        lucro_liquido = valor_recebido - custo_combustivel

        print(f"\nDistância percorrida: {distancia_total:.2f} km")
        print(f"Média de consumo: {media_consumo:.2f} km/L")
        print(f"Custo com combustível: R$ {custo_combustivel:.2f}")
        print(f"Lucro líquido do dia: R$ {lucro_liquido:.2f}")

except ValueError:
    print("Entrada inválida. Digite apenas números.")

#04
try:
    codigo = int(input("Digite o código de origem do produto: "))

    match codigo:
        case 1:
            regiao = "Sul"
        case 2:
            regiao = "Norte"
        case 3:
            regiao = "Leste"
        case 4:
            regiao = "Oeste"
        case 5 | 6:
            regiao = "Nordeste"
        case 7 | 8 | 9:
            regiao = "Sudeste"
        case 10:
            regiao = "Centro-Oeste"
        case 11:
            regiao = "Noroeste"
        case _:
            regiao = "Código inválido ou Região Desconhecida"

    print(f"Região de procedência: {regiao}")

except ValueError:
    print("Entrada inválida. Digite um número inteiro correspondente ao código.")



#05

try:
    nota1 = float(input("Digite a nota da 1ª avaliação: "))
    nota2 = float(input("Digite a nota da 2ª avaliação: "))
    optativa = float(input("Digite a nota da avaliação optativa (-1 se não fez): "))

    
    if optativa != -1:
        if nota1 < nota2 and optativa > nota1:
            nota1 = optativa
        elif nota2 <= nota1 and optativa > nota2:
            nota2 = optativa

    media = (nota1 + nota2) / 2

    print(f"\nMédia final: {media:.2f}")

    
    if media >= 6.0:
        print("Situação: Aprovado")
    elif media >= 3.0:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")

except ValueError:
    print("Entrada inválida. Digite apenas valores numéricos para as notas.")


#06 

try:
    valor = float(input("Digite um valor: "))

    
    if valor >= 0:
        print("O valor é Positivo")
    else:
        print("O valor é Negativo")

except ValueError:
    print("Entrada inválida. Digite apenas valores numéricos.")






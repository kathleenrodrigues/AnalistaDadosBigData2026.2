##ESTRUTURAS DE REPETIÇÃO

#FOR:

# meunome = "Kathleen"

# for i in meunome:
#     print(i)


# for i in range (10):
#     print(i)

# for i in range (1,10):
#     print(i)

# for i in range (1,10,2):
#     print(i)

# for i in range (10):
#      print(i)

# for i in range (-102,-1,2):
#      print(i)

#--------------------------------------------------
#WHILE

acertou = 0
while acertou < 5:
    print(f"Número {acertou + 1} de 5:") 
    num = float(input("Digite um número: ")) 
        
    dobro = num * 2 
    triplo = num * 3 
    quádruplo = num * 4 
        
    print(f"  Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
    acertou+=1
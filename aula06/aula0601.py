#Sem usar Lista []
# impar_01 = 3
# impar_02 = 5
# impar_03 = 13
# impar_04 = 27


# #Direita para Esquerda
# impares = []
# print(type(impares))
# impares = [3,5,13,27]
# print(impares[0])


# #Esquerda para direita
# impares = []
# print(type(impares))
# impares = [3,5,13,27]
# print(impares[-1])

# lista_01 = [
#     12,
#     "Pedro",
#     12.53343,
#     "[{_{^^{}}}",
#     False,
#     0,
#     [2,4,6,8]
# ]

# print(lista_01[1],lista_01[2],lista_01[4],lista_01[6][2])

# #CONDICIONAIS

# lista_02 = ["Márcia"]

# if "Márcia" in lista_02:
#     print(lista_02)

# else:
#     print("Márcia não está presente na lista")

#LOOPINGS:

# participantes = ["Isaque","Luana","Fernando","Bianca","Ana Paula"]

# # for participantes in participantes:
# #     print(participantes)

# partic_2 = "Hugo"
# participantes.append(partic_2)
# participantes.insert(2,partic_2)
# participantes.pop(1)
# participantes.remove("Hugo")
# participantes.reverse()
# participantes.count("Hugo")

# participantes.clear()
# print(participantes)


#TUPLAS
# participantes = ("Isaque","Luana","Fernando","Bianca","Ana Paula")
# print(participantes)
# print(participantes,type(participantes))
# participantes_02 = ("Fernando","111.11.******","Avenida Dr. Tibúrcio, 444", "DDD2199999999")
# print(participantes_02.index("Avenida Dr. Tibúrcio, 444"))
# listinha_partic_02=list(participantes_02)
# print(listinha_partic_02)


#SETS

# numeros_pares = {
#     202,
#     203,
#     204,
#     204,
#     205,
#     219,
#     291,
#     292,
#     202
# }

# #print(numeros_pares,type(numeros_pares))
# numeros_impares = {111,111,112,291,291,205}
# print(numeros_pares.intersection(numeros_impares))
# numeros_pares.remove(205)
# print(numeros_pares)

#DICIONÁRIO:

produtos = {"maçã":5.99,"laranja":4.79}
#print(produtos,(type(produtos)))
print(produtos.items())
print(produtos.keys())
print(produtos.values())
print(produtos.get("laranja"))
produtos2 = produtos.copy()
print(produtos2)
#produtos2.pop("maçã")
produtos2["maçã"]=7.99
print(produtos2)
###
achadinhos = {}
print(type(achadinhos))
achadinhos["capinha celular"]=12.99
print(achadinhos)
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

#-----------------------------------------------------------

#01

TOTAL_ALUNOS = 10

for i in range(1, TOTAL_ALUNOS + 1):
    print(f"\n--- Aluno {i} de {TOTAL_ALUNOS} ---")
    try:
        nota1 = float(input("Digite a nota da 1ª avaliação: "))
        nota2 = float(input("Digite a nota da 2ª avaliação: "))
        optativa = float(input("Digite a nota da optativa (-1 se não fez): "))

        
        if optativa != -1:
            if nota1 < nota2 and optativa > nota1:
                nota1 = optativa
            elif nota2 <= nota1 and optativa > nota2:
                nota2 = optativa

        media = (nota1 + nota2) / 2
        print(f"Média final: {media:.2f}")

        if media >= 6.0:
            print("Situação: Aprovado")
        elif media >= 3.0:
            print("Situação: Recuperação")
        else:
            print("Situação: Reprovado")

    except ValueError:
        print("Entrada inválida. Digite valores numéricos para as notas.")


#02

ANO_ATUAL = 2026
TOTAL_CANDIDATOS = 12

for i in range(1, TOTAL_CANDIDATOS + 1):
    print(f"\n--- Candidato {i} de {TOTAL_CANDIDATOS} ---")
    try:
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        idade = ANO_ATUAL - ano_nascimento

        if idade < 18:
            print("Candidato menor de 18 anos. Não pode participar do processo.")
            continue  

        
        nome = input("Digite o nome completo: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o e-mail: ")

        print(f"Candidato {nome} cadastrado com sucesso!")

    except ValueError:
        print("Entrada inválida. Digite um ano válido.")


#03

USUARIO_CORRETO = "admin"
SENHA_CORRETA = "123456"
TENTATIVAS_MAXIMAS = 3

login_sucesso = False

for tentativa in range(1, TENTATIVAS_MAXIMAS + 1):
    usuario_input = input("Digite o nome de usuário: ")
    senha_input = input("Digite a senha: ")

    if usuario_input == USUARIO_CORRETO and senha_input == SENHA_CORRETA:
        print("\nLogin efetuado com sucesso! Bem-vindo ao sistema.")
        login_sucesso = True
        break  
    else:
        tentativas_restantes = TENTATIVAS_MAXIMAS - tentativa
        if tentativas_restantes > 0:
            print(f"Usuário ou senha incorretos. Você ainda tem {tentativas_restantes} tentativa(s).\n")

if not login_sucesso:
    print("\nNúmero máximo de tentativas excedido. Acesso bloqueado!")


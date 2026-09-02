def listar_garcons(cadastrar_garcom):
    """
    Lista todos os garçons cadastrados no sistema.
    
    Parâmetro:
        garcons: lista contendo os dados dos garçons.
    """

    try:
        if len(cadastrar_garcom) == 0:
            print("\nNenhum garçom cadastrado.")
            return

        print("\n===== LISTA DE GARÇONS =====")

        for i in range(len(cadastrar_garcom)):
            nome = cadastrar_garcom[i][0]
            matricula = cadastrar_garcom[i][1]
            situacao = cadastrar_garcom[i][2]

            print(f"\nGarçom {i + 1}:")
            print("Nome:", nome)
            print("Matrícula:", matricula)
            print("Situação:", situacao)

    except (TypeError, IndexError):
        print("Erro ao listar os garçons.")

        
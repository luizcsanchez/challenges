def adicionar_contato(contatos):
    print("\nAdicionar contato")
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    contato = {"contato_nome": nome, "contato_telefone": telefone, "contato_email": email, "contato_favorito": False}
    contatos.append(contato)
    print("Contato adicionado com sucesso!")
    return

def ver_contatos(contatos):
    print("\nLista de Contatos:")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "❤" if contato["contato_favorito"] else " "
        nome_contato = contato["contato_nome"]
        telefone_contato = contato["contato_telefone"]
        email_contato = contato["contato_email"]
        print(f"{indice}. {nome_contato} - {telefone_contato} - {email_contato} {favorito}")
    return

def editar_contato(contatos, indice_contato, escolha_edicao):
    print(f"{len(contatos)+1}. Voltar")
    indice_contato_ajustado = indice_contato - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        if escolha_edicao == "1":
            novo_nome = input("Digite o novo nome do contato: ")
            contatos[indice_contato_ajustado]["contato_nome"] = novo_nome
            print(f"Nome do contato atualizado para: {novo_nome}")
        elif escolha_edicao == "2":
            novo_telefone = input("Digite o novo telefone do contato: ")
            contatos[indice_contato_ajustado]["contato_telefone"] = novo_telefone
            print(f"Telefone do contato atualizado para: {novo_telefone}")
        elif escolha_edicao == "3":
            novo_email = input("Digite o novo email do contato: ")
            contatos[indice_contato_ajustado]["contato_email"] = novo_email
            print(f"Email do contato atualizado para: {novo_email}")
        elif escolha_edicao == {len(contatos)+1}:
            return
    else:
        print("Contato não encontrado")
    return

def marcar_desmarcar_favorito(contatos, indice_contato):
    indice_contato_ajustado = indice_contato - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        if contatos[indice_contato_ajustado]["contato_favorito"]:
            contatos[indice_contato_ajustado]["contato_favorito"] = False
            print("Contato desmarcado como favorito")
        else:
            contatos[indice_contato_ajustado]["contato_favorito"] = True
            print("Contato marcado como favorito")
    else:
        print("Contato não encontrado")
    return

def ver_contatos_favoritos(contatos):
    print("\nLista de Contatos Favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        if contato["contato_favorito"]:
            nome_contato = contato["contato_nome"]
            telefone_contato = contato["contato_telefone"]
            email_contato = contato["contato_email"]
            print(f"{indice}. {nome_contato} - {telefone_contato} - {email_contato}")
    return

def apagar_contato(contatos, indice_contato):
    indice_contato_ajustado = indice_contato - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos.pop(indice_contato_ajustado)
        print("Contato apagado com sucesso")
    else:
        print("Contato não encontrado")
    return

contatos=[]
while True:
    print("\nMenu do Gereciador de Contatos")
    print("1 - Adicionar contato")
    print("2 - Ver contatos")
    print("3 - Editar contato")
    print("4 - Marcar/Desmarcar contato favorito")
    print("5 - Ver contatos favoritos")
    print("6 - Apagar contato")
    print("7 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        adicionar_contato(contatos)
    elif escolha == "2":
        ver_contatos(contatos)
    elif escolha == "3":
        while True:
            ver_contatos(contatos)
            indice_contato = int(input("Digite o número do contato que deseja editar: "))

            print("\nMenu de edição de contato:")
            print("1 - Editar nome")
            print("2 - Editar telefone")
            print("3 - Editar email")
            print("4 - Voltar")

            escolha_edicao = input("Escolha uma opção: ")
            editar_contato(contatos, indice_contato, escolha_edicao)
            if escolha_edicao == "4":
                break
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = int(input("Digite o número do contato que deseja marcar/desmarcar como favorito: "))
        marcar_desmarcar_favorito(contatos, indice_contato)
    elif escolha == "5":
        ver_contatos_favoritos(contatos)
    elif escolha == "6":
        ver_contatos(contatos)
        indice_contato = int(input("Digite o número do contato que deseja apagar: "))
        apagar_contato(contatos, indice_contato)
    elif escolha == "7":
        break
import aluguel, imovel, inquilino, proprietario

lista = []

def menu():
  while True:
    print("Selecione uma opção:")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Deletar")
    print("5 - Sair")
    opcao = int(input(""))
    if opcao in [1,2,3,4,5]:
        if opcao == 1: #Menu Cadastrar
            menuCadastrar()
        elif opcao == 2: #Listar
            for i in lista:
                print(i)
                print("\n")
        elif opcao == 3: #Atualizar
            menuAtualizar()
        elif opcao == 4: #Deletar
            identi = input("Digite o ID: ")
            for i in lista:
                if i.id == identi:
                    lista.remove(i)
                    print("Cadastro deletado")
                else:
                    print("ID não encontrado")
        elif opcao == 5: #Sair
            print("Saindo do sistema.")
            break
    else:
      print("Opção Inválida!")

def menuCadastrar():
    while True: 
        print("Selecione uma opção:")
        print("1 - Cadastrar Imóveis")
        print("2 - Cadastrar Inquilino")
        print("3 - Cadastrar Aluguel")
        print("4 - Cadastrar Proprietário")
        print("5 - Voltar")
        opcao = int(input(""))
        if opcao in [1,2,3,4,5]:
            if opcao == 1: #Cadastrar Imóveis
                imoveis = imovel.imovel()
                imoveis.id = input("Digite o ID: ")
                imoveis.lougradouro = input("Digite o lougradouro: ")
                imoveis.cep = input("Digite o cep: ")
                imoveis.bairro = input("Digite o bairro: ")
                imoveis.cidade = input("Digite a cidade: ")
                lista.append(imoveis)
                print("\nCadastro Concluido\n")
            elif opcao == 2: #Cadastrar Inquilino
                inquilinos = inquilino.inquilino()
                inquilinos.id = input("Digite o ID: ")
                inquilinos.nome = input("Digite o nome: ")
                inquilinos.datanasc = input("Digite a data de nascimento: ")
                lista.append(inquilinos)
                print("\nCadastro Concluido\n")
            elif opcao == 3: #Cadastrar Aluguel
                alugueis = aluguel.aluguel()
                alugueis.id = input("Digite o ID: ")
                alugueis.num_contrato = input("Digite o número do contrato: ")
                alugueis.idImovel = input("Digite o ID do imóvei associado ao aluguel: ")
                alugueis.idProp = input("Digite o ID do proprietário associado ao aluguel: ")
                lista.append(alugueis)
                print("\nCadastro Concluido\n")
            elif opcao == 4: #Cadastrar Proprietário
                proprietarios = proprietario.proprietario()
                proprietarios.id = input("Digite o ID: ")
                proprietarios.nome = input("Digite o nome: ")
                proprietarios.datanasc = input("Digite a data de nascimento: ")
                lista.append(proprietarios)
                print("\nCadastro Concluido\n")
            elif opcao == 5: #Voltar
                menu()
                break 
        else:
            print("Opção Inválida!")

def menuAtualizar():
    while True: 
        print("Selecione uma opção:")
        print("1 - Atualizar Imóveis")
        print("2 - Atualizar Inquilino")
        print("3 - Atualizar Aluguel")
        print("4 - Atualizar Proprietário")
        print("5 - Voltar")
        opcao = int(input(""))
        if opcao in [1,2,3,4,5]:
            if opcao == 1: #Atualizar Imóveis
                identi = input("Digite o ID: ")
                for i in lista:
                    if i.id == identi:
                        i.id = input("Digite o ID: ")
                        i.lougradouro = input("Digite o lougradouro: ")
                        i.cep = input("Digite o cep: ")
                        i.bairro = input("Digite o bairro: ")
                        i.cidade = input("Digite a cidade: ")
                        print("Cadastro atualizado")
                else:
                    print("ID não encontrado")
            elif opcao == 2: #Atualizar Inquilino
                identi = input("Digite o ID: ")
                for i in lista:
                    if i.id == identi:
                        i.id = input("Digite o ID: ")
                        i.nome = input("Digite o nome: ")
                        i.datanasc = input("Digite a data de nascimento: ")
                        print("Cadastro atualizado")
                else:
                    print("ID não encontrado")
            elif opcao == 3: #Atualizar Aluguel
                identi = input("Digite o ID: ")
                for i in lista:
                    if i.id == identi:
                        i.id = input("Digite o ID: ")
                        i.num_contrato = input("Digite o número do contrato: ")
                        i.idImovel = input("Digite o ID do imóvei associado ao aluguel: ")
                        i.idProp = input("Digite o ID do proprietário associado ao aluguel: ")
                else:
                    print("ID não encontrado")
            elif opcao == 4: #Atualizar Proprietario
                identi = input("Digite o ID: ")
                for i in lista:
                    if i.id == identi:
                        i.id = input("Digite o ID: ")
                        i.nome = input("Digite o nome: ")
                        i.datanasc = input("Digite a data de nascimento: ")
                        print("Cadastro atualizado")
                else:
                    print("ID não encontrado")
            elif opcao == 5: #Voltar
                menu()
                break  
        else:
            print("Opção Inválida!")

menu()
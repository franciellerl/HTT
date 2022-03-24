
# Fazer um cadastro de 3 campos com funções

def cadastrar(lista):
     nome = ""
     data_nasc = ""
     endereco = ""
     while nome == "":
         nome = input("Coloque o nome: ")
     while data_nasc == "":
         data_nasc = input("Coloque a data de nascimento: ")
     while endereco == "":
         endereco = input("Coloque o endereço: ")

     registro = {"Nome":nome, "Data_Nascimento":data_nasc, "Endereco": endereco}
     lista.append(registro)
     print("Sucesso! Cadastrado!")

def listar(lista):
     for item in lista:
        print(item)

def menu():
     print("Selecione uma opção:")
     print("1 - Cadastrar")
     print("2 - Listar")
     print("3 - Sair")
     opcao = int(input(""))
     return opcao

def main():
    #usuario e print também poderiam estar no menu()
    #Mas preferi manter igual o original, fora do loop
    usuario = input("Entre com o seu nome: ")
    print(f"Seja Bem-vindo {usuario} !\n")
    lista = []
    while True:
        opcao = menu()
        if opcao in [1,2,3]:
            if opcao == 1: #Cadastrar
                cadastrar(lista)
            elif opcao == 2: #Listar
                listar(lista)
            elif opcao == 3: #Sair
                print("Saindo do sistema...")
                break
        else:
            print("Opção Inválida!")

main()



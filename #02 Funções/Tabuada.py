# Fazer um programa que imprima a tabuada com funções

def multiplicar():
     print("Iniciando a multiplicação")

     for i in range(11):
        for j in range(11):
            print(f"{i} x {j} = {i*j}")
        print("\n")
     print("Sucesso!")

def menu():
     print("Selecione uma opção:")
     print("1 - Multiplicar")
     print("2 - Sair")
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
        if opcao in [1,2]:
            if opcao == 1: #Multiplicar
                multiplicar()
            elif opcao == 2: #Sair
                print("Saindo do sistema...")
                break
        else:
            print("Opção Inválida!")

main()

from funcoes import *

while True:
    Exibir_menu()
    
    try:
        escolha = int(input("Escolha uma das opções: "))
        
        if escolha == 0:
            print("Saindo do programa!")
            break
        elif escolha == 1:
            name =input("Qual tarefa deseja adicionar: ")
            add_task(name)
        elif escolha == 2:
            print("Finalizando uma tarefa")
            task_done()
        elif escolha == 3:
            view_list()
        elif escolha == 4:
            print("Removendo um tarefa")
        else: 
            print("Opção invalida, por favor, escolha novamente.")
        
    except ValueError:
        print("Digite um numero valido.")
Lista = []
Concluidas = []

def Exibir_menu():
    print("1. Adicionar uma Tarefa")
    print("2. Finalizar Tarefa")   
    print("3. Visualizar Tarefas")
    print("0. Sair do programa")    

def add_task(new_task):
    Lista.append(new_task)
    print("\nNova tarefa adicionada na lista.\n")
    
def view_list():
    print(f"\nTarefas listadas: {Lista}\n\nTarefas concluidas:{Concluidas}\n")
    
def task_done():
    while True:
        print("="*18)
        for indice, value in enumerate(Lista):
            print(f'{indice}. {value}')
        
        escolha = int(input("Qual tarefa você deseja marca como finalizada: "))
        
        if escolha == indice:
            tarefa_finalizada = Lista.pop(indice)
            Concluidas.append(tarefa_finalizada)
            print(f'\nA tarefa {value} foi marcada como finalizada.\n')
            break
        else:
            print('\nTarefa não encontrada, Escolha uma mostrada na lista.\n')
        print("="*18)

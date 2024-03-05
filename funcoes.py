Lista = []
Concluidas = []

def Exibir_menu():
    print("1. Adicionar uma Tarefa")
    print("2. Finalizar Tarefa")   
    print("3. Visualizar Tarefas")
    print("4. Remover uma tarefa")
    print("0. Sair do programa")    

def add_task(new_task):
    Lista.append(new_task)
    print("="*18)
    print("\nNova tarefa adicionada na lista.\n")
    print("="*18)
    
def view_list():
    print("="*18)
    print(f"\nTarefas listadas: {Lista}\nTarefas concluidas:{Concluidas}\n")
    print("="*18)
    
def task_done():
    while True:
        for indice, value in enumerate(Lista):
            print(f'{indice+1}. {value}')
        
        escolha = int(input("Qual tarefa você deseja marca como finalizada: "))
        
        if escolha == indice:
            print('='*18)
            print(f'A tarefa {value} foi marcada como finalizada.')
            print('='*18)
            break
        else:
            print("="*18)
            print('Tarefa não encontrada, Escolha uma mostrada na lista.')
            print("="*18)
from GerenciadorDeTarefas import GerenciadorDeTarefas

# Initialize the task manager
gerenciador = GerenciadorDeTarefas()
def exibir_menu():
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Sair")

while True:
    exibir_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        titulo = input("Título da Tarefa: ")
        descricao = input("Descrição da Tarefa: ")
        data_limite = input("Data Limite (DD/MM/AAAA): ")
        gerenciador.adicionar_tarefa(titulo, descricao, data_limite)
        print("Tarefa adicionada com sucesso!")

    elif escolha == '2':
        gerenciador.listar_tarefas()

    elif escolha == '3':
        try:
            tarefa_id = int(input("ID da Tarefa a ser marcada como concluída: "))
            gerenciador.marcar_tarefa_concluida(tarefa_id)
        except ValueError:
            print("Por favor, insira um ID válido.")

    elif escolha == '4':
        print("Saindo do Gerenciador de Tarefas. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
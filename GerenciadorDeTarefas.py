from Tarefa import Tarefa

class GerenciadorDeTarefas:
    def __init__(self):
       self.tarefas = []

    # Always use self. for instance variables inside class methods.    
    def adicionar_tarefa(self, titulo, descricao, data_limite):
        nova_tarefa = Tarefa(titulo, descricao, data_limite)
        self.tarefas.append(nova_tarefa)

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return
        for tarefa in self.tarefas:
            print(tarefa)
            print("-" * 20)

    def marcar_tarefa_concluida(self, tarefa_id):
        for tarefa in self.tarefas:
            if tarefa.id == tarefa_id:
                if tarefa.status == "Finalizada.":
                    print(f"Tarefa ID {tarefa_id} já está concluída.")
                else:
                    tarefa.marcar_concluida()
                    print(f"Tarefa ID {tarefa_id} marcada como concluída.")
                    return
        print(f"Tarefa com ID {tarefa_id} não encontrada.")
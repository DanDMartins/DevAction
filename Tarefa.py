class Tarefa:
    proximo_id = 1
    def __init__(self, titulo, descricao, data_limite):
        # Atributos da tarefa - Geração automática de ID para evitar duplicados
        self.id = Tarefa.proximo_id
        Tarefa.proximo_id += 1
        self.titulo = titulo
        self.descricao = descricao
        self.status = "Pendente."
        self.data_limite = data_limite

    def marcar_concluida(self):
        self.status = "Finalizada."

    def __str__(self):
        return f"ID: {self.id}\nTítulo: {self.titulo}\nDescrição: {self.descricao}\nStatus: {self.status}\nData Limite: {self.data_limite}"
    
    
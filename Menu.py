Class Menu:
    def __init__(self, CadastrarContato, ListarContato, ExcluirContato, CriarTarefa, ListarTarefas, ExcluirTarefas):
        self.__CadastrarContato = CadastrarContato
        self.__ListarContato = ListarContato
        self.__ExcluirContato = ExcluirContato
        self.__CriarTarefa = CriarTarefa
        self.__ListarTarefas = ListarTarefas
        self.__ExcluirTarefas = ExcluirTarefas

    def get_CadastrarContato(self):
        return self.CadastrarContato

    def get__ListarContato(self):
        return self.ListarContato

    def get__ExluirContato(self):
        return self.ExcluirContato

    def get__CriarTarefa(self):
        return self.__CriarTarefa

    def get__ListarTarefas(self):
        return self.ListarTarefas

    def get__ExcluirTarefas(self):
        return self.ExluirTarefas




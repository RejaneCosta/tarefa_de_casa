class CriarTarefas:

    def __init__(self, AdicionarDescricao, EditarTarefa, SelecionarStatus):
        self.__AdicionarDescricao = AdicionarDescricao
        self.__EditarTarefa = EditarTarefa
        self.__SelecionarStatus = SelecionarStatus

    def get_AdicionarDescricao(self):
        return self.__AdicionarDescricao

    def get_EditarTarefa(self):
        return self.__EditarTarefa

    def get_SelecionarStatus(self):
        return self.__SelecionarStatus

    def set_AdicionarDescricao(self, AdicionarDescricao):
        self.__AdicionarDescricao = AdicionarDescricao

    def set_EditarTarefa(self, EditarTarefa):
        self.__EditarTarefa = EditarTarefa

    def set_SelecionarStatus(self,SelecionarStatus):
        self.__SelecionarStatus = SelecionarStatus

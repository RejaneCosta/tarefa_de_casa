class Contato:

    def __init__(self, NomeContato, Apelido, TelefoneContato, EmailContato, GrupoAssociado):
        self.__NomeContato = NomeContato
        self.__Apelido = Apelido
        self.__TelefoneContato = TelefoneContato
        self.__EmailContato = EmailContato
        self.__GrupoAssociado = GrupoAssociado

    def get_NomeContato(self):
        return self.__NomeContato

    def get_Apelido(self):
        return self.__Apelido

    def get_TelefoneContato(self):
        return self.__TelefoneContato

    def get_EmailContato(self):
        return self.__EmailContato

    def get_GrupoAssociado(self):
        return self.__GrupoAssociado
    

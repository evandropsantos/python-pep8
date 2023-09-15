import abc


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ''

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def inseri_cliente(self):
        self.fila.append(self.senha_atual)

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gerar_senha_atual()
        self.inseri_cliente()

    @abc.abstractmethod
    def chama_cliente(self, caixa: int) -> str:
        ...

    @abc.abstractmethod
    def gerar_senha_atual(self) -> None:
        ...

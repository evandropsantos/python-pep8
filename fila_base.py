import abc
from typing import List, Union

from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

Classes = Union[EstatisticaResumida, EstatisticaDetalhada]


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ''

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    def inseri_cliente(self):
        self.fila.append(self.senha_atual)

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gerar_senha_atual()
        self.inseri_cliente()

    def estatistica(self, retorna_estatistica: Classes) -> dict:
        return retorna_estatistica.roda_estatistica(self.clientes_atendidos)

    @abc.abstractmethod
    def chama_cliente(self, caixa: int) -> str:
        ...

    @abc.abstractmethod
    def gerar_senha_atual(self) -> None:
        ...

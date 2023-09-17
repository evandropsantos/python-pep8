from typing import Dict, List, Union

from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO


class FilaPrioritaria(FilaBase):
    def gerar_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (
            f'Cliente atual: {cliente_atual }, dirija-se ao caixa: {caixa}'
        )

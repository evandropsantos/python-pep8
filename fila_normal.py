from fila_base import FilaBase


class filanormal(FilaBase):
    def gerarsenhaatual(self) -> None:
        self.senhaatual = f'NM{self.codigo}'

    def atualizafila(self) -> None:
        self.reseta_fila()
        self.gerarsenhaatual()
        self.fila.append(self.senhaatual)

    def chamacliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, dirija-se ao caixa {caixa}')

class filanormal:
    codigo: int = 0
    fila = []
    clientesatendidos = []
    senhaatual: str = ''

    def gerarsenhaatual(self) -> None:
        self.senhaatual = f'NM{self.codigo}'

    def resetafila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualizafila(self) -> None:
        self.resetafila()
        self.gerarsenhaatual()
        self.fila.append(self.senhaatual)

    def chamacliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, dirija-se ao caixa {caixa}')
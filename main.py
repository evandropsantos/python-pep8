from fila_normal import filanormal
from fila_prioritaria import FilaPrioritaria


# fila_teste = filanormal()

# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()

# print(fila_teste.chamacliente(5))
# print(fila_teste.chamacliente(10))

fila_teste2 = FilaPrioritaria()

fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()

print(fila_teste2.chama_cliente(10))
print(fila_teste2.chama_cliente(1))
print(fila_teste2.estatistica('10/01/1993', 198, 'detail'))



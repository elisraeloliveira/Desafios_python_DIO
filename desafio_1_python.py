def analise_vendas(vendas):
    total_vendas = sum(vendas)
    total_media = total_vendas / len(vendas)
    return f'{int(total_vendas)}, {total_media:.2f}'

# numeros pedidos 120, 150, 170, 130, 200, 250, 180, 220, 210, 160, 140, 190
#                 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 12
#                 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60

def obter_entrada(valores):
    entrada = input(valores)
    vendas = [float(venda) for venda in entrada.split(',')]
    return vendas

vendas = obter_entrada("")
print(analise_vendas(vendas))

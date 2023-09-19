# Sabendo como calcular aluguel de um carro
k_p = float(input('Digite a quantidade de Km que você percorreu ? '))
d_a = int(input('Digite a quantidade de dias o carro foi alugado ? '))
preco_dias = d_a * 60
preco_Km = k_p * 0.15
total = preco_dias + preco_Km
print(f'O total do aluguel completo ficou em R${total:.2f}')

produto = float(input('Digite o preço do produto: R$'))
desonto = 0.05 * produto
valor_descontado = produto - desonto
print(f'O produto custava R${produto:.2f} e com desconto aplicado agora está custando R${valor_descontado:.2f}')
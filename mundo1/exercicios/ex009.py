n1 = int(input('Digite um numero: '))
print('tabuada 1')
# tabuada feita 1 a 1:
tabuada = (f'{n1} x {1} = {1*n1} \n{n1} x {2} = {2*n1} \n{n1} x {3} = {3*n1} \n{n1} x {4} = {4*n1} \n{n1} x {5} = {5*n1} \n{n1} x {6} = {6*n1} \n{n1} x {7} = {7*n1} \n{n1} x {8} = {8*n1} \n{n1} x {9} = {9*n1} \n{n1} x {10:<0} = {10*n1} \n')
print(f'{tabuada}')
# segundo jeito de tabuada:
print(20*'=')
print(f'{n1} x {1} = {n1*1}')
print(f'{n1} x {2} = {n1*2}')
print(f'{n1} x {3} = {n1*3}')
print(f'{n1} x {4} = {n1*4}')
print(f'{n1} x {5} = {n1*5}')
print(f'{n1} x {6} = {n1*6}')
print(f'{n1} x {7} = {n1*7}')
print(f'{n1} x {8} = {n1*8}')
print(f'{n1} x {9} = {n1*9}')
print(f'{n1} x {10} = {n1*10}')
print(20*'=')
# terceiro jeito de tabuda:
for n in range(1, 11):
    print(f'{n1} x {n:2} = {n1*n}')
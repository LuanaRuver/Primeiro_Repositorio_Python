# indentação e blocos

saldo = 100

def sacar(saldo, valor):
    if saldo >= valor:
        saldo =- valor
        print('saque concluído com sucesso')
    else:
        print('valor excede o limite disponível')

sacar(saldo, 10)
print(saldo)

# estruturas condicionais

idade = int(input ('Qual sua idade?'))
print(idade)
if idade>=18:
    print('Maior de idade')
elif idade<18 and idade>0:
    print('Menor de idade')
else:
    print('Idade Inválida')

x = 10
y = 5

resultado = True if x>y else False
print(resultado)

# estrutura de repetição

var = [0, 1, 2, 3]

for j in var:
    print(j, end=" ")


for j in range(0,11):
    print(j, end=" ")

while True:
    lista = list(range(0,15))
    print (lista)
    for i in lista:
        if i == 10:
            break
        elif i % 2 == 0:
            continue
        else:
            print(i)
    break
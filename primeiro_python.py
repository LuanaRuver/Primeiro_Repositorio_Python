print("Hello, World!");
print('1'+'2')
print(1+2)
print(1.2+1.4)

# variaveis e constantes

nome = 'Luana'
idade = 27
print(nome, idade)

nome, idade = 'Victor', 30
print(f'tenho {idade} anos')

CONSTANTE = 'da para alterar, porém maiúscula indica constante, é uma boa pratica'
print(CONSTANTE)
CONSTANTE = 'não altere'
print(CONSTANTE)

snake_case = 'usar _ em espaços em branco, também é boa prática'
print(snake_case)

# convertendo tipos

preco = 10
print(type(preco))
preco = float(preco)
print(preco, type(preco))
preco = str(preco)
print(preco, type(preco))

# divisoes

print(10/2) #float
print(10//2) #int


# input
nome = input('Seu nome:')
idade = input('Sua idade:')
print(nome, idade)
print(nome, idade, end='...\n') # por padrão end é uma quebra de linha (\n)
print(nome, idade, sep='_') # por padrão sep é um espaço em branco

# operadores aritimeticos

print( 3 % 2 ) # módulo - resto da divisão
print( 3 ** 2 ) # exponenciação

# operadores lógicos 

print(10>5 and 10>6) # True
print(10>5 and 10<6) # False
print(10>5 or 10<6) # True
print(not (10>5 and 10<6)) # True

# operadores de identidade

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False
print(a == c)  # True

# operadores de associação

frutas = ["limao", "uva"]
curso = "Curso de python"

print("laranja" not in frutas) # True
print("limao" in frutas) # True
print("Python" in curso) # False // sensitive
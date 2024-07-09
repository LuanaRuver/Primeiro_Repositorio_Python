var = "   PythoN  "

print(var.upper())
print(var.lower())
print(var.title())
print(var.strip())
print(var.lstrip())
print(var.rstrip())
print(var.center(15,"!"))
print("_".join(var))

# old stile %

nome = 'Luana'
idade = 27
altura = 1.6

pessoa = {"nome": nome, "idade": idade, "altura": altura}

print('Olá, me chamo %s, tenho %d anos e %f de altura' % (nome, idade, altura))

#.format()

print('Olá, me chamo {}, tenho {} anos e {} de altura' .format(nome, idade, altura))
print('Olá, me chamo {name}, tenho {years} anos e {altura:.2f} de altura' .format(name = nome, years = idade, altura = altura))
print('Olá, me chamo {nome}, tenho {idade} anos e {altura:.2f} de altura' .format(**pessoa))
print(f'Olá, me chamo {nome}, tenho {idade} anos e {altura:.2f} de altura')

#fatiando 

string = 'Luana Ruver'

print(string[0])
print(string[:10])
print(string[10:])
print(string[5:10])
print(string[5:10:2])
print(string[:])
print(string[::-1])
print(string[-1])

#multiplas linhas ou triplas

mensagem = f'''
oi    ,
    me chamo LUANA    
'''

print(mensagem)

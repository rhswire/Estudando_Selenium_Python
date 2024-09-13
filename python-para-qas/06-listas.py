
# criar lista
lista = [1, 2, 3, 4]
print(lista)

# adicionar item a list
lista.append(5)
print(lista)

# remover o último elemento da lista
lista.pop()
print(lista)

#remover um item da lista
lista.remove(2)
print(lista)

#reverter a ordem dps elementos da lista
lista.reverse()
print(lista)

#adicionar mais itens na lista
lista.extend([2, 5, 0, 3])
print(lista)

#Ordenar os itens da lista
lista.sort()
print(lista)

#Acessar item
print(lista[2])
print(lista[5])

# contar itens
quantidade = lista.count(3)
print(quantidade)

#pegar o tamanho da lista
tamanho = len(lista)
print(tamanho)

# pesquisar na lista
if 4 in lista:
    print("número está na lista")
else:
    print("número não está na lista")






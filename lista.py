lista1 = ['Diemes', 'Nunes', 'Souza' , 'Caio' , 'Luana' ]
print(type(lista1))
print(len(lista1))
print(lista1[4])
lista2 = lista1 *2
print(lista2)
lista1.append('Amanda') #adiciona itens ao fim da lista
print(lista1)
lista1.remove('Caio') #exclui itens pelo nome
print(lista1)
lista1.pop(2) #exclui itens pelo seu indice
print(lista1)
for listageral in lista1:
print(listageral)
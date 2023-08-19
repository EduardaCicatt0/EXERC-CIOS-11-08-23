dados_cliente = {
'nome' : 'Eduarda' ,
'endereço' : 'Rua Rio Grande do Sul , 1270' , 
'Telefone' : '98182963'
}
print(dados_cliente['endereço'])

dados_cliente ['cidade']  = 'Ivaiporã'
print(dados_cliente)

dados_cliente.pop('telefone') #exclui dados do dicionário
print(dados_cliente)

for indice, valor in dados_cliente.item():
    print(f'indice: {indice}, valor: {valor}')

    #pip install numpy faz calculo em matrizes
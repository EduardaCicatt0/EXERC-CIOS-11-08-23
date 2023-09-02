def minha_funcao(*args):
  for arg in args :
    print(arg)
  print(type(args))

minha_funcao (1, 2, 3, 4)
#args é do tipo tupla. Aqui, usa-se um laço de repetição FOR para mostrar na tela a sequência de números 
# até o final


def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
       print(f"A chave é {chave} e o valor é {valor}")
    print(type(kwargs))

minha_funcao(nome="Eduarda", idade=25, pais="Brasil")
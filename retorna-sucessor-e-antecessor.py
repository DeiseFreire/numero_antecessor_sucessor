def antecessor_sucessor(numero):
  """
  Função que recebe um número inteiro como entrada e retorna o seu antecessor e sucessor

  Argumentos:
  numero (int): O número inteiro para o qual se deseja calcular o antecessor e sucessor.

  Retorno:
  tuple: Uma tupla contendo o antecessor e o sucessor do número, nessa ordem.
  """
  if numero == 0:
    antecessor = None
  else:
     antecessor = numero - 1
  sucessor = numero + 1
  return antecessor,sucessor
numero = int(input("Digite um número inteiro: "))
antecessor,sucessor = antecessor_sucessor(numero)
if antecessor is None:
     print(f"O número {numero} não possui antecessor.")
else:
    print(f"O antecessor de {numero} é {antecessor}.")
    print(f"O sucessor de {numero} é {sucessor}.")

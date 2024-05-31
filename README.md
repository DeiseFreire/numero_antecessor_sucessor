### Função `antecessor_sucessor`

<img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/>

### Descrição:

Esta função recebe um número inteiro como entrada e retorna o seu antecessor e sucessor em uma tupla.

### Argumentos:

* `numero` (int): O número inteiro para o qual se deseja calcular o antecessor e sucessor.

### Retorno:

* `tuple`: Uma tupla contendo o antecessor e o sucessor do número, nessa ordem.

### Observações:

* Se o número for 0, o antecessor será `None`.
* A função utiliza `input` para solicitar ao usuário que digite um número inteiro.
* A função imprime o antecessor e o sucessor do número digitado.

### Exemplo de uso:

```python
numero = int(input("Digite um número inteiro: "))
antecessor, sucessor = antecessor_sucessor(numero)

if antecessor is None:
    print(f"O número {numero} não possui antecessor.")
else:
    print(f"O antecessor de {numero} é {antecessor}.")
    print(f"O sucessor de {numero} é {sucessor}.")
```

### Teste:

Execute o código acima e digite um número inteiro. A função imprimirá o antecessor e o sucessor do número digitado.

### Melhorias:

* A função pode ser modificada para aceitar números de ponto flutuante.
* A função pode ser modificada para verificar se o número digitado é um número válido.
* A função pode ser modificada para usar exceções para lidar com erros.

### Processos de desenvolvimento:


[![Replit](https://img.shields.io/badge/Replit-F26207.svg?style=for-the-badge&logo=Replit&logoColor=white)](https://replit.com/@DeiseFreire2022/numeroantecessorsucessor)


[![YouTube](https://img.shields.io/badge/YouTube-FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/playlist?list=PLZpH1iUcDo5hCRy-PXWZR5xkEwbFw1LB3)

### Tags

#python #funcao #numeroAntecessor #numeroSucessor #antecessor #sucessor #educacao #aprendizado #programacaoIniciantes

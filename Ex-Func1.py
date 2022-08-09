#Função de Entrada de dados

def entrada():
    num = int(input("Digite um número: "))
    n1 = dobro(num)
    imprimir(num, n1)

#Função de Calculo do dobro
def dobro(num):
    dobro = num * 2
    return dobro

#Função de Inprimir na tela
def imprimir(num, num2):
    print(f"O número digitado foi: {num}")
    print(f"O dobro do número digitado é de: {num2}")


#Programa Principal
entrada()



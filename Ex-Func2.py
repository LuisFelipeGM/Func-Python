#Função de Entrada de dados

from re import X


def entrada():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    imprimir(maior(x, y))



#Função de Calculo do dobro
def maior(x, y):
    if x > y:
        par = f"O número {x} é maior que {y}"
    elif y > x:
        par = f"O número {y} é maior que {x}"
    elif x == y:
        par = f"Os números {x} e {y} são iguais"
    
    return par
    

#Função de Inprimir na tela
def imprimir(par):
    print(par)


#Programa Principal
entrada()


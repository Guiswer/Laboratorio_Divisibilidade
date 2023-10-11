import math


def divisibilidade2(num):
    verificador = False
    ultimo_digito = int(str(num)[-1])
    if ultimo_digito == 0 or ultimo_digito == 2 or ultimo_digito == 4 or ultimo_digito == 6 or ultimo_digito == 8:
        verificador = True
    return verificador


def testarDivisibilidade(dividendo, divisor):
    return True


def imprimirObjetivoLab():
    print("Programa TESTE DE DIVISIBILIDADE\n"
    + "O  programa  tem  por  objetivo  informar  se  um  determinadonumero ehou nao divisivel por outro.\n"
    + "Os testes de divisibilidade sao validos para os seguintes divisores: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15 e 25.\n\n")
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))
    
    while divisor not in [2, 3, 4, 5, 6 , 7, 8, 10, 11, 12, 15, 25]:
        print("Divisor invalido! Favor informar novos valores.")
        dividendo = int(input("Dividendo: "))
        divisor = int(input("Divisor: "))
    
    if testarDivisibilidade(dividendo, divisor):
        print(str(dividendo) + " eh divisivel por " + str(divisor))
    else:
        print(str(dividendo) + " NAO eh divisivel por " + str(divisor))
    
    resposta_usuario = input("Deseja realizar novo teste (s/n)?").upper()
    while resposta_usuario not in "SsNn":
        resposta_usuario = input("Opcao invalida! Deseja realizar novo teste (s/n)?").upper()
    if resposta_usuario == "S":
        imprimirObjetivoLab()

imprimirObjetivoLab()
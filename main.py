import math


def divisibilidade2(num):
    verificador = False
    ultimo_digito = int(str(num)[-1])
    if ultimo_digito == 0 or ultimo_digito == 2 or ultimo_digito == 4 or ultimo_digito == 6 or ultimo_digito == 8:
        verificador = True
    return verificador


def divisibilidade3(num):

    verificador = False
    a = list(str(num))
    b = 0

    if len(a) > 1: #para números com mais de 1 algorismos
        while len(a) > 1:
            for i in a:
                b += int(i)
            a = str(b)
            b = 0

        if a == "3" or a == "6" or a == "9":
            verificador = True          
            
    else: #para números com 1 algorismos       
        while num > 0:
            num -= 3
        if num == 0:
            verificador = True
       
    return verificador

def divisibilidade11(num):
    verificador = False
    par_impar = int(str(num[0]))
    contador = 0


    par = []
    impar = []

    x = 0 
    y = 0

    while par_impar > 0:
        par_impar -= 2 


    if par_impar == 0:
        x = 0 
        y = 1
        
        while contador < len(num):
            try:
                par.append(int(str(num[x])))
            except IndexError:
                par.append(0)
                
            try:
                impar.append(int(str(num[y])))
            except IndexError:
                impar.append(0)
                
            contador += 1
            x += 2 
            y += 2
    else:
        x = 1
        y = 0
        z = 0
        while contador < len(num):
            try:
                par.append(int(str(num[x])))
            except IndexError:
                par.append(0)
                

            try:
                impar.append(int(str(num[y])))
            except IndexError:
                impar.append(0)
                
            contador += 1 
            x += 2
            y += 2

    print(par)
    print(impar)

    sp = 0
    x = 0

    #Realizando a soma dos pares
    for e in par:
        sp += int(str(par[x]))
        x += 1

    si = 0
    y = 0 

    #Realizando a soma dos impares
    for i in impar:
        si += int(str(impar[y]))
        y += 1 


    if sp >= si:
        resultado = sp - si

        if resultado == 0:
            verificador = True


        else:
            x = 0
            z = str(resultado)
            while len(str(resultado)) > 1:
                resultado = int(z[x]) - int(z[x+1]) 
            
            if resultado == 0:
                verificador = True


    elif si >= sp:
        resultado = si - sp

        if resultado == 0:
            verificador = True

        else:
            x = 0
            z = str(resultado)
            while len(str(resultado)) > 1:
                resultado = int(z[x]) - int(z[x+1]) 
            if resultado == 0:
                verificador = True

    return verificador


def divisibilidade15(num):

    verificador = False
    verificador3 = False
    a = list(str(num))
    b = 0

    if len(a) > 1: #para números com mais de 1 algorismos
        while len(a) > 1:
            for i in a:
                b += int(i)

            a = str(b)
            b = 0

        if a == "3" or a == "6" or a == "9":
            verificador3 = True    
            
    else: #para números com 1 algorismos     
        while num > 0:
            num -= 3
        if num == 0:
            verificador3 = True
        
    verificador5 = False
    ultimo_digito = int(str(num)[-1])
    if ultimo_digito == 5 or ultimo_digito == 0:
        verificador5 = True

    if verificador3 and verificador5:
        verificador = True

    return verificador


def testarDivisibilidade(dividendo, divisor):
    verificador = False
    if divisor == 2:
        verificador = divisibilidade2(dividendo)
    elif divisor == 3:
        verificador = divisibilidade3(dividendo)
    elif divisor == 4:
        verificador = divisibilidade4(dividendo)
    elif divisor == 5:
        verificador = divisibilidade5(dividendo)
    elif divisor == 6:
        verificador = divisibilidade6(dividendo)
    elif divisor == 7:
        verificador = divisibilidade7(dividendo)
    elif divisor == 8:
        verificador = divisibilidade8(dividendo)
    elif divisor == 9:
        verificador = divisibilidade9(dividendo)
    elif divisor == 10:
        verificador = divisibilidade10(dividendo)
    elif divisor == 11:
        verificador = divisibilidade11(dividendo)
    elif divisor == 12:
        verificador = divisibilidade12(dividendo)
    elif divisor == 15:
        verificador = divisibilidade15(dividendo)
    else:
        verificador =divisibilidade25(dividendo)
    return verificador


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
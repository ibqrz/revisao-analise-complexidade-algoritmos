def zero(X):
    return X == 0

def add(X):
    return X + 1

def sub(X):
    return X - 1

def soma_versao_convertida(A, B):
    P = 0
    R = 1

    while R != 0:
        P += 1

        if R == 1:
            if zero(B):
                R = 0
            else:
                R = 2

        elif R == 2:
            A = add(A)
            R = 3

        elif R == 3:
            B = sub(B)
            R = 1

    return A, B, P

print('- - - - - - - - - - - - - - - - - - -')
print('         ~~ RESULTADOS: ~~')
print('A = 2 | B = 3 ->', soma_versao_convertida(2,3))
print('A = 4 | B = 0 ->', soma_versao_convertida(4,0))
print('- - - - - - - - - - - - - - - - - - -')
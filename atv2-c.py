def zero(X):
    return X == 0

def add(X):
    return X + 1

def sub(X):
    return X - 1


def soma_estruturada_direta(A, B):
    P = 0

    while not zero(B):
        P += 1
        while not zero(B):
            P += 1
            A = add(A)
            B = sub(B)

    P += 1
    return A, B, P

print('- - - - - - - - - - - - - - - - - - -')
print('         ~~ RESULTADOS: ~~')
print('A = 2 | B = 3 ->', soma_estruturada_direta(2,3))
print('A = 4 | B = 0 ->', soma_estruturada_direta(4,0))
print('- - - - - - - - - - - - - - - - - - -')
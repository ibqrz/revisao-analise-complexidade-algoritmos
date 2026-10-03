def zero(X):
    return X == 0

def add(X):
    return X + 1

def sub(X):
    return X - 1


def soma(A, B, tracar=False):
    """A <- A + B (monolítico). Rótulo 0 representa F (fim)."""
    P = 0   # passos
    R = 1   # rótulo corrente

    while R != 0:
        P += 1
        executado = R

        if R == 1:
            R = 0 if zero(B) else 2
        elif R == 2:
            A = add(A)
            R = 3
        elif R == 3:
            B = sub(B)
            R = 1

        if tracar:
            print(f"{P:5} | {executado:6} | {A} | {B}")

    return A, B, P


def soma_5b(A, B, tracar=False):
    """A <- A + 5B: cinco add(A) (rótulos 2 a 6) e sub(B) no rótulo 7."""
    P = 0
    R = 1

    while R != 0:
        P += 1
        executado = R

        if R == 1:
            R = 0 if zero(B) else 2
        elif R <= 6:          # rótulos 2, 3, 4, 5 e 6
            A = add(A)
            R += 1
        elif R == 7:
            B = sub(B)
            R = 1

        if tracar:
            print(f"{P:5} | {executado:6} | {A} | {B}")

    return A, B, P


def mostrar(titulo, programa, A, B):
    print(titulo)
    print("passo | rótulo | A | B")
    resultado = programa(A, B, tracar=True)
    print("resultado: A = %d, B = %d; passos = %d\n" % resultado)
    return resultado


if __name__ == "__main__":
    assert mostrar("(a/b) A <- A + B; A = 2, B = 3", soma, 2, 3) == (5, 0, 3 * 3 + 1)
    assert mostrar("(c) A <- A + B; A = 4, B = 0", soma, 4, 0) == (4, 0, 1)
    assert mostrar("(d) A <- A + 5B; A = 2, B = 3", soma_5b, 2, 3) == (17, 0, 7 * 3 + 1)
    assert mostrar("(d) A <- A + 5B; A = 4, B = 0", soma_5b, 4, 0) == (4, 0, 1)
    print("Todas as verificações passaram.")
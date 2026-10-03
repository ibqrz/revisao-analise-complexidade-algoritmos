"""D1-D4: função computada, domínio e classificação (conferência por simulação)."""

LIMITE = 5000

# "se": (operação, registrador, destino se zero, destino se diferente de zero)
# "add"/"sub": (operação, registrador, próximo rótulo)
PROGRAMAS = {
    "D1": {1: ("se", "A", "F", 2), 2: ("sub", "A", 3), 3: ("sub", "A", 1)},
    "D2": {1: ("se", "B", "F", 2), 2: ("add", "A", 3), 3: ("add", "B", 1)},
    "D3": {1: ("se", "B", "F", 2), 2: ("add", "A", 3), 3: ("add", "A", 4),
        4: ("add", "A", 5), 5: ("sub", "B", 1)},
    "D4": {1: ("se", "A", 3, 2), 2: ("sub", "A", 1), 3: ("add", "A", 4),
        4: ("add", "A", "F")},
}


def executar(programa, A, B, limite=LIMITE):
    """Devolve (parou, A_final, passos)."""
    registros = {"A": A, "B": B}
    rotulo, passos = 1, 0

    while rotulo != "F" and passos < limite:
        instrucao = programa[rotulo]
        operacao, registrador, *argumentos = instrucao

        if operacao == "se":
            se_zero, senao = argumentos
            rotulo = se_zero if registros[registrador] == 0 else senao
        else:
            rotulo = argumentos[0]
            variacao = 1 if operacao == "add" else -1
            registros[registrador] = max(0, registros[registrador] + variacao)
        passos += 1

    parou = rotulo == "F"
    return parou, registros["A"] if parou else None, passos


# previsões feitas SÓ pelo raciocínio (parte a): (para?, A_final, passos)
PREVISAO = {
    "D1": lambda A, B: (True, 0, 3 * ((A + 1) // 2) + 1),
    "D2": lambda A, B: (True, A, 1) if B == 0 else (False, None, LIMITE),
    "D3": lambda A, B: (True, A + 3 * B, 5 * B + 1),
    "D4": lambda A, B: (True, 2, 2 * A + 3),
}

if __name__ == "__main__":
    for nome, programa in PROGRAMAS.items():
        print(f"{nome} (linhas: A, colunas: B; célula: A_final/passos, ∞ = não parou)")
        print("      " + "".join(f"B={b:<9}" for b in range(6)))

        for a in range(6):
            celulas = []
            for b in range(6):
                resultado = executar(programa, a, b)
                assert resultado == PREVISAO[nome](a, b), (nome, a, b, resultado)
                parou, valor_a, passos = resultado
                celulas.append(f"{valor_a}/{passos}" if parou else "∞")
            print(f"A={a}   " + "".join(f"{celula:<10}" for celula in celulas))
        print()

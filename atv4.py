BRANCO = '␣'

def maquina_inverte(w):
    fita = list(w) + [BRANCO]
    pos = 0 # cabeçote / posição inicial da fita 
    P = 0
    E = 'q0'

    while E != 'qf':
        P += 1

        if fita[pos] == 'a':
            fita[pos] = 'b'
            pos += 1

        elif fita[pos] == 'b':
            fita[pos] = 'a'
            pos += 1

        else:
            E = 'qf'

    return ''.join(fita[:-1]), P

print('- - - - - - - - - - - - - - - - - - -')
print('         ~~ RESULTADOS: ~~')
for w in ['', 'a', 'b', 'ab', 'abba', 'aabbb', 'bbbb']:
    print(repr(w), '->', maquina_inverte(w))
print('- - - - - - - - - - - - - - - - - - -')
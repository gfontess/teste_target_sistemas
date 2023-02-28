def sequencia_fibonacci(n):
    # Inicia a sequência com os dois primeiros valores (0 e 1)
    sequencia = [0, 1]

    # Calcula os próximos valores da sequência até chegar em n
    while sequencia[-1] < n:
        next_value = sequencia[-1] + sequencia[-2]
        sequencia.append(next_value)

    # Verifica se n pertence à sequência
    if n in sequencia:
        print(f'O numero {n} pertence a sequencia de Fibonacci: {sequencia}')
    else:
        print(f'O numero {n} nao pertence a sequencia de Fibonacci: {sequencia}')

# Exemplo de uso
sequencia_fibonacci(21)
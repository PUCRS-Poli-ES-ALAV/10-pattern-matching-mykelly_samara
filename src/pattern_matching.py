def encontrar_primeira_ocorrencia(s1, s2):
    """
    Retorna o índice da primeira ocorrência de s2 em s1, ou -1 se não existir.
    Também retorna o número de iterações e instruções executadas.
    """
    n = len(s1)
    m = len(s2)
    iteracoes = 0
    instrucoes = 0
    for i in range(n - m + 1):
        iteracoes += 1  # Uma iteração do laço externo
        match = True
        for j in range(m):
            instrucoes += 1  # Uma instrução de comparação
            if s1[i + j] != s2[j]:
                match = False
                break
        if match:
            return i, iteracoes, instrucoes
    return -1, iteracoes, instrucoes


def testar(s1, s2, esperado, descricao):
    idx, it, inst = encontrar_primeira_ocorrencia(s1, s2)
    print(f"--- {descricao} ---")
    print(f"Padrão: '{s2}'\nTexto:  '{s1[:50]}{'...' if len(s1) > 50 else ''}")
    print(f"Índice encontrado: {idx} | Esperado: {esperado}")
    print(f"Iterações: {it} | Instruções: {inst}\n")

if __name__ == "__main__":
    # Testes pequenos
    testar(
        "ABCDCBDCBDACBDABDCBADF",
        "ADF",
        19,
        "Padrão no final (exemplo do enunciado)"
    )

    # Teste com strings grandes
    import random
    import string
    tamanho = 500_000
    s1_grande = ''.join(random.choices(string.ascii_uppercase, k=tamanho))
    s2_grande = s1_grande[-10:]  # Garante que s2 está no final de s1
    testar(
        s1_grande,
        s2_grande,
        tamanho-10,
        "Padrão no final de string grande"
    )

    # Outros testes sugeridos
    testar("ABCDEFGH", "XYZ", -1, "Padrão não existe")
    testar("HELLO WORLD", "HEL", 0, "Padrão no início")
    testar("PYTHON IS FUN", "IS", 7, "Padrão no meio")
    testar("TESTE", "TESTE", 0, "Padrão igual à string inteira")
    testar("ABC", "ABCDE", -1, "Padrão maior que a string")

    print("Complexidade no pior caso: O(n*m), onde n = len(s1) e m = len(s2)") 
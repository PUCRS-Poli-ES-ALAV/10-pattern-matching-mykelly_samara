import sys

def hash_horner(s, M, R, Q, contadores=None):
    h = 0
    for j in range(M):
        h = (h * R + ord(s[j])) % Q
        if contadores is not None:
            contadores['instrucoes'] += 1
    return h


def rabin_karp(pat, txt, R=256, Q=997_399_999):
    """
    Retorna o índice da primeira ocorrência de pat em txt usando Rabin-Karp,
    ou -1 se não existir. Conta iterações e instruções.
    R: tamanho do alfabeto (ASCII=256)
    Q: primo grande para módulo
    """
    M = len(pat)
    N = len(txt)
    contadores = {'iteracoes': 0, 'instrucoes': 0}
    patHash = hash_horner(pat, M, R, Q, contadores)
    for i in range(N - M + 1):
        contadores['iteracoes'] += 1
        txtHash = hash_horner(txt[i:i+M], M, R, Q, contadores)
        if patHash == txtHash:
            # Verificação para evitar colisão
            if txt[i:i+M] == pat:
                return i, contadores['iteracoes'], contadores['instrucoes']
    return -1, contadores['iteracoes'], contadores['instrucoes']


def encontrar_primeira_ocorrencia(s1, s2):
    n = len(s1)
    m = len(s2)
    iteracoes = 0
    instrucoes = 0
    for i in range(n - m + 1):
        iteracoes += 1
        match = True
        for j in range(m):
            instrucoes += 1
            if s1[i + j] != s2[j]:
                match = False
                break
        if match:
            return i, iteracoes, instrucoes
    return -1, iteracoes, instrucoes


def testar_simples(pat, txt, esperado, descricao):
    idx, it, inst = encontrar_primeira_ocorrencia(txt, pat)
    print(f"--- {descricao} (Busca Simples) ---")
    print(f"Padrão: '{pat}'\nTexto:  '{txt[:50]}{'...' if len(txt) > 50 else ''}")
    print(f"Índice encontrado: {idx} | Esperado: {esperado}")
    print(f"Iterações: {it} | Instruções: {inst}\n")

def testar_rabin_karp(pat, txt, esperado, descricao):
    idx, it, inst = rabin_karp(pat, txt)
    print(f"--- {descricao} (Rabin-Karp) ---")
    print(f"Padrão: '{pat}'\nTexto:  '{txt[:50]}{'...' if len(txt) > 50 else ''}")
    print(f"Índice encontrado: {idx} | Esperado: {esperado}")
    print(f"Iterações: {it} | Instruções: {inst}\n")

def testar_kmp(pat, txt, esperado, descricao):
    idx, it, inst = kmp_search(pat, txt)
    print(f"--- {descricao} (KMP) ---")
    print(f"Padrão: '{pat}'\nTexto:  '{txt[:50]}{'...' if len(txt) > 50 else ''}")
    print(f"Índice encontrado: {idx} | Esperado: {esperado}")
    print(f"Iterações: {it} | Instruções: {inst}\n")

def testar_personalizado(descricao, funcao):
    print(f"\n--- Teste personalizado: {descricao} ---")
    txt = input("Digite o texto (s1): ")
    pat = input("Digite o padrão (s2): ")
    if descricao == 'Busca Simples':
        idx, it, inst = funcao(txt, pat)
    else:  # Rabin-Karp
        idx, it, inst = funcao(pat, txt)
    print(f"Padrão: '{pat}'\nTexto:  '{txt[:50]}{'...' if len(txt) > 50 else ''}")
    print(f"Índice encontrado: {idx}")
    print(f"Iterações: {it} | Instruções: {inst}\n")

def testar_personalizado_kmp():
    print(f"\n--- Teste personalizado: KMP ---")
    txt = input("Digite o texto (s1): ")
    pat = input("Digite o padrão (s2): ")
    idx, it, inst = kmp_search(pat, txt)
    print(f"Padrão: '{pat}'\nTexto:  '{txt[:50]}{'...' if len(txt) > 50 else ''}")
    print(f"Índice encontrado: {idx}")
    print(f"Iterações: {it} | Instruções: {inst}\n")

def menu():
    while True:
        print("\nEscolha a atividade para testar:")
        print("1 - Atividade 1: Busca Simples (testes automáticos)")
        print("2 - Atividade 2: Rabin-Karp (testes automáticos)")
        print("3 - Busca Simples (inserir texto e padrão)")
        print("4 - Rabin-Karp (inserir texto e padrão)")
        print("5 - KMP (testes automáticos)")
        print("6 - KMP (inserir texto e padrão)")
        print("0 - Sair")
        opcao = input("Opção: ")
        if opcao == '1':
            print("\nTestando Busca Simples:")
            testar_simples("ADF", "ABCDCBDCBDACBDABDCBADF", 19, "Padrão no final (exemplo do enunciado)")
            import random, string
            tamanho = 500_000
            txt_grande = ''.join(random.choices(string.ascii_uppercase, k=tamanho))
            pat_grande = txt_grande[-10:]
            testar_simples(pat_grande, txt_grande, tamanho-10, "Padrão no final de string grande")
            testar_simples("XYZ", "ABCDEFGH", -1, "Padrão não existe")
            testar_simples("HEL", "HELLO WORLD", 0, "Padrão no início")
            testar_simples("IS", "PYTHON IS FUN", 7, "Padrão no meio")
            testar_simples("TESTE", "TESTE", 0, "Padrão igual à string inteira")
            testar_simples("ABCDE", "ABC", -1, "Padrão maior que a string")
            print("Complexidade no pior caso: O(n*m), onde n = len(txt) e m = len(pat)")
        elif opcao == '2':
            print("\nTestando Rabin-Karp:")
            testar_rabin_karp("ADF", "ABCDCBDCBDACBDABDCBADF", 19, "Padrão no final (exemplo do enunciado)")
            import random, string
            tamanho = 500_000
            txt_grande = ''.join(random.choices(string.ascii_uppercase, k=tamanho))
            pat_grande = txt_grande[-10:]
            testar_rabin_karp(pat_grande, txt_grande, tamanho-10, "Padrão no final de string grande")
            testar_rabin_karp("XYZ", "ABCDEFGH", -1, "Padrão não existe")
            testar_rabin_karp("HEL", "HELLO WORLD", 0, "Padrão no início")
            testar_rabin_karp("IS", "PYTHON IS FUN", 7, "Padrão no meio")
            testar_rabin_karp("TESTE", "TESTE", 0, "Padrão igual à string inteira")
            testar_rabin_karp("ABCDE", "ABC", -1, "Padrão maior que a string")
            print("Complexidade no pior caso: O(n*m), onde n = len(txt) e m = len(pat)")
        elif opcao == '3':
            testar_personalizado('Busca Simples', encontrar_primeira_ocorrencia)
        elif opcao == '4':
            testar_personalizado('Rabin-Karp', rabin_karp)
        elif opcao == '5':
            print("\nTestando KMP:")
            testar_kmp("ADF", "ABCDCBDCBDACBDABDCBADF", 19, "Padrão no final (exemplo do enunciado)")
            import random, string
            tamanho = 500_000
            txt_grande = ''.join(random.choices(string.ascii_uppercase, k=tamanho))
            pat_grande = txt_grande[-10:]
            testar_kmp(pat_grande, txt_grande, tamanho-10, "Padrão no final de string grande")
            testar_kmp("XYZ", "ABCDEFGH", -1, "Padrão não existe")
            testar_kmp("HEL", "HELLO WORLD", 0, "Padrão no início")
            testar_kmp("IS", "PYTHON IS FUN", 7, "Padrão no meio")
            testar_kmp("TESTE", "TESTE", 0, "Padrão igual à string inteira")
            testar_kmp("ABCDE", "ABC", -1, "Padrão maior que a string")
            print("Complexidade no pior caso: O(n + m), onde n = len(txt) e m = len(pat)")
        elif opcao == '6':
            testar_personalizado_kmp()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def kmp_search(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0] * M
    iteracoes = 0
    instrucoes = 0
    # Calcula o vetor LPS
    def compute_lps():
        len_lps = 0
        lps[0] = 0
        i = 1
        nonlocal instrucoes
        while i < M:
            instrucoes += 1
            if pat[i] == pat[len_lps]:
                len_lps += 1
                lps[i] = len_lps
                i += 1
            else:
                if len_lps != 0:
                    len_lps = lps[len_lps - 1]
                else:
                    lps[i] = 0
                    i += 1
    compute_lps()
    i = 0  # index para txt
    j = 0  # index para pat
    while i < N:
        iteracoes += 1
        instrucoes += 1
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            return i - j, iteracoes, instrucoes  # retorna o índice da primeira ocorrência
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1, iteracoes, instrucoes

if __name__ == "__main__":
    menu() 
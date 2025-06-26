def contar_inversoes(sequencia):
    inversoes = 0
    n = len(sequencia)
    
    for i in range(n):
        for j in range(i + 1, n):
            if sequencia[i] > sequencia[j]:
                inversoes += 1
    
    return inversoes

def determinar_vencedor(inversoes):
    if inversoes % 2 == 1:
        return "Marcelo"
    else:
        return "Carlos"

while True:
    linha = input().strip()
    if linha == "0":
        break
    
    dados = list(map(int, linha.split()))
    n = dados[0]
    sequencia = dados[1:]
    
    inversoes = contar_inversoes(sequencia)
    
    vencedor = determinar_vencedor(inversoes)
    print(vencedor)
def contar_inversoes(sequencia):
    inversoes = 0
    n = len(sequencia)
    
    for i in range(n):
        for j in range(i + 1, n):
            if sequencia[i] > sequencia[j]:
                inversoes += 1
    
    return inversoes

n = int(input())

for _ in range(n):
    l = int(input())
    
    if l == 0:
        print("Optimal train swapping takes 0 swaps.")
        continue
    
    vagoes = list(map(int, input().split()))
    
    trocas = contar_inversoes(vagoes)
    
    print(f"Optimal train swapping takes {trocas} swaps.")
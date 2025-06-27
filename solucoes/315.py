from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        contagens = [0] * n
        itens = [(nums[i], i) for i in range(n)]
        self._merge_sort(itens, 0, n - 1, contagens)
        return contagens

    def _merge_sort(self, itens: List[tuple], esquerda: int, direita: int, contagens: List[int]):
        if esquerda >= direita:
            return
        meio = esquerda + (direita - esquerda) // 2
        self._merge_sort(itens, esquerda, meio, contagens)
        self._merge_sort(itens, meio + 1, direita, contagens)
        self._merge(itens, esquerda, meio, direita, contagens)

    def _merge(self, itens: List[tuple], esquerda: int, meio: int, direita: int, contagens: List[int]):
        temp = []
        i = esquerda
        j = meio + 1
        menores_direita = 0

        while i <= meio and j <= direita:
            if itens[i][0] <= itens[j][0]:
                indice_original = itens[i][1]
                contagens[indice_original] += menores_direita
                temp.append(itens[i])
                i += 1
            else:
                menores_direita += 1
                temp.append(itens[j])
                j += 1

        while i <= meio:
            indice_original = itens[i][1]
            contagens[indice_original] += menores_direita
            temp.append(itens[i])
            i += 1

        while j <= direita:
            temp.append(itens[j])
            j += 1

        for k in range(len(temp)):
            itens[esquerda + k] = temp[k]

# --- Teste no VS Code ---
if __name__ == '__main__':
    solucao = Solution()
    exemplo = [5, 2, 6, 1]
    resultado = solucao.countSmaller(exemplo)
    print("Entrada:", exemplo)
    print("Saida esperada: [2, 1, 1, 0]")
    print("Saida obtida :", resultado)
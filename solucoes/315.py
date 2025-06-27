from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        Calcula o número de elementos menores à direita de cada elemento em nums.
        """
        n = len(nums)
        # Cria uma lista de resultados, inicializada com zeros.
        counts = [0] * n

        # Cria uma lista de tuplas (valor, índice_original) para rastreamento.
        # A função enumerate() do Python é perfeita para isso.
        # Trocamos a ordem para (valor, índice) para facilitar a ordenação.
        items = [(nums[i], i) for i in range(n)]

        # Chama a função auxiliar de merge sort.
        self._merge_sort(items, 0, n - 1, counts)

        return counts

    def _merge_sort(self, items: List[tuple], left: int, right: int, counts: List[int]):
        """
        Função recursiva de Merge Sort que ordena a lista 'items' e preenche 'counts'.
        """
        # Caso base da recursão: a sub-lista tem 0 ou 1 elemento.
        if left >= right:
            return

        mid = left + (right - left) // 2

        # Chamadas recursivas para as metades esquerda e direita.
        self._merge_sort(items, left, mid, counts)
        self._merge_sort(items, mid + 1, right, counts)

        # Combina as duas metades ordenadas.
        self._merge(items, left, mid, right, counts)

    def _merge(self, items: List[tuple], left: int, mid: int, right: int, counts: List[int]):
        """
        Combina duas sub-listas ordenadas (de 'left' a 'mid' e de 'mid+1' a 'right')
        e atualiza a contagem de elementos menores.
        """
        temp = []
        i = left          # Ponteiro para a sub-lista esquerda
        j = mid + 1       # Ponteiro para a sub-lista direita
        right_count = 0   # Contador de elementos da direita que são menores

        # Loop principal para combinar as duas metades
        while i <= mid and j <= right:
            # Se o elemento da esquerda é menor ou igual ao da direita
            if items[i][0] <= items[j][0]:
                # A mágica acontece aqui:
                # O número de elementos menores da direita que já vimos (right_count)
                # é adicionado à contagem do elemento atual da esquerda.
                original_index = items[i][1]
                counts[original_index] += right_count

                temp.append(items[i])
                i += 1
            else: # O elemento da direita é menor
                # Incrementamos nosso contador pois encontramos um elemento da direita
                # que é menor que o elemento atual da esquerda.
                right_count += 1

                temp.append(items[j])
                j += 1

        # Adiciona os elementos restantes da sub-lista esquerda
        while i <= mid:
            original_index = items[i][1]
            counts[original_index] += right_count # Todos os elementos da direita já foram contados
            temp.append(items[i])
            i += 1

        # Adiciona os elementos restantes da sub-lista direita
        while j <= right:
            temp.append(items[j])
            j += 1

        # Copia a lista temporária ordenada de volta para a lista original
        for k in range(len(temp)):
            items[left + k] = temp[k]


# --- Testes ---
if __name__ == '__main__':
    solver = Solution()

    # Exemplo 1
    nums1 = [5, 2, 6, 1]
    result1 = solver.countSmaller(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}") # Esperado: [2, 1, 1, 0]
    print("-" * 20)

    # Exemplo 2
    nums2 = [-1]
    result2 = solver.countSmaller(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}") # Esperado: [0]
    print("-" * 20)

    # Exemplo 3
    nums3 = [-1, -1]
    result3 = solver.countSmaller(nums3)
    print(f"Input: {nums3}")
    print(f"Output: {result3}") # Esperado: [0, 0]
    print("-" * 20)
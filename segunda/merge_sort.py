def mergeSort(alist):
    # Verifica se a lista tem mais de um elemento
    if len(alist) > 1:
        mid = len(alist) // 2  # Calcula o ponto médio da lista
        lefthalf = alist[:mid]  # Divide a lista em duas metades: left e right
        righthalf = alist[mid:]

        # Chama recursivamente mergeSort para ordenar as duas metades
        mergeSort(lefthalf)
        mergeSort(righthalf)

        # Inicializa variáveis de indice para controlar as posições na lista
        i = 0
        j = 0
        k = 0

        # Merge das sublistas ordenadas
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        # Adiciona os elementos restantes da metade esquerda à lista
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        # Adiciona os elementos restantes da metade direita à lista
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

# Exemplo de uso:
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print("Lista ordenada:", alist)
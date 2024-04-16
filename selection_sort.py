def selection_sort(arr):
    n= len(arr)
    for i in range(n):
        menor = i
        # Começando no segundo número para usar como comparação
        for j in range (i+1,n):
            if arr[menor] > arr[j]:
                menor = j
        arr[i], arr[menor] = arr[menor], arr[i]  # Troca de lugar se o número analisado for menor que o número mais à esquerda

a = [54,26,93,17,77,31,44,55,20]
selection_sort(a)
print(a)

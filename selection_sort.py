def selection_sort(lista):
    n=9
    for i in range(n):
        # Começando no segundo número para usar como comparação
        for j in range (i+1,n):
            if lista[i] > lista[j]:
                # Troca de lugar se o número analisado for menor que o número mais à esquerda
                lista[i], lista[j] = lista[j], lista[i]

a = [54,26,93,17,77,31,44,55,20]
print(selection_sort(a))
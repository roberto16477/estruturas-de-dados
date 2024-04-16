def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[0]        #Define o primeiro elemento do array como o pivo.
        menores_pivo = [elemento for elemento in arr[1:] if elemento <= pivo] #Cria uma lista com todos os elementos menores ou iguais ao pivo, excluindo o próprio pivo.
        maiores_pivo = [elemento for elemento in arr[1:] if elemento > pivo] #Cria uma lista contendo todos os elementos maiores que o pivo.
        ordena_menores = quick_sort(menores_pivo) #Recursão da função quick_sort para ordenar os elementos menores que o pivo.
        ordena_maiores = quick_sort(maiores_pivo) #Recursão da função quick_sort para ordenar os elementos maiores que o pivo.
        return ordena_menores + [pivo] + ordena_maiores #exibe as listas ordenadas uma antes e a outra depois do pivo.

# Exemplo de uso:
arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
arr_ordenado = quick_sort(arr)
print("Lista ordenada:", arr_ordenado)
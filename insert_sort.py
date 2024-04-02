def insertion_sort(lista):
    for i in range(1, len(lista)): #loop indo do segundo até o ultimo elemento da lista
        chave = lista[i]  #pega o valor armazenado no indice i
        j = i - 1   # j é a variavel que vamos usar para comparar o valor armazenado no indice i-1 (para comparar o primeiro com o segundo por exemplo)
        while j >= 0 and lista[j] > chave:  #verifica se o valor armazenado no indice j(i-1) é maior que o valor armazenado na variavel chave (i), se for ele entra para realizar a troca
            lista[j + 1] = lista[j]   #coloca o valor do indice j no indice j+1 (primeiro vai pro segundo)
            j -= 1
        lista[j + 1] = chave

lista = [5, 2, 8, 12, 1, 7]
insertion_sort(lista)
print(lista)  # Output: [1, 2, 5, 7, 8, 12]

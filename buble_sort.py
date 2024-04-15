def bubbleSort(arr):
    for passnum in range(len(arr)):  #essa linha me da um for que vai percorrer do inicio ao fim da lista
        for i in range((len(arr)-1)-passnum):  #essa linha evita que eu compare os numeros já organizados (os maiores, que vão estar no final)
            if arr[i]>arr[i+1]:      #compara o item i com o proximo item para ver se precisa ou não trocá-los
                temp = arr[i]     #variavel de apoio
                arr[i] = arr[i+1]   #faz a primeira troca (passa o item i+1 para a posição i)
                arr[i+1] = temp    #passa o item i para a posição i+1

a = [54,26,93,17,77,31,44,55,20]
bubbleSort(a)
print(a)
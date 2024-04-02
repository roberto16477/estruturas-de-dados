def bubbleSort(lista):
    for passnum in range(len(lista)):  #essa linha me da um for que vai percorrer do inicio ao fim da lista
        for i in range(len(lista)-1-passnum):  #essa linha evita que eu compare os numeros já organizados (os maiores, que vão estar no final)
            if lista[i]>lista[i+1]:      #compara o item i com o proximo item(se i for menor que i+1 ele troca) para ver se precisa ou não trocá-los
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

l = [54,26,93,17,77,31,44,55,20]
bubbleSort(l)
print(l)
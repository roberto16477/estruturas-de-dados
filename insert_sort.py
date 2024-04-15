def insertion_sort(arr):
    for i in range(1, len(arr)): #loop indo do segundo até o ultimo elemento do array
        chave = arr[i]  #pega o valor armazenado no indice i
        ant = i - 1   # ant é o valor anterior a i (i-1) (para comparar o primeiro com o segundo por exemplo)
        while ant >= 0 and arr[ant] > chave:  #verifica se o valor armazenado no indice j(i-1) é maior que o valor armazenado na variavel chave (i), se for ele entra para realizar a troca
            arr[ant + 1] = arr[ant]   #coloca o valor do indice ant no indice ant+1 (primeiro vai pro segundo)
            ant -= 1
            #print(arr)
        arr[ant + 1] = chave
        #print(arr)

a = [26,54,93,17,77,31,44,55,20]
insertion_sort(a)
print(a)  

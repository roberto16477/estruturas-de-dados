def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)  #informa a lista, define o leftmark como o primeiro elemento da lista e o rightmark como o ultimo elemento da lista

def quickSortHelper(alist,first,last): #essa função faz os marcadores caminharem
   if first<last:
                                            
       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1) #faz o rightmark caminhar
       quickSortHelper(alist,splitpoint+1,last)  #faz o leftmark caminhar


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
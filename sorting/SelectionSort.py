def selection_sort(array):
  for i in xrange(len(array)-1):
    min = i
    j = i + 1
    for j in xrange(len(array)):
      if array[j] < array[i]:
        min = j
    if min != i:
      temp = array[i]
      array[i] = array[min]
      array[min] = temp

array = [54,26,93,17,77,31,44,55,20]
selection_sort(array)
print array

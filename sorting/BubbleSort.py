def bubble_sort(array):
  for i in xrange(len(array)-1):
    for j in xrange(len(array)-1):
      if array[j] > array[j+1]:
        temp = array[j+1]
        array[j+1] = array[j]
        array[j] = temp

def optimized_bubble_sort(array):
  exchanged = True
  passes = len(array)-1
  while passes > 0 and exchanged:
    exchanged = False
    for i in range(passes):
      if array[i] > array[i+1]:
        exchanged = True
        temp = array[i+1]
        array[i+1] = array[i]
        array[i] = temp
    passes -= 1


array = [54,26,93,17,77,31,44,55,20]
bubble_sort(array)
print array
array2 = [54,26,93,17,77,31,44,55,20]
optimized_bubble_sort(array2)
print array2

def insertion_sort(array):
  for i in xrange(1, len(array)):
    current_val = array[i]
    position = i

    while position > 0 and array[position-1] > current_val:
      array[position] = array[position-1]
      position -= 1

    array[position] = current_val

array = [54,26,93,17,77,31,44,55,20]
insertion_sort(array)
print array

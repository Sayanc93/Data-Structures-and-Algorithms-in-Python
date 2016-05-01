def quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
      return array

array = [54,26,93,17,77,31,44,55,20]
print quick_sort(array)

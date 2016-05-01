def merge_sort(array):

  if len(array) > 1:
    mid = len(array)//2
    left_split = array[:mid]
    right_split = array[mid:]

    merge_sort(left_split)
    merge_sort(right_split)

    result = []
    i, j = 0, 0
    while i < len(left_split) and j < len(right_split):
      if left_split[i] < right_split[j]:
        result.append(left_split[i])
        i += 1
      else:
        result.append(right_split[j])
        j += 1

    while i < len(left_split):
      result.append(left_split[i])
      i += 1

    while  j < len(right_split):
      result.append(right_split[j])
      j += 1

array = [54,26,93,17,77,31,44,55,20]
merge_sort(array)
print(array)

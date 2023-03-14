def bubbleSort(x):
  length = len(x) - 1
  for i in range(length, 0, -1):
    for j in range(i):
      if x[j] > x [j+1]:
        x[j], x[j+1] = x[j+1], x[j]
  return x

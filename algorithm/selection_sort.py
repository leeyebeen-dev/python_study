def selectionSort(x):
	length = len(x)
	for i in range(length-1):
		for j in range(i+1, length):
			if x[i] > x[j]:
				x[i], x[j] = x[j], x[i]
	return x

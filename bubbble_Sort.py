def bubbleSort(sequence):
    n = len(sequence)
    for i in range(n-1):
        for j in range(n-i-1):
            if(sequence[j] > sequence[j+1]):
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]

seq = [83, 73, 8, 50, 29, 66, 46, 19]

seq = bubbleSort(seq)

print(seq)
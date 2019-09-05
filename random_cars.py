import random
import numpy

arr1 = numpy.array([[0]*4]*10)
arr2 = numpy.array([[0]*4]*10)
arr3 = numpy.array([[0]*4]*10)
arr4 = numpy.array([[0]*4]*10)

a = [0]*16
for i in range(16):
    a[i] = random.randrange(1,11)

print(a)
print()

n = 0
i = 0
while i != 4:
    for j in range(a[n]):
        arr1[j][i] = 1
    for k in range(a[n+1]):
        arr2[k][i] = 1
    for l in range(a[n+2]):
        arr3[l][i] = 1
    for m in range(a[n+3]):
        arr4[m][i] = 1
    n += 4
    i += 1

print(arr1)
print()
print(arr2)
print()
print(arr3)
print()
print(arr4)
print()
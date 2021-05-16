# Aufgabe 04
# Jürgen Weidig

def printArray(arr):
    print("array(" + np.array2string(arr) + ")")
    return    

def printArrayWithType(arr):
    print("array(" + np.array2string(arr) + ", dtype="+ str(arr.dtype) + ")")
    return  

# 1. Import numpy as np and see the version
import numpy as np
print(np.__version__)

# 2. How to create a 1D array?
arr = np.arange(10)
print("array(" + np.array2string(arr) + ")")

# 3. How to create a boolean array?
booArr = np.ones((3,3), dtype=bool) #np.full((3, 3), True, dtype=bool)
printArrayWithType(booArr)

# 4. How to extract items that satisfy a given condition from 1D array?
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(arr[arr % 2 == 1])
print("array(" + np.array2string(arr[arr % 2 == 1]) + ")")

# 5. How to replace items that satisfy a condition with another value in numpy array?
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.place(arr, arr % 2 ==1, -1)
print("array(" + np.array2string(arr) + ")")

# 6. How to replace items that satisfy a condition without affecting the original array?
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = np.where(arr % 2 == 1, -1, arr)
printArray(arr)
printArray(out)

# 7. How to reshape an array?
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = arr.reshape(2, 5) # out = arr.reshape(2, -1)
printArray(arr)
printArray(out)

# 8. How to stack two arrays vertically?
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
# out = np.concatenate([a,b], axis=0)
# out = np.vstack([a, b])
out = np.r_[a, b]
printArray(out)

# 9. How to stack two arrays horizontally?
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
out = np.concatenate([a,b], axis=1)
# out = np.hstack([a, b])
# out = np.c_[a, b]
printArray(out)

# 10. How to generate custom sequences in numpy without hardcoding?
a = np.array([1,2,3])
#out = np.r_[np.repeat(a, 3), np.tile(a, 3)]
out = np.hstack([np.repeat(a, 3), np.tile(a, 3)])
printArray(out)

# 11. How to get the common items between two python numpy arrays?
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
out = np.intersect1d(a, b)
printArray(out)

# 12. How to remove from one array those items that exist in another?
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
out = np.setdiff1d(a,b)
printArray(out)

# 13. How to get the positions where elements of two arrays match?
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
out = np.where(a == b)
print(out)

# 14. How to extract all numbers between a given range from a numpy array?
a = np.array([2, 6, 1, 9, 10, 3, 27])
#out = np.where((a >= 5) & (a <= 10))
out = np.where(np.logical_and(a>=5, a<=10))
print(out)

# 15. How to make a python function that handles scalars to work on numpy arrays?
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

pair_max= np.vectorize(maxx, otypes=[float])

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
printArray(pair_max(a, b))

# 16. How to swap two columns in a 2d numpy array?
arr = np.arange(9).reshape(3,3)
#printArray(arr)
#arr[:,[0, 1, 2]] = arr[:,[1, 0, 2]]
out = arr[:,[1, 0, 2]]
printArray(out)

# 17. How to swap two rows in a 2d numpy array?
arr = np.arange(9).reshape(3,3)
out = arr[[1, 0, 2],:]
printArray(out)

# 18. How to reverse the rows of a 2D array?
arr = np.arange(9).reshape(3,3)
out = arr[::-1]
printArray(out)

# 19. How to reverse the columns of a 2D array?
arr = np.arange(9).reshape(3,3)
out = arr[:, ::-1]
printArray(out)

# 20. How to create a 2D array containing random floats between 5 and 10?
#arr = np.random.randint(low=5, high=10, size=(5,3)) + np.random.random((5,3))
arr = np.random.uniform(5,10, size=(5,3))
printArray(arr)

# 21. How to print only 3 decimal places in python numpy array?
np.set_printoptions(precision=3)
out = np.random.random((5,3))
#out = arr[:4]
printArray(out)

# 22. How to pretty print a numpy array by suppressing the scientific notation (like 1e10)?
np.set_printoptions(suppress=False)
np.random.seed(100)
arr = np.random.random([3,3])/1e3
printArray(arr)
np.set_printoptions(suppress=True, precision=6)
printArray(arr)

# 23. How to limit the number of items printed in output of numpy array?
a = np.arange(15)
np.set_printoptions(threshold=6)
printArray(a)


# 24. How to print the full numpy array without truncating
np.set_printoptions(threshold=6)
a = np.arange(15)
printArray(a)
import sys
# np.set_printoptions(threshold=np.nan) --> nur in Python 2
np.set_printoptions(threshold=sys.maxsize)
printArray(a)


# 25. How to import a dataset with numbers and texts keeping the text intact in python numpy?
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#iris = np.genfromtxt(url, delimiter=',', dtype='object')
iris = np.genfromtxt(url, delimiter=',', dtype=None)
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
printArrayWithType(iris[:3])

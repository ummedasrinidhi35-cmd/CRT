"""import array
arr = array.array('f', [40.5, 10.0, 25.5, 60.0])
print(arr, type(arr))
arr.append(75.48)
print(arr)
arr.insert(2,24.5)
print(arr)
arr.remove(25.5)
print(arr)
"""
import numpy
arr = numpy.array([12,45,78,23,89])

"""Array is collection of homogeneous data elements that can store under a single variable python does not suppport arrays"""
"""NUMPY:
        Numpy--->Numeric Python
        it can easily access arrays
        Mainly uses in ML,DS,AI Applications
        
        the index value starts with 0 ans ends with(n-1)-->Siza of the array"""
import numpy as np
arr=np.array([10,20,30])
print(arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr))
print(np.zeros(8))
print(np.ones(5))
print("Even numbers list is:",np.arange(2,10,2))
print("Odd nubers list is:",np.arange(1,10,2))

n=int(input("Enter the size of array:"))
ele=list(map(int,input("Enter elements:").split()))
print("Array elements are:",np.array(ele))
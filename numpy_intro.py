import math
#getting the squareroot of a number by importing the whole module
A=25
print(math.sqrt(A))


#Importing a specific methos in the math module, use the from math import command

from math import sqrt
A=36
B=7
print(sqrt(A))
print(sqrt(B))



#NUMPY
#Numerical python is the foundational package for mathematical computing in python
#Supports ndarray(multidimensional arrays)
#Element-wise computations and mathematical calculations
#Linear algebraic operations, fourier transforms and random number generation
#Read and wrote array-based datasets from and to disks
#store and manipulate data
#Tools to intergrate language codes(C and C++)

#NDARRAY
#An array in NumPy is like a list but with additional features::
#1. Mathematical function support
#2. Multidimensional
#3. Fast and efficient
#4. Collection of values
#5. Single type(homogenous)
#6. Add, remove and update

#MATHEMATICAL FUNCTION SUPPORT

import numpy as np
from numpy import pi
#squareroot
num=np.sqrt([4,9,16,25,36])
print(num)

#cosine
print(np.cos(0))
print(np.cos(pi))


#sine
print(np.sin(pi/2))

#Round off the numbers to the nearest integer
print(np.floor([1.5,1.6,2.7,3.3,1.1,-0.3,-1.4]))

#calculates the exponential value of a floating-point argument
print(np.exp([0,1,5]))

#a numpy array
numpy_array1=np.array([1,2,3,4,5,6])
print(numpy_array1)

#A numpy array containing zeroes
numpy_array2=np.zeros((3,3))
print(numpy_array2)

#A numpy array containing ones 
numpy_array3=np.ones((2,2))
print(numpy_array3)

#A numpy array that is empty it will contain random numbers
numpy_array4=np.empty((2,3))
print(numpy_array4)

#A numpy array with arange method
numpy_array5=np.arange(12)
print(numpy_array5)

#reshaping the array, making it a two-dimensional or a multidimentional array
numpy_array6=numpy_array5.reshape(3,4)
print(numpy_array6)

#linspace for linearly (equal) spaced data elements
numpy_array7=np.linspace(1,6,10)
# 1 is the first element of the array
# 6 is the last element of the array
# 10 is the total number of elements in the array equidistant of one another
print(numpy_array7)

#SHAPE MANIPULATION
#one dimensional array 
oneD_array=np.arange(15)
print(oneD_array)

#two dimensional array 
twoD_array=oneD_array.reshape((3,5))
print(twoD_array)

#Three dimensional array
threeD_array=np.arange(27).reshape(3,3,3)
print(threeD_array)

#When using dynamic data sets when converting them to multidimensional array
#you need to use np.array(2,2,-1)
#It automatically calculates the last dimension into three
#you can flatten the array by using np.array(-1)

nump3=np.arange(12)
print(nump3)
print(nump3.reshape(2,2,-1))
print(nump3.reshape(-1))

#Arithmetic operations on numpy arrays is like adding matrices
#Adding
A=np.array([[1,2,3],[2,2,2]])
B=np.array([5,4,3])
print(np.add(A,B))

#Subtracting
print(np.subtract(A,B))

#Multiply
print(np.multiply(A,B))

#Divide
print(np.divide(A,B))

#To the power of
print(np.power(A,B))

#Conditional logic in numpy arrays
Z=np.array([i for i in range(11)])
print(Z)
print(np.where(Z%2==0,'even', 'odd'))

condlist=[Z<5,Z>5]
choicelist=[Z**2,Z**3]
print(np.select(condlist,choicelist,default=Z))

#Mathematical and statistical functions
arr=np.array([[4,3,2],[10,1,0],[5,8,25]])
print(arr)
print(np.amin(arr,axis=1))
print(np.max(arr,axis=0))
print(np.median(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.percentile(arr,50))

deg=np.array([10,20,30,40,50,60,70,80,90])
print(np.sin(deg*np.pi/180))
print(np.cos(deg*np.pi/180))
print(np.tan(deg*np.pi/180))

arr2=np.array([1.0,2.2,-3.5,-4.6,9.87,3.45])
#The floor method returns the values after rounding them off without the maths restrictions that a value after the decimal point should be more than 5 to be rounded off
print(np.floor(arr2))
#The ceil method returns the value after trancuating it
print(np.ceil(arr2))



#Indexing and slicing in python numpy arrays
#indexing
array_1d=np.array([1,2,3,4,5,6,7,8,9,10])
array_2d=np.array([[1,2,3,4,5],[6,7,8,9,10]])
array_3d=np.array([[[1,2,3],[4,5,6]],
                 [[7,8,9],[10,11,12]]])
print(array_1d[0])
print(array_2d[1,0])
print(array_3d[1,1,0])

#slicing
print(array_1d[2:5])
print(array_2d[1,1:3])
print(array_3d[1,1,0:])


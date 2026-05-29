import numpy as np

# arr = np.array([1,2,3])
# print(type(arr))


## 2-d arr

# arr2 = np.array([[1,2,3] , [4,5,6]])

# print(arr2)

# arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# # print(arr3)

## dtype : using dtype we can change the datatype of a numpy array.
# a1 = np.array([1,2,3] , dtype = float)
# # print(a1)

## arange : arange is used to generate numbers in between a given range . like range function using with for loop.

# a2 = np.arange(1,10)
# # print(type (a2))
# a3 = np.arange(1,11,2)
# # print(a3)

## reshape : it is used to give a shape to the numpy array (or we can reshape a array using this.)

# a1 = np.arange(1,11).reshape(5,2)
# print(a1)

# a2 = np.arange(1,25).reshape(2,12)
# print(a2)

### np.ones and np.zeros: np.ones create a np.array of ones . and np.zero create a np.array with value 0.

# a = np.ones((3,4) , dtype=int)
# print(a)


# a = np.zeros((4,4) , dtype=int)
# print(a)

## random : random is used to generate random values for a np. array in between  0 to 1.


# a = np.random.random((3,4))
# print(a*100 )

## linspace : linear space is used to generate numbers between a given range and havign equal distance with each other . 

# a = np.linspace(-10 , 10,10)
# print(a)

## np.identity:  it is used to generate identity matrix.

# a = np.identity(12)
# print(a)

## ARRAY  ATTRIBUTES : 

## ndim: it gives the dimension of an array
# a = np.arange(1,11)
# b = np.arange(1,17).reshape(4,4)

# c = np.arange(1,9).reshape(2,2,2)
# d  = np.arange(1,17).reshape(2,2,2,2)
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

## shape : shape tells that how many rows and columns exists in each dimension.

# a = np.arange(1,11)
# print(a.shape)
# b = np.arange(1,9).reshape(4,2)
# print(b.shape)
# c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(c.shape)

## size : size tells that how mant elements in an array.

# a = np.arange(1,33).reshape(2,2,2,2,2)
# print(a)
# print(a.size)

# a = np.array([[[[[ 1,2],
#     [ 3 , 4]],
#    [[ 5 , 6],
#     [ 7  ,8]]],
#   [[[ 9, 10],
#     [11 ,12]],
#    [[13, 14],
#     [15 ,16]]]],
#  [[[[17, 18],
#     [19 ,20]],
#    [[21, 22],
#     [23 ,24]]],
#   [[[25, 26],
#     [27 ,28]],
#    [[29 , 30],
#     [31 , 32]]]]] , dtype=np.int32)
# print(a.size)

### itemsize: it tells that how much size occupied by each element in an array. 
# print(a.itemsize)

# print(a.dtype)
# b = np.arange(1,11)
# print(b.dtype)

## astype : we can change the  datatype of a function. 

# a = np.array([[1,2],[3,4]])
# print(a)
# print(a.dtype)
# print(a.itemsize)
# a = a.astype(np.int32)
# print(a.dtype)
# print(a.itemsize)

## Array Operations : 

a1 = np.arange(12).reshape(3,4)
# print(a1)
a2 = np.arange(12,24).reshape(4,3)
# print(a2)

## scalar operations : 
## 1. Arithmetic : 
# print(a1*2)

## 2. relational : 
# print(a1 > 5)
# print(a1==5)

## Vector operations : operations thar are performed on two or more np arrays. but the shape must be same .

arr1 = np.arange(16).reshape(4,4)
arr2 = np.arange(16,32).reshape(4,4)
# print(arr1,arr2)
# print(arr1 + arr2)

### NUMPY Array fucntions : 
## min , max , sum , prod

# print(np.max(a1))
# print(np.min(a1))
# print(np.sum(a1))
# print(np.prod(a1))  # multiply with 0 

### 
# print(a1)
# print(np.max(a1,axis=1))      # 1 ---> rows
# print(np.min(a1 , axis=0))    # 0 ----> col

# print(np.sum(a1 , axis=1))

### mean / median / std/ var/

# print(a1)
# print(np.mean(a1 , axis=1))
# print(np.median(a1 , axis = 0))
# print(np.std(a1 , axis = 1))
# print(np.var(a1 , axis = 0))

### trignometric fucntions : 

# print(a1)
# a = np.array([30 , 45, 60 ,90])
# print(a)
# print(np.sin(a))
# print(np.tan(a))

### dot product : 

# print(a1)
# print()
# print(a2)

# print(np.dot(a1, a2))

## log and exponent : 

a = np.array([0,1,2,3])
# print(a)

# print(np.log(a))
# print(np.exp(a))

## round floor ceil : 

arr = np.array([[0.45975103 , 0.71408143 , 0.84777454],
                [0.70488086 ,0.80613501, 0.07630053]])
arr = arr*100
# print(arr)
# print(np.round(arr*100))
# print(np.round(arr))

# print(np.floor(arr))
# print(np.ceil(arr))

### indexing and slicing : 


# print(a1)
# print(a1[0::2,2:])

# print(a1[1: , 2:])
# print(a1[-1])
# print(a1[1: , 0::3])

a  = np.arange(1,28).reshape(3,3,3)
# # print(a)
# # print(a[2])
# # print(a[: , 2: , 0])
# print(a[1: , ::2 , ::2])

c = np.array([1,2,3,4,5,6,7,8,9])

# for i in c:
#     print(i)

# print(a1)
# for i in a1.ravel():
#     print(i)

# print(a)
# for i in a.ravel():
#     print(i%2==0)

### reshaping : : 
a = np.arange(1,16).reshape(3,5)
# print(a)

## transpose : transpose change the rows into columns and vice-versa.

# print(a.transpose())

# print(a.T)   

### stacing : 
a2 = np.arange(1,13).reshape(3,4)
# print(a1)
# print()
# print(a2)

## hstack : it merge both the arrays horizontally.


# print(a1)
# print()
# print(a2)
# print(np.hstack((a1,a2)))
# print(np.vstack((a1,a2)))

## spiliting : 

### hspilit: 
a = np.arange(36).reshape(6,6)
# print(a)

# print(np.hsplit(a ,2))
# print(np.vsplit(a ,3))

for i in np.hsplit(a , 3):
    print(i)
    print()
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)

# import numpy as np
# arr=np.array((1,2,3,3,4,4,5,6))
# print(arr)
# print(type(arr))



# 0Darry
# import numpy as np
# arr=np.array(42)
# print(arr)

# # 1Daary
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,])
# print(arr)

# list=[1,2,3,4,5] list print using comma but arry only print without comma 
# print(list)

 # 2Darray
# import numpy as np
# arr=np.array([[1,2,3],[1,2,3,]])
# print(arr)

# 3Darray
# import numpy as np
# arr=np.array([[[1,2,6,3],[1,2,3,9],[1,2,3,8]]])
# print(arr)


# import numpy as np
# arr=np.array([[[1,2,3,4,5],[34,55,67,88,78],[2,4,6,7,8,],[3,4,5,6,8]]]),
# ([[1,2,3,4,5,],[1,2,3,4,4,5]])
# print(arr)

# import numpy as np
# a=np.array(42)
# b=np.array([1,2,3,4,5,])
# c=np.array([[2,3,45,6,7]])
# d=np.array([[[1,2,3,4,5,]]])
# print(a.ndim,b.ndim,c.ndim,d.ndim) #ndim is
   

# import numpy as np
# arr = np.array([[[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],[[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]])
# print(arr[0, 1, 2, 3])

# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,4,5,6,7,8,4,3,2,4,5,6,7,89,995,4,3,5])
# print(arr[-8:-3])
 

# indexing
# import numpy as np
# arr=np.array([[[1,2,3,4,5,6,],[6,7,8,9,0,11],[22,33,44,55,66,77],[98,76,54,43,32,21]]])
# print(arr[0,3,3:4])


# import numpy as np
# # arr=np.array([1.1,2,2,3,3,4,5,6,7,8,9,10])
# arr=np.array(['1','2','3','4','5','6','7','8',"apple","mango"])
# print(arr.dtype)


# define datatype
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5,8], dtype='i2')
# print(arr.dtype)

# import numpy as np
# arr = np.array([1.1,2.2,3.3,4.4,5.5], dtype='f8')
# print(arr.dtype)/


# import numpy as np
# arr = np.array([1.1,2.2,3.3,4.4,5.5])
# newarr=arr.astype(type)
# print(newarr.dtype)


# import numpy as np
# arr = np.array([-1,0,1])
# newarr=arr.astype(bool)
# print(newarr)

# import numpy as np
# arr=np.array([1,2,3,4,5])
# x=arr.copy()
# arr[0]=42
# print(arr)
# print(x)
# import numpy as np
# arr=np.array([1,2,3,4,5,6])
# x=arr.view()
# arr[0]=42
# print(arr)
# print(x)

# arr = np.array([1, 2, 3, 4, 5, 6])
# x = arr.copy()
# y = arr.view()
# print(x.base)  # Output: None (copy does not share memory with the original array)
# print(y.base)  # Output: Original array (view shares memory with the original array)


# arr=np.array([1,2,3,5],ndmin=6)
# print(arr)
# print('share of array ',arr.shape)

# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr=arr.reshape(2,6)
# print(newarr)

# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,7])
# newarr=arr.reshape(3,3,3)
# print(newarr)


# arr=np.array([1,2,3,4,5,6,7,8,9,0,9,9,8,7,77,6])
# # newarr=arr.reshape(4, 4)  
# print( arr.reshape(2,12).base)



# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,])
# newarr=arr.reshape(2,2,-1)
# print(newarr)

# import numpy as np
# arr=np.array([[1,2,3],[4,5,6]])
# newarr=arr.reshape(-1)
# print(newarr)


# #  masking and filteirng
# import numpy as np 
# a=np.array([1,2,3,4,5,6,7])
# mask=a>3
# print(a[mask])

# #brodcasting
# import numpy as np
# a=np.array([1,2,3,4,5])
# b=5
# print (a+b)

# import numpy as np
# print(np.random.rand(3))
# print(np.random.randint(1,10,5))
# print(np.random . randn(3,3))
# print(np.random . seed(42))


# a=np.array([1,2,3,4,5,6,7,8,9,])
# gochu=[0,2,3,5]
# print(a[gochu])

# import numpy as np
# a=np.array(['cat','dog'],dtype='U6')
# print(a.dtype)

# from numpy.linalg import inv,det,eig
# a=np.array([[1,2],[3,4]])
# result=np.dot(a,a)
# inv(a)
# det(a)
# eig(a)
# print(result)
# print(inv(a),det(a),eig(a))

# a=np.array([[1,2],[3,4]])
# np.save('my_array.npy',a)
# np.load('data.csv',a,delimiter=',')
# np.genfromtxt('data.csv',delimiter=',')


# arr=np.array([np.nan,np.nan,np.nan])
# print(np.nan(arr))
# print(np.nan_to_num(arr))

# import pandas as pd

# data = {
#     'Name': ['alice', 'bob', 'charlie'],
#     'Age': [24, 27, 22],
#     'city': ['delhi', 'Mumbai', 'pune']
# }

# ghochu = pd.DataFrame(data)
# print(ghochu)

# df=pd.read_csv("student.csv")
# df.to_csv("output.csv",
#           index=False)

# df.head()first 5 rows
# df.tail() displaythe last three rows of the dataframe
# df.info()display the datatypes and null vales 
# df.colums()only return colums
 # df.discribe()summry statistics
#  # df.shape()get the shape of the dataframe
# data = {
#     'Name': ['alice', 'bob', 'charlie'],
#     'Age': [24, 27, 22],
#     'city': ['delhi', 'Mumbai', 'pune'],
#     'score': [56, 56, 78, 79, 23]
# }
# print("\ninfo:")
# df.info()


import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)



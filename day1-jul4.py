#generating common arrays 

import numpy as np

array = np.linspace(0,100,3)
print("Generated array:", array)

#arithmetic operations on array(matrices)
a = np.array([10,20,30])
b = np.array([1,2,1])

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#Vectorization

arr_3 = np.array([1,2,3,4,5])
result = arr_3 * 2
print("\nVectorization arr_3 * 2",result)

#indexing and slicing

arr_4 = np.array([10,20,30,40,50])
print("\nindex 0 to 4 ",arr_4[:])
print(" index 4 ",arr_4[-1:])
print(" index 2 to 3 ",arr_4[1:4])

#2D array indexing
 
data = np.array([
    [1,2,3],
    [5,6,7]
 ])

print(data[1,1])

# Statistical Analysis on Marks data

marks = np.array([80,90,89,79,92,78])

print("\nMarks = ",marks,"\n \n Statistical Analysis On Marks Data\n")
print("Mean: ",np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:",np.std(marks))
print("Variance:",np.var(marks))


#Aggregation Function

data_2 = np.array([10,20,30,40,50])

print("\n \n Aggregation Functions on\n",)

print(np.sum(data_2))
print(np.min(data_2))
print(np.max(data_2))

#Reshaping Data

arr_5 = np.arange(12)

print("\n\nReshaping arr_5 = ",arr_5,"\n")
new_array = arr_5.reshape(3,4)
print(new_array)


#Filtering Data

sales = np.array([100,200,300,400,500])
high_sales = sales[sales >250]
print("\n\n Hgh sales:",high_sales)

#random_number generation
print("\n\n")
print("floating point random nums:",np.random.rand(5))
print("10 integer random nums between 1 -100 ",np.random.randint(1,100,10))

print("\n\n")


#Linear Algebra

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print("dot product of A and B matrix: \n",np.dot(A,B))
print("\n\n")


#Practical data analysis Example

visitors = np.array([
    1200, 1500, 1800,
    1700, 2000, 2200,
    
])

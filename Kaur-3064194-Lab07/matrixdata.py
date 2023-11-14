'''
Author: Manvir Kaur
KUID: 3064194
Date: 10/25/2021
Lab: lab07
Last modified: 11/01/2021
Purpose: Writing Files with Matrix Information
'''

filename = input("Enter your file name: ")
diagonal_file = open("diagonal.txt", "w")
flipped_file = open("flipped.txt", "w")
reverse_file = open("reverse.txt", "w")
avg_file = open("averages.txt", "w")
input_file = open("input.txt", "r")

matrix = []
for line in input_file:
    matrix.append([])
    for num in line.split():
        matrix[-1].append(float(num))

def matrixstring(matrix):
    newmatrix = list(matrix)
    for index, row in enumerate(newmatrix):
        row = list(row)
        for i in range(len(row)):
            row[i] = str(row[i])
        row_str = " "
        newmatrix[index] = row_str.join(row)
    matrix_str = "\n"
    matrix_str = matrix_str.join(newmatrix)
    return matrix_str


fullaverage = 0
row = 0
for index in matrix:
    total = 0
    count = 0
    row = row + 1
    for num in index:
        total = total + num
        count = count + 1
    average = total/count
    fullaverage = fullaverage + average
total = "Total average: " + str(fullaverage/row)+ "\n"
avg_file.write(total)

row = 0
for index in matrix:
    total1 = 0
    count = 0
    row = row + 1
    for num in index:
        total1 = total1 + num
        count = count + 1
    average = total1/count
    rows = "Row " + str(row) + " average: " + str(average) + "\n"
    avg_file.write(rows)

avg_file.close()



reversematrix = [x[:] for x in matrix]
for i, row in enumerate(reversematrix):
    reversematrix[i] = row[::-1]
    
reverse_file.write(matrixstring(reversematrix))
reverse_file.close()



flip = matrixstring(matrix[::-1])
flipped_file.write(flip)
flipped_file.close()



symmatrix = [x[:] for x in matrix]
symmetric = []
for i in range(len(symmatrix)):
    sym = []
    for j in range(len(symmatrix)):
        sym.append(symmatrix[j][i])
    symmetric.append(sym)

diagonal_file.write(matrixstring(symmetric))
diagonal_file.close()
    


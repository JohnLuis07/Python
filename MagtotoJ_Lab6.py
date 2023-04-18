print("input your desire list to create a matrix don't forget to use semicolon for another row in the matrix.")
a = input('input1:' )
b = input('input2:' )

#for input1
smcolon = 0
for i in a:
    if i == ";":
        smcolon +=1 #total number of the semicolon

nestl = a.split("; ", smcolon) #divider, put how many semi colon

nestli = [[] for i in range(smcolon +1)] #make brackets for nested list, added one for the sublists, 1 semicolon - 2 sublists, 2 - 3, so on [[], []]

for i in range(smcolon +1):
    nestli[i] = [int(j) for j in nestl[i].split(", ")]#convert list to int

#for input2
smcolon1 = 0
for i in b:
    if i == ";":
        smcolon1 +=1

nestl1 = b.split("; ", smcolon1)
print(nestl)
nestli2 = [[] for i in range(smcolon1 +1)]

for i in range(smcolon1 +1):
    nestli2[i] = [int(j) for j in nestl1[i].split(", ")]

print()
print('input1: ')
for k in nestli: #to print the first matrix
    print(k)
b = len(k) #determine the column of matrix 1

print()
print('input2: ')
p = 0 
for k2 in nestli2: #to priny the second matrix
    p += 1 #total row in matrix 2
    print(k2)
print("input1: ", nestli)
print("input2: ", nestli2)
print()
if p == b:
    product = [[sum(q*r for q,r in zip(nestli_row,nestli2_col)) for nestli2_col in zip(*nestli2)] for nestli_row in nestli] #process for multiplication 
    print("product: ", product)                                                                                                                        
else:
    print("Cannot be multiplied.")

#for the product: for the nestli_row in nestli, it will result to
#[1, 2, 3]
#[4, 5. 6]

#for nestli2_col in zip(*nestli2)
#[1, 3, 5]
#[2, 4, 6]

#sum(q*r for q,r in zip(nestli_row,nestli2_col)
#1*1 + 2*3 + 3*5 = 22    1*2 + 2*4 + 3*6 = 28
#4*1 + 5*3 + 6*5 = 49   4*2 + 5*4 + 6*6 = 64 

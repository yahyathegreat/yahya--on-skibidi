print("half the pyrimads of stars(*):")
n = int(input("enter the numbers of rows: "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()
rows =int(input("please enter the total number of rows : "))
number = 1
print("floyd's triangle")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end = '  ')
        number = number + 1
    print()
rowsize = int(input("enter the names of rows: "))
ifrowsize%2==0:
  halfdiamrow = int(rowsize/2)
else:
  halfdiamrow = int(rowsize/2)+1
space = halfdiamrow-1
num=1
for i in range(1, halfdiamrow+1):
  for j in range(1, space+1):
    print(end="")   
space = space-1
num = 1
for j in range(2*i-1):
   print(end=str(num))
   num = num+1
print()
space = 1
     
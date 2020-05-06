i=0
j=1
count=0
n=int(input('input the number: '))
if(n<=0):
    print('invalid number')
else:
   while count < n:
       print(i)
       sum = i + j
       i = j
       j = sum
       count += 1

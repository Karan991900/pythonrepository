l=[1, 2, 3, 4, 5]
sum_even=0
sum_odd=0
for i in l:
       if i%2==0:
              sum_even=sum_even+i 
       else:
              sum_odd=sum_odd+i
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)
list=[10,20,30,40,50]
even_sum=0
odd_sum=0
i=0
while i<=len(list)-1:
    if list[i]% 2==0:

        even_sum=even_sum+list[i]
    else:
        odd_sum=odd_sum+list[i]
    i=i+1
print(even_sum)
print(odd_sum)

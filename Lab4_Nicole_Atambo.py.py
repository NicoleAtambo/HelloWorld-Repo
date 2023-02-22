#selection statements
#loops
#nested loops

#c represents count of the numbers either perfect, deficient
a=int(input("Enter an upper bound for a check: "))
sum=0
c=0
c1=0
c2=0
if(a>0):
    print("between 1 and", a, "there are: ")
for i in range(1, a+1):
    for k in range(1, i):
        if i%k==0:
            sum=sum+k
    if sum<i:

        c1=c1+1
    elif sum==i:

        c=c+1
    elif sum>i:

        c2=c2+1

    else:
        print("Invalid")
    sum=0
print(c1, "deficient numbers")
print(c, "perfect numbers")
print(c2, "abundant numbers")

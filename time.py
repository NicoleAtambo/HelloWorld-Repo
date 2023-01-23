print("What is the number of seconds")
#oneday= 86400 seconds
no_of_seconds=int(input())
x= no_of_seconds//3600
y=(no_of_seconds%3600)//60
b=(no_of_seconds%3600)%60
print("Hours: " ,x)
print("Minutes: " ,y )
print("Seconds: " ,b)

#Advanced calculation
print("Enter number of seconds at beginning of the year ")
no_of_seconds= int(input())

"""
1day=86400 seconds
d=days
x= hours
y=minutes
a=seconds
b=population
c=birth
e=death
f=immigrant
g=flapjacks
"""
d=(no_of_seconds)//86400
x=(no_of_seconds%86400)//3600
y=(no_of_seconds%3600)//60
a=(no_of_seconds%3600)%60

total_seconds = (6* 24 * 3600) + (12 * 60 * 60) +31 * 60 + 30
c = total_seconds// 7
e= total_seconds // 13
f= total_seconds // 35
b=c + f +334205119 -e

g=(((334205119+350)**2-12)//50)**(1/5)
flapjack=int(g)
print("Days: " ,d, "Hours: " ,x, "Minutes: " ,y, "Seconds: " ,a, "After the start of 2022, the total population was: " ,b)
print("The average amount of flapjacks eaten is: ", flapjack)

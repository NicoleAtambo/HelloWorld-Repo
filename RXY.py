a={"Nicole":90,"Maria":94,"Lisah":87,"Amina":72,"Sal":70 }
a.update({"Sam":78,"Ria":88,"Marie":92})

abt=len(a)
print(abt)

#average for class
total=sum(a.values())
avg=total/abt
print(avg)
#number of students above class average
numOfStud=0
for scores in a.values():
	
	if scores>avg:
		
		numOfStud+=1
print(numOfStud)

#the student with the highest score(value)
p=list(a.values())
print(a)
p.sort()
print(p[-1])

#student Marie apply for re evaluation from 92 to update to 95
a.update({"Sam": 95})
print(a)

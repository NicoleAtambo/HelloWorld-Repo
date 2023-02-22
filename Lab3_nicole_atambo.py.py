sales=int(input("Enter the amount you sold in 2022: "))
#a=input("Are you a senior associate or junior associate: ")
b=input("Type s for senior associate and j for junior associate: ")

if (sales>=0 and sales<=5000) and b=='j':
	comm=0.03*sales
	print("This year you made: ",comm, "in sales commission")
	
elif(sales>=0 and sales<=5000) and b=='s':
	comm=0.04*sales
	print("This year you made: ",comm, "in sales commission")

elif(sales>=5001 and sales<=25000) and b=='j':
	comm=(sales-5000)*0.04+(5000*0.03)
	print("This year you made: ",comm, "in sales commission")
	
elif(sales>=5001 and sales<=25000) and b=='s':
	comm=(sales-5000)*0.05+(5000*0.04)
	print("This year you made: ",comm, "in sales commission")

elif(sales>=25001 and sales<=100000) and b=='j':
	comm=(sales-25000)*0.05+(20000*0.04)+(5000*0.03)
	print("This year you made: ",comm, "in sales commission")

elif(sales>=25001 and sales<=100000) and b=='s':
	comm=(sales-25000)*0.07+(20000*0.05)+(5000*0.04)
	print("This year you made: ",comm, "in sales commission")
	
elif(sales>=100001) and b=='j':
	comm=(sales-100000)*0.07+(75000*0.05)+(20000*0.04)+(5000*0.03)
	print("This year you made: ",comm, "in sales commission")
	
elif(sales>=100001) and b=='s':
	comm=(sales-100000)*0.10+(75000*0.07)+(20000*0.05)+(5000*0.04)
	print("This year you made: ",comm, "in sales commission")
	
elif(sales<0):
	print("Go to HR")



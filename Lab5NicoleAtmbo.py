"""



"""



def main():


	#encodedWord = "tx33dom"
	#encodedWord = "t3xb3f"
	#encodedWord = "koxb3zpond3nk3"
	#encodedWord = "fako fim3"
	#encodedWord = "zom3 xafz bun"	
	#encodedWord = "txiday tun tob tx3nkh tbi3z"
	encodedWord = "kafz kan kafkh kakfuz3z wifh klawz"
	
		
	#encodedWord = "UUHO"  		#Used for Bonus
	#encodedWord = "EOUUUUOUU" 	#Used for Bonus
	
	print(DecodeWord(encodedWord))






#Your code goes here.
def DecodeWord(encodedWord):
	for i in encodedWord :
		if i=='t':
			print("f",end='')
		elif i=='f':
			print("t",end='')
		elif i=='k':
			print("c",end='')
		elif i=='s':
			print("z",end='')
		elif i=='b':
			print("r",end=='')
		elif i=='x':
			print("r",end='')
		elif i=='3':
			print("e",end='')
		else:
			print(i,end='')
	return ""
		
	











#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	
if __name__ == "__main__":
	main()

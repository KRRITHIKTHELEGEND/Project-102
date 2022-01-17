import os

def folder():
	folderName = input("Enter the name of the folder: ")
	print(" ")
	  
	location = input("Enter the path where you want to create the folder: ")
	print(" ")
	  
	path = os.path.join(location, folderName)
	  
	
	os.mkdir(path)
	print("Wo hooo !!! Your Directory", "'", folderName, "'", "is created.")

def calc():
	equation=input("addition, subtraction, multiplication or division ? ")
	if(equation=='addition'):
		os.system('cls')
	    firstNumber=int(input("type your first number : "))
	    secondNumber=int(input("type you second number : "))
	    result=firstNumber+secondNumber
	    print("Your Result Is : ", result)
	elif(equation=='a'):
		os.system('cls')
	    firstNumber=int(input("type your first number : "))
	    secondNumber=int(input("type you second number : "))
	    result=firstNumber+secondNumber
	    print("Your Result Is : ", result)
	elif(equation=='add'):
		os.system('cls')
	    firstNumber=int(input("type your first number : "))
	    secondNumber=int(input("type you second number : "))
	    result=firstNumber+secondNumber
	    print("Your Result Is : ", result)

	elif(equation=='subtraction'):
		os.system('cls')
	    firstNumber=int(input("type your first number : "))
	    secondNumber=int(input("type you second number : "))
	    result=firstNumber-secondNumber
	    print("Your Result Is : ", result)
	elif(equation=='s'):
		os.system('cls')
	    firstNumber=int(input("type your first number : "))
	    secondNumber=int(input("type you second number : "))
	    result=firstNumber-secondNumber
	    print("Your Result Is : ", result)
	elif(equation=='sub'):
		os.system('cls')
	    firstNumber=int(input("type your first number : "))
	    secondNumber=int(input("type you second number : "))
	    result=firstNumber-secondNumber
	    print("Your Result Is : ", result)
	
	elif(equation=='multiplication'):
		os.system('cls')
	    firstNumber=int(input("type your first number : "))
	    secondNumber=int(input("type you second number : "))
	    result=firstNumber*secondNumber
	    print("Your Result Is : ", result)
	elif(equation=='m'):
		os.system('cls')
	    firstNumber=int(input("type your first number : "))
	    secondNumber=int(input("type you second number : "))
	    result=firstNumber*secondNumber
	    print("Your Result Is : ", result)
	elif(equation=='mul'):
		os.system('cls')
	    firstNumber=int(input("type your first number : "))
	    secondNumber=int(input("type you second number : "))
	    result=firstNumber*secondNumber
	    print("Your Result Is : ", result)
	
	elif(equation=='division'):
		os.system('cls')
	    firstNumber=int(input("type your first number : "))
	    secondNumber=int(input("type you second number : "))
	    result=firstNumber/secondNumber
	    print("Here Ya Go... Your Result Is ", result)
	elif(equation=='d'):
		os.system('cls')
	    firstNumber=int(input("type your first number : "))
	    secondNumber=int(input("type you second number : "))
	    result=firstNumber/secondNumber
	    print("Here Ya Go... Your Result Is ", result)
	elif(equation=='div'):
		os.system('cls')
	    firstNumber=int(input("type your first number : "))
	    secondNumber=int(input("type you second number : "))
	    result=firstNumber/secondNumber
	    print("Here Ya Go... Your Result Is ", result)
	
	else:
	    print("That is not a valid input idiot")

something = input("Calculator or New Folder ? \n\n")
if(something == 'Calculator'):
	os.system('cls')
	calc()
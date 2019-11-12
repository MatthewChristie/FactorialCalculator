#Created by Matthew Christie
#31/10/2019
#Adding an Array to sort and display answers on 1 line


from os import system

system("title Factorial Calculator")
n = 1

factorialinput = input("Factorial of...? ")
factorialinput = int(factorialinput)


array = [0]

looping = factorialinput * (factorialinput - 1)
print(looping)
print ("F:", factorialinput)
factorialinputL = factorialinput - 1

while n != (factorialinput - 1):
    looping = looping * (factorialinputL - 1)
    n = n + 1
    factorialinputL = factorialinputL - 1
    print("F2: ", factorialinputL)
    #currentnumber = looping
    print(looping)
    #array[n] = looping
    print ("Array No.: ", n)

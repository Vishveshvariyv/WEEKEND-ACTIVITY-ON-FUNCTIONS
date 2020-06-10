#7.        Define a function that can accept two strings as input and print the string with maximum length 
# in console. 
# If two strings have the same length, then the function should print all strings line by line.

def q7(input1,input2):

    
    if len(input1) == len(input2) :
        print(input1)
        print(input2)
    elif len(input1) > len(input2):
        print(input1)
    else:
        print(input2)    
input1=input("Enter a string: ")
input2=input("Enter second string: ")
q7(input1,input2)         
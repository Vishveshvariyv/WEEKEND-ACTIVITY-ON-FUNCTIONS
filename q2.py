#2. 	Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
#Expected Output:
#No. of Upper case characters : 3
#No. of Lower case Characters : 12
s="AppleAppLE"
def q2(s):
    countUp=0
    countLow=0
    for x in s:
        if x.isupper():
            countUp+=1
        elif x.lower():
            countLow+=1
        else:
            pass
    print("No. of Upper case characters :", countUp)
    print("No. of Lower case Characters :", countLow)                
   
q2(s)
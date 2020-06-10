#4.Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a
#  hyphen-separated sequence after sorting them alphabetically.
def q4():
    data=input("Enter hyphen-separated sequence of words").split('-')
    data.sort()
    print(data)
q4()    




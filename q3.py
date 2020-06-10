#3.        Create a function that takes a list and returns a new list with unique elements of the first list.

data=[1,2,2,3,4,3,4,1,5,6]

def q3(data):
    newData=[]
    for i in data:
        if i not in newData:
            newData.append(i)
    print(newData) 

q3(data)

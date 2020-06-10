#10.Write a program which can filter() to make a list whose elements are even number between 1 and 20 
# ( both included)

def filter():
    l1=list()
    for i in range(1,20):
        if i%2==0:
            l1.append(i)

    print(l1)
filter()            
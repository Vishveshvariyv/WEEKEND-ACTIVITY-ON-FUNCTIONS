#8. Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.

def q8():
    tp=tuple()
    l1=list(tp)
    for i in range(1,20):
        l1.append(i**2)
    tp=tuple(l1) 
    print(tp)
q8()      
        

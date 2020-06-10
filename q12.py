#12. 	Write a function to compute 5/0 and use try/except to catch the exceptions

def q12():  
       
    try:
        print(5/0)
    except ZeroDivisionError as e:
        print(e)

q12()    


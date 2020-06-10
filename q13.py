#13. 	Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
#Goal : Turn [1,2,3,4,5,6,7] to 1234567 

from functools import reduce

def q13():
    ini_list = [[1, 2, 3], 
            [3, 6, 7], 
            [7, 5, 4]] 
              

    print ("initial list ", str(ini_list)) 
    flatten_list = reduce(lambda z, y :z + y, ini_list) 
  

    print ("final_result", str(flatten_list)) 


q13()

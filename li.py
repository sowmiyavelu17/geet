test_list = [4, 5, 6, 3, 9] 
print ("The original list is : " + str(test_list)) 
res = [i for i in test_list for x in (0, 1)] 
print ("The list after element duplication " +  str(res)) 
 

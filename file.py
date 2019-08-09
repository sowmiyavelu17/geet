def floor_log(num, base):
    if num< 0:
       raise ValueError("Non-negative number only.")
    exponent=0
    while num >1:
        num >>= 1
        exponent += 1
    return base << (exponent - 1)
 
print floor_log(3,2) #2 
print floor_log(4,2) #4
print floor_log(5,2) #4
print floor_log(6,2) #4

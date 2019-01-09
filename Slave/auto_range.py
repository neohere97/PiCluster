lower_limit = input("Give the lower limit")
upper_limit = input("Give the upper limit")
cycles = 0

no_of_splits = 20
ranges = []
k = 0
l = 0
for i in range(int(lower_limit),int(upper_limit)+1):
    cycles = cycles + i

equalized_cycles = int(cycles/no_of_splits)

split_cycles = 0
lower_limit_range = 0
upper_limit_range = 0
for i in range(int(lower_limit),int(upper_limit)+1):    
    split_cycles = split_cycles + i
    if(split_cycles >= equalized_cycles):
        upper_limit_range = i
        ranges.append([lower_limit_range,upper_limit_range])        
        lower_limit_range = i
        split_cycles = 0
        k = k+1

    if(k+1 == no_of_splits):
        ranges.append([lower_limit_range,int(upper_limit)])
        break


print(ranges)


    




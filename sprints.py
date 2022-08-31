def MyFunc(list):
    sum=0
    counter =0
    max = 0
    if len(list) ==0:
        return 0
    for i in list:
        check_float = isinstance(i, float)
        if((i%2)==0 & check_float == False):
            sum += i
            counter+=1
        elif(check_float):
            if(i >= max):
                max = i
            else:
                max= max
    mean = sum/ counter
    return mean, max

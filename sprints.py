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
print("Mean and maximum values of the list: ",MyFunc([2,33,1,4,5.6,8.2,9.5,5.1,8.2,0.1,6.5,10.2,7.4,-4.1]))
print(MyFunc([]))
x = input("Years: ").split('-')  #users input that accepts dash
#converts the years into integer to manipulat them with the use of operators
y = int(x[0]) 
z = int(x[1])
if y > 1582: #Prevents user to put year that are less than 1582 
    res = [] #creates a blank list to be fill in later with leap years
    while y < z: #this will run until it reach the ite range in it
        y += 1
        if y % 4 == 0: #divides the years by four, if the remainder is eqaul to zero then it wull proceed to the next condition
            if y % 100 == 0:#if the year is not divisible by 100 then it is a leap year, if it is divisible it will proceed to the next condition
                if y % 400 == 0:#if the year is divisible to 400 then it is a leap year if not, then it is not a leap year
                    res.append(y)#the following year will be added as an element in the blank list
            else:
                res.append(y)#the following year will be added as an element in the blank list
    print('Output: ', len(res), "- ", end = "")#wpresent the total number of leap year
    for i in res:
        print(i, sep = ",", end =" ") #remove the bracket in the list 
else:
    print('Output: ', 'Invalid range')            
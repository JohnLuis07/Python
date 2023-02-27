print("All caps only for choosing your desire conversion.")
ask = input('HINDU TO ROMAN or ROMAN TO HINDU?:')
if ask == 'HINDU TO ROMAN':     #Hindu to roman if true
    x = int(input('input any hindu arabic:'))
    while x < 1:
        x = int(input("Numbers must be not less that 0 please input again"))
    def rom(x):
        Hindu_Arabic = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        roman = ['I', 'IV', 'V', 'IX', 'X','XL', 'L','XC', 'C', 'CD', 'D', 'CM', 'M']
        i = 12 #I use this to count the list into reverse mode
        rom = (' ')
        while x > 0: #execute until the value of input isn't 0
            if Hindu_Arabic[i] <= x:    #Hindu_Arabic[i] will start at last which is 1000. 
                rom += roman[i]         #convert the index that first satisfies the condition
                x = x - Hindu_Arabic[i] #subtract the input to the index of hindu arabic that satisfied the condition
            else:
                i = i - 1 #subtract the index until it satisfies the condition
        return rom 
    print('Output:', rom(x))
elif ask == 'ROMAN TO HINDU': #Roman to hindu if the first conditional statement is false
    y = input("Roman Numeral: ").upper()
    z = len(y)
    RtoInt = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} #Dictionary for Roman to Integer
    output = 0 #This will be the answer later
    for i in range(z): #solution to combine the value of Roman Numerals
        initial_value = (RtoInt[y[i]]) 
        if i + 1 < z and initial_value < (RtoInt[y[i+1]]): #The main purpose of this is for IV yL CD CM the first number must be smaller than the neyt
            output = output - initial_value #This will deduct the total amount in output
        else:
            output = output + initial_value #add the total amount of the out put
    print('Output:', output)
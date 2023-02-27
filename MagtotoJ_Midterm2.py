x = list("“this is a sample list 1,2,3,4}”")
z = ''.join(x)
y = 0
#this process will count how many brackets are there
#for ()
for i in range(len(x)):
    if x[i] == '(':
        y += 1 #this means one of the pair is there
    elif x[i] == ')':
        y -= 1 #this means one of the pair is there
               #if both if and else execute that means it has a pair brackets
#Same as line 6 but different symbol
#for []
for i in range(len(x)):
    if x[i] == '[':
        y += 1
    elif x[i] == ']':
        y -= 1
#for {}
for i in range(len(x)):
    if x[i] == '{':
        y += 1
    elif x[i] == '}':
        y -= 1
if y == 0:  #this condition is whether the [{()}] is with pair or not
    print('Matched!')
else:
    blank = []
    for j in z:
        if j in "{[()]}":
            blank.append(j)
    list_to_str = ""
    for k in blank: #removes the pair brackets, it will only get the pair
        list_to_str =  list_to_str.replace("()", "")
        list_to_str =  list_to_str.replace("[]", "")
        list_to_str =  list_to_str.replace("{}", "")
        list_to_str += k
    position = z.find(list_to_str) + 1 #finds the position of the brackets that are not in pair
    print('Output: Mismatch at position', position)
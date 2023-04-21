# X → xY
# Y → ZwY | xY | ∈
# Z → yW
# W → zW | ∈

str = input("Enter string to be parsed: ") + "$"
global i
i = 0

def W():
    global i, str
    if str[i] == 'z':
        i += 1
        W()
def Y():
    global i, str
    if str[i] == 'x':
        i += 1
        Y()
    elif str[i] == 'y':
        i += 1
        W()
        if str[i] == 'w':
            i += 1
            Y()
        else:
            i -= 1 #we do this to simply mismatch str in the end since if it doesnt match with w it is not correct

def X():
    global i, str
    if str[i] == 'x':
        i += 1
        Y()
    else:
        return
    
X()
if (i == len(str) - 1):
    print("Accepted!")
else:
    print("Rejected")


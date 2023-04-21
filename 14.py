str = input("Enter expression: ")

variables = []
operators = []
def isOperator(str):
    op = ['+', '-', '*', '/', '=']
    if str in op:
        return True
    return False

temp = ""
for ch in str:
    if(isOperator(ch)):
        variables.append(temp)
        temp = ""
        operators.append(ch)
    else:
        temp += ch
if len(temp) != 0:
    variables.append(temp)

r = 0
for i in variables:
    if r == 0:
        r += 1
        continue
    ch = "{}".format(r)
    print("MOV R" + ch + ", " + i)
    r += 1

print()

i = len(operators) - 1
while i >= 0:
    j = len(variables) - 1
    a = variables.pop()
    b = variables.pop()
    if operators[i] == '+':
        print("ADD R" + "{}".format(j - 1) +", R" + "{}".format(j))
        variables.append("R" + "{}".format(j - 1))
    
    elif operators[i] == '-':
        print("SUB R" + "{}".format(j - 1) +", R" + "{}".format(j))
        variables.append("R" + "{}".format(j - 1))

    elif operators[i] == '*':
        print("MUL R" + "{}".format(j - 1) +", R" + "{}".format(j))
        variables.append("R" + "{}".format(j - 1))

    elif operators[i] == '/':
        print("DIV R" + "{}".format(j - 1) +", R" + "{}".format(j))
        variables.append("R" + "{}".format(j - 1))

    elif operators[i] == '=':
        print("MOV " + b + ", R" + "{}".format(j))
    i -= 1
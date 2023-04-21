file = open("1.txt", 'r')
mcomment = False
mstr = ""
lines = file.readlines()
print(lines)
for line in lines:
    if line[0:2] == '/*':
        mcomment = True
    elif line[0:2] == '//':
        pass
        print(line)
    if line[-3:] == '*/\n':
        mstr += line
        print(mstr)
        mstr = ""
        mcomment = False
    if mcomment == True: 
        mstr += line

if mcomment == True: 
    print(mstr)
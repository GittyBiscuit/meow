import sys
# a*bb+a*
a1, b, a2 = 0, 0, 0

str = input("Enter input string: ")

for ch in str:
    if ch == 'a':
        if b > 0:
            a2 += 1
        else:
            a1 += 1
    elif ch == 'b':
        if a2 > 0:
            print("Invalid String")
            sys.exit()
        b += 1

if (a1 >= 0 and b >= 2 and a2 >= 0):
    print("Valid String")
else:
    print("Invalid String")




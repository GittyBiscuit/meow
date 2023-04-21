file = open("3.txt", "r")
# formatting lines
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

token_count = 0
punctuators = set()
valid_ids = set()
tokens = set()
constants = set()
invalid_ids = set()

def isPunctuator(str):
    punch = ["+", "-", "*", "/", ",", ";", ">", "<", "=", "(", ")", "[", "]", "{", "}", "&", "|"]
    if str in punch:
        return True
    return False

def isKeyword(str):
    keywords = ["asm","double","new","switch", 
                "auto","else","operator","template", 
                "break","enum","private","this",
                "case","extern","protected","throw",
                "catch","float","public","try",
                "char","for","register","typedef",
                "class","friend","return","union",
                "const","goto","short","unsigned",
                "continue","if","signed","virtual",
                "default","inline","sizeof","void",
                "delete","int","static","volatile", "do","long","struct",
                "while", "main", "int", "if", "return", "cout"]
    if str in keywords:
        return True
    return False

def isValidIdentifier(str):
    special = ["$", "@", "#"]
    if str[0].isdigit() or str[0] == "_":
        return False
    for ch in str[0]:
        if ch in special:
            return False
    return True

def isConst(str):
    if str.isnumeric():
        return True
    return False

for i in range(len(lines)):
    temp = lines[i].split()
    for token in temp:
        if token[-1] == ';' and len(token) >= 2:
            punctuators.add(token[-1])
            token = token[:-1]
            token_count  += 1
        if isPunctuator(token):
            punctuators.add(token)
        elif isKeyword(token):
            tokens.add(token)
        elif isConst(token):
            constants.add(token)
        elif isValidIdentifier(token):
            valid_ids.add(token)
        else:
            invalid_ids.add(token)
        token_count += 1
        
print("total tokens: " + str(token_count))
print("Punctuators: " + ', '.join(punctuators))
print("constants: " + ', '.join(constants))
print("tokens: " + ', '.join(tokens))
print("valid ids: " + ', '.join(valid_ids))
print("invalid ids: " + ', '.join(invalid_ids))

def getTerms_NonTerms(grammar):
    nonTerms = set()
    terms = set()
    for prod in grammar:
        i = 0
        for i in range(len(prod)):
            if i == 1 or i == 2:
                continue
            if prod[i].isupper() and prod[i] != '#':
                nonTerms.add(prod[i])
            elif not prod[i].isupper() and prod[i] != '#':
                terms.add(prod[i])
    return [terms, nonTerms]

# not perfect lol
def firstUtil(non_terminal, nonTerms, terms, grammar):
    arr = set()
    for prod in grammar:
        if prod[0] == non_terminal:
            i = 3
            if prod[i] in terms:
                arr.add(prod[i])
            elif prod[i] in nonTerms and prod[i] != non_terminal:
                temp = firstUtil(prod[i], nonTerms, terms, grammar)
                for i in temp:
                    arr.add(i)
            elif prod[i] == '#':
                arr.add('#')
    return arr
            

def findFirst(terms, nonTerms, grammar):
    first = {}
    for non_terminal in nonTerms:
        first[non_terminal] = firstUtil(non_terminal,nonTerms, terms, grammar)
    return first
# taking input 
file = open("5.txt", "r")

grammar = []

lines = file.readlines()
for line in lines:
    grammar.append(line.strip())

# finding terms and nonterms
terms, nonTerms = getTerms_NonTerms(grammar)[0], getTerms_NonTerms(grammar)[1]

first = findFirst(terms, nonTerms, grammar)
print(first)
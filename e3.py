def myLength(L):
    return len(L)

def myMaximum(L):
    return max(L)

def average(L):
    return sum(L)/len(L)

def buildPalindrome(L):
    #I haven't understood the purpose of the function
    pass

def remove(L1, L2):
    for a in L2:
        if a in L1:
            L1.remove(a)
    return L1

def flatten(L):
    if L == []:
        return L
    if isinstance(L[0], list):
        return flatten(L[0]) + flatten(L[1:])
    return L[0:1] + flatten(L[1:])

def oddsNevens(L):
    odds = list()
    evens = list()
    for a in L:
        if a%2:
            evens.append(a)
        else:
            odds.append(a)
    return odds, evens

def primeDivisors(n):
    primeDivisors = list()
    i = 2
    added = 0
    while i <= n:
        while n%i == 0:
            n //= i
            if not added:
                added = 1
                primeDivisors.append(i)

        i += 1
        added = 0
    return primeDivisors

def is_increasing(L):
    booleans = list()
    i = 0
    while i < len(L)-1:
        booleans.append((L[i]<L[i+1]))
        i += 1
    return booleans

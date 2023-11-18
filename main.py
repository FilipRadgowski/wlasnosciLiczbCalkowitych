from math import *
def sito(n):
    tab = []
    x = int(sqrt(n))
    for i in range(2,n+1):
        tab += [i]
    j = 0
    o = 2
    for i in range(2,x+1):
        while i*o <= n: 
            j = i*o
            if j in tab:
                tab.remove(j)
            o+=1
        j = 0
        o = 2

    return tab

def sito2(n):
    limit = n * (int(n* (log(n) + log(log(n)))))
    i = 0
    print("Zlozonosc obliczeniowa to: O(", limit,")")
    return sito(limit)[n-1]

x = input("Wprowadz liczbe naturalna: ")
print(sito2(int(x)))

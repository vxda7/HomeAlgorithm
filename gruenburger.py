def isPalindrom(word):
    lenword = len(word)
    for i in range(lenword//2):
        if word[i] != word[lenword - 1 - i]:
            return False
    return True

def makePalindrom(word):
    res = ""
    for i in reversed(word):
        res += i
    return res

def gruenburger(num):
    yes = False
    word = str(num)
    lenword = len(word)
    if lenword == 0:
        return "More than 2 length"
    while not yes:
        if isPalindrom(word):
            return word
        else:
            word = str(int(word) + int(makePalindrom(word)))
            print(word)
            lenword = len(word)

# a = int(input())
a = input()
# print(makePalindrom(a))
print(gruenburger(a))
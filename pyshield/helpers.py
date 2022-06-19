import random
import string


def randomNameGenerator(name,level):
    if level == 1:
        charList = list(name)
        return ''.join(random.choices(charList,k=8))
    
    elif level == 2:
        charList = string.ascii_letters
        return ''.join(random.choices(charList,k=16))
    
    else:
        charList = string.ascii_letters
        return ''.join(random.choices(charList,k=32))


def randomChineseChars():
    charList = []

    for _ in range(10):
        asciiNum = random.randint(19990,20500)
        charList.append(chr(asciiNum))

    return "".join(charList)


def chineseVars(num,j):
    varList = []

    for _ in range(num):
        var = randomChineseChars() + f"='{randomChineseChars()}'"
        varList.append(var)

    return j.join(varList)




funcRegex = r"(?<=def.)(.+)(?=\()"

classRegex = r"(?<=class.)(\w+)"

varRegex = r"(\w+\s?)(?=\=)"

varReplaceRegex = r"(?<=[^.])(\b{}\b)"

funcReplaceRegex = r"({}\s?)(?=\()"

classReplaceRegex = r"({})(?=.)"

 
 

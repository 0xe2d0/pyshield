from .helpers import *
import re
import base64


def variableRenamer(code,level):
    code = "\n" + code
    variables = re.findall(varRegex,code)
    for i in range(len(variables)):
        var = variables[i].strip("=").strip()
        randomName = randomNameGenerator(var,level)
        code = re.sub(varReplaceRegex.format(var),randomName,code)

    return code



def functionRenamer(code,level):
    funcs = re.findall(funcRegex,code)
    for i in range(len(funcs)):
        randomName = randomNameGenerator(funcs[i],level)

        code = re.sub(funcReplaceRegex.format(funcs[i]),randomName,code)

    return code

def classRenamer(code,level):
    classes = re.findall(classRegex,code)
    for i in range(len(classes)):
        randomName = randomNameGenerator(classes[i],level)
        code = re.sub(classReplaceRegex.format(classes[i]),randomName,code)

    return code



def addRandomChineseVars(code,level,j):
    code = chineseVars(level*10,j) + j  + code

    code = code + j  + chineseVars(level*10,j)

    return code


def b64Encode(code,level):
    encodedCode = base64.b64encode(code.encode())
    fullCode = f"exec(__import__('base64').b64decode({encodedCode}))"
    return fullCode


def main(code,level):
    methods = [variableRenamer, functionRenamer, classRenamer, b64Encode]
    if level == 1:
        for method in methods:
            code = method(code,level)
            
    elif level == 2:
        for method in methods:
            code = method(code,level)
        
        code = addRandomChineseVars(code,level,";")

    else:
        methods.remove(b64Encode)
        for method in methods:
            code = method(code,level)

        code = addRandomChineseVars(code,level,"\n")
        code = b64Encode(code,level)
        code = addRandomChineseVars(code,level,";")

    return code
    
    



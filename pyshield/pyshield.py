from pyshield.funcs import *
class PyShield:
    def __init__(self):
        pass

    @staticmethod
    def obfuscate(file,level):
        levels = [1,2,3]
        
        if level not in levels:
            print(2)
            return False


        try:
            code = open(file,'r',encoding="utf-8").read()

        except Exception as e:
            return e,False
            

        obfuscatedCode = main(code,level)
        
        return obfuscatedCode

            



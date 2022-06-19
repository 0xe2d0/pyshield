import pyshield
from rich import print as rprint
import argparse
from rich.progress import track

def obfuscate(arguments):
    filePath = arguments.file
    outputFile = arguments.output
    level = arguments.levels

    obfuscate = pyshield.PyShield.obfuscate(filePath,level=level)

    if obfuscate: 
        return obfuscate

    else:
        return False


def cli():
    parser = argparse.ArgumentParser(description="Best Python Code Obfuscater")
    parser.add_argument("-f","--file",help="File to be obfuscated .",required=True)
    parser.add_argument("-l","--levels",help="Obfuscate level. Range 1-3 .",required=True,default=1,type=int)
    parser.add_argument("-o","--output",help="File to save the code .",default=False)

    args = parser.parse_args()
    
    for n in track(range(100), description="Obfuscating..."):
        code = obfuscate(args)

    
    if code:
        rprint("[italic][green][+] Code Obfuscated !")
        if args.output:
            f = open(args.output,"w")
            f.write(code)
            f.close()
            rprint("[italic][green][+] Obfuscated Code Saved !")
        else:
            print(code)

    else:
        rprint("[italic][red][-] Error !")



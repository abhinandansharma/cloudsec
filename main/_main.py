from context import optparse
from . import encryptmain, decryptmain



def start():
    print("Initializing")
    args = optparse.parser()
    if(args.subparser_name == 'encrypt'):
        encryptmain.initialize(args)
    else:
        decryptmain.initialize(args)
   
    
           

    

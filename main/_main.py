from context import optparse
from . import encryptmain, decryptmain
import os



def start():
    args = optparse.parser()
    if(args.subparser_name == 'encrypt'):
        encryptmain.initialize(args)
    elif(args.subparser_name == 'decrypt'):
        decryptmain.initialize(args)
    elif(args.subparser_name == 'config'):
        os.system('rclone config')

   
    
           

    

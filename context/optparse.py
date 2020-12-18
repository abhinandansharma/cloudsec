import argparse

def parser():
    parser = argparse.ArgumentParser(description='CloudSec Encryption of files done by hybrid cryptography.')
    subparser = parser.add_subparsers(dest="subparser_name",help="Cloudsec Modes")
    parsera = subparser.add_parser('encrypt',help="Used in Encryption | cloudsec encrypt --help")
    parsera.add_argument('-f','--file',help="File Name")
    parsera.add_argument('-s','--segment',help="Segment of file between 2 to 4",default=3,type=int)
    parsera.add_argument('-r','--remote',help="Remote Name defined in configuration of cloud")
    parsera.add_argument('-l','--local',help="If locally encrypted and not uploaded to cloud",default=False,action="store_true")
    parserb = subparser.add_parser('decrypt',help="Used in Decryption | cloudsec decrypt --help")
    parserb.add_argument('-l','--local',help="If locally encrypted and not uploaded to cloud",default=False,action="store_true")
    parserb.add_argument('-d','--dfile',help="File Containing Key")
    parserb.add_argument('-r','--remote',help="Remote Name defined in configuration of cloud")
    args = parser.parse_args()
    return args

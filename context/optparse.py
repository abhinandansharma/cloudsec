import argparse

def parser():
    parser = argparse.ArgumentParser(description='CloudSec Options')
    parser.add_argument('-f','--file',help="File Name")
    parser.add_argument('-s','--segment',help="Segment of file between 2 to 4",default=3,type=int)
    parser.add_argument('-r','--remote',help="Remote Name defined in configuration of cloud")
    parser.add_argument('-l','--local',help="If locally encrypted and not uploaded to cloud",type=bool,default=False)
    args = parser.parse_args()
    return args

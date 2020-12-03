import argparse

def parser():
    parser = argparse.ArgumentParser(description='CloudSec Options')
    parser.add_argument('-f','--file',help="File Name")
    parser.add_argument('-s','--segment',help="Segment of file between 2 to 4",default=3,type=int)
    args = parser.parse_args()
    return args
from context import optparse
import os

def start():
    args = optparse.parser()
    if(args.segment < 2 or args.segment >4):
        print("Segment value out of range ",args.segment)
        return
    if(not os.path.isfile(args.file)):
        print("Not a file ",args.file)
        return
    print("Project Initialized")

import os
import subprocess
from context.common import dividefile
# from context.finalkey import finalkeygeneration

def initialize(args):
    if(args.segment < 2 or args.segment >4):
        print("Segment value out of range ",args.segment)
        return
    if(not os.path.isfile(args.file)):
        print("Not a file ",args.file)
        return
    remote = args.remote
    passed_file = args.file
    passed_segment = args.segment
    passed_pass = ""
    if(args.password):
        passed_pass = args.password
    local = args.local
    if(not remote and not local):
        print("Remote Name Necessary to upload")
    
    filetext = ""
    with open(passed_file,'r') as fp:
        filetext += fp.read()
    response = dividefile(filetext,passed_segment)
    if(response):
        print("File Dividing Success")
    else:
        print("Error Dividing File")
    if(not local and remote):
        os.system("rclone copy uploads "+remote+":test -v")
        output = subprocess.check_output("rclone ls "+remote+":test",shell=True)
        k = output.split(b'\n')
        outputlist = []
        for i in range(len(k)):
            real = str(k[i])
            templist = real.split(" ")
            outputlist.append(templist[len(templist)-1][0:-1])
        outputlist = outputlist[0:-1]
        filepresent = True
        for i in os.listdir("uploads"):
            if(i not in outputlist):
                filepresent = False
                break
        if(filepresent):
            print("File Tranferred to Cloud")
        else:
            print("Error Tranffering file to Cloud")
            print("Encrypted Files are present at Uploads")
        # finalkeygeneration(passed_pass)

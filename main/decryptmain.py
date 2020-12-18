import os
import subprocess
import json
from context.finalkey import keydecryption
from context.ende import decryptmains
from context.common import combinefile

def initialize(args):
    remote = args.remote
    decryptfile = args.dfile
    content = b""
    if(decryptfile and os.path.isfile(decryptfile)):
        with open(decryptfile,'rb') as fp:
            content = fp.read().split(b"\n")
    else:
        print("File Not Exist")
        return
    data = keydecryption(content[1],content[0])
    content = json.loads(data)
    filelist = []
    for i in content:
        filelist.append(i)
    output = subprocess.check_output("rclone ls "+remote+":test",shell=True)
    k = output.split(b'\n')
    outputlist = []
    for i in range(len(k)):
        real = str(k[i])
        templist = real.split(" ")
        outputlist.append(templist[len(templist)-1][0:-1])
    outputlist = outputlist[0:-1]
    filepresent = True
    for i in filelist:
        if(i not in outputlist):
            filepresent = False
            break
    if(not filepresent):
        print("File not Present on Cloud")
        return
    print("Files Found on Cloud")
    os.system('rm -rf uploads')
    os.mkdir('uploads')
    for i in filelist:
        os.system("rclone copy "+remote+":test/"+i+" uploads -v")
    decryptmains(content)
    print("File Decrypted")
    combinefile(content)
    print("Files Assembled Succesfull")
    print("Output File name is outputfile")

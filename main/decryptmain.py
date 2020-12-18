import os
import subprocess
import json
from context.finalkey import keydecryption
from context.ende import decryptmains
from context.common import combinefile
from context.color import col_error, col_warning, col_info, col_connect

def initialize(args):
    col_connect("Starting Decryption")
    remote = args.remote
    decryptfile = args.dfile
    content = b""
    if(decryptfile and os.path.isfile(decryptfile)):
        with open(decryptfile,'rb') as fp:
            content = fp.read().split(b"\n")
    else:
        col_error("File Not Exist")
        return
    data = keydecryption(content[1],content[0])
    content = json.loads(data)
    col_info("Key Decrypted")
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
        col_error("File not Present on Cloud")
        return
    col_info("Files Found on Cloud")
    os.system('rm -rf uploads')
    os.mkdir('uploads')
    for i in filelist:
        os.system("rclone copy "+remote+":test/"+i+" uploads -v")
    col_info("Files Downloaded")
    decryptmains(content)
    col_info("File Decrypted")
    combinefile(content)
    col_info("Files Assembled Succesfull")
    col_connect("Output File name is outputfile")

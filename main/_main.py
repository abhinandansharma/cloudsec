from context import optparse
from context.finalkey import finalkeygeneration
import os

def dividefile(content,size):
    file_size = len(content) // size
    os.system('rm -rf uploads')
    os.mkdir('uploads')
    try:
        for i in range(size):
            filename = "uploads/files"+str(i+1)
            with open(filename,'w') as fp:
                if(size == i+1):
                    fp.write(content[i*file_size:])
                else:
                    fp.write(content[i*file_size:(i+1)*file_size])
            print("File Path: ",filename)
        return True
    except Exception as e:
        print(e)
        return False
    
    

def start():
    print("Initializing")
    args = optparse.parser()
    if(args.segment < 2 or args.segment >4):
        print("Segment value out of range ",args.segment)
        return
    if(not os.path.isfile(args.file)):
        print("Not a file ",args.file)
        return
    remote = args.remote
    passed_file = args.file
    passed_segment = args.segment
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
        if(os.path.isdir("drive")):
            print("File Tranferred to Cloud")
            finalkeygeneration()
            os.rmdir("drive")
        else:
            print("Error Tranffering file to Cloud")
            print("Encrypted Files are present at Uploads")

    

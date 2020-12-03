from context import optparse
import os

def dividefile(content,size):
    file_size = len(content) // size
    os.system('rm -rf uploads')
    os.mkdir('uploads')
    try:
        for i in range(size):
            filename = "uploads/file"+str(i+1)
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
    passed_file = args.file
    passed_segment = args.segment
    filetext = ""
    with open(passed_file,'r') as fp:
        filetext += fp.read()
    response = dividefile(filetext,passed_segment)
    if(response):
        print("File Dividing Success")
    else:
        print("Error Dividing File")
    

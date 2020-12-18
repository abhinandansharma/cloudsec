import os
import uuid
from . import color

def dividefile(content,size):
    file_size = len(content) // size
    os.system('rm -rf uploads')
    os.mkdir('uploads')
    filelist = []
    try:
        for i in range(size):
            testname = str(uuid.uuid4())
            filename = "uploads/"+ testname
            filelist.append(testname)
            with open(filename,'w') as fp:
                if(size == i+1):
                    fp.write(content[i*file_size:])
                else:
                    fp.write(content[i*file_size:(i+1)*file_size])
            color.col_upload("File Path: ",filename)
        return filelist
    except Exception as e:
        print(e)
        return False

def combinefile(key):
    if(os.path.isfile('outputfile')):
        os.remove('outputfile')
    outputfile = 'outputfile'
    listfile = [""]*len(key)
    for i in key:
        listfile[key[i][1]] = i
    chunk = b""
    for i in listfile:
        data = b""
        with open('uploads/'+i,'rb') as file1:
            data = file1.read()
        chunk += data
    with open('outputfile','wb') as ab:
        ab.write(chunk)
    
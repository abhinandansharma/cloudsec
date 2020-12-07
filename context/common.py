import os
import uuid

def dividefile(content,size):
    file_size = len(content) // size
    os.system('rm -rf uploads')
    os.mkdir('uploads')
    try:
        for i in range(size):
            filename = "uploads/"+ str(uuid.uuid4())
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
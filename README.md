CloudSec Using hybrid computing
# Install Instruction
 
chmod +x script.sh

./script.sh

# To Activate Enviroment

. cloudsecenv/bin/activate

# To Deactivate
deactivate

# To Run Tool after activating enviroment

cloudsec --help

# Modes

cloudsec encrypt --help

cloudsec decrypt --help


## Encrypt Options

-h, --help&nbsp; &nbsp; &nbsp; show this help message and exit  
-f FILE, --file FILE  File Name  
-s SEGMENT, --segment SEGMENT  
 &nbsp; &nbsp; &nbsp;                        Segment of file between 2 to 4  
-r REMOTE, --remote REMOTE  
 &nbsp; &nbsp; &nbsp;                        Remote Name defined in configuration of cloud  
-l, --local           If locally encrypted and not uploaded to cloud  

## Decryption Options

  -h, --help&nbsp; &nbsp; &nbsp;             show this help message and exit  
  -l, --local&nbsp; &nbsp; &nbsp;            If locally encrypted and not uploaded to cloud  
  -d DFILE, --dfile DFILE  
   &nbsp; &nbsp; &nbsp;                      File Containing Key  
  -r REMOTE, --remote REMOTE  
   &nbsp; &nbsp; &nbsp;                      Remote Name defined in configuration of cloud  

## Example

cloudsec encrypt -f test -s 3 -r remote

cloudsec decrypt -d /root/secretkey -r remote

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

# Options

-s No of segment to be done of given file

-f file path to split and encrypt

## Example

cloudsec -f text.txt -s 3

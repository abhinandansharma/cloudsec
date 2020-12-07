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

-s No of segment to be done of given file

-f file path to split and encrypt

-p Password used for final key generation and decryption

-l If stored only locally not to cloud

-r Remote Name

## Decryption Options

-p Password for decryption

-l if files present locally

-et Encoded text or final key

## Example

cloudsec encrypt -f test -s 3 -r remote -p random_pass

cloudsec decrypt -p random_pass -et your_encoded_text

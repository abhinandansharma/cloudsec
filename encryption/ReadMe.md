# How to use encryption.

## There is a function saved in aes256.sh script file.
- It will aes256 encrypt a file, and then base64 encode it. When doing the reverse, it will base64 decode, decrypt, and then spit out the original plaintext.
- To use it follow steps below:
1) Copy that function and paste it on the terminal.
2) Run it. i.e press enter.
3) Now you can use this function to encrypt and decrypt files.

## Usage:
- echo "my string" | aes256
#### enter aes-256-cbc encryption password
`Returns: U2FsdGVkX1++e/BhBGlNOzNvarqq7zI13S/hbiKVzXQ=`

- echo "U2FsdGVkX1++e/BhBGlNOzNvarqq7zI13S/hbiKVzXQ=" | aes256 -d
#### enter aes-256-cbc decryption password
`Returns: my string`

- aes256 file.plain > file.crypt
#### enter aes-256-cbc encryption password

- aes256 -d file.crypt
#### enter aes-256-cbc decryption password
`Spits out original unencrypted file.`

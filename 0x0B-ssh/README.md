## SSH - Key based authentication

**SSH** Secure Shell is a cryptographic network protocol for operating network services securely over an unsecured network. Usually people use password based authentication when logging into remote server. But there is another way called **key-based** authentication.

With key based authentication, these are steps you can go through to configure this authentication method:

1. create public and private key. To create these keys type this command in your terminal:

` $ ssh-keygen -t <method> -b <length> `

This command generates those keys, the **-t** option specifies the type of key(example: rsa, dsa) while **-b** option specifies the length of the key (default: 3072)

when this command execute two files are created **id_rsa** and **id_rsa.pub** and are in this directory **~/.ssh/** .
**id_rsa** contains the private key and **id_rsa.pub** contains the public key. With this method of authentication, the private key is kept on local computer and the private key is uploaded on the remote server

2. upload the the public key on the remote computer:

   To upload this key stored in ~/ssh/id_rsa.pub to our remote computer(as uploaded.pub) we can type this command in terminal:
   ` $ scp id_rsa.pub <username>@<ip-address>:/.ssh/uploaded.pub `

3. copy the key (on remote computer) in uploaded.pub and paste it in new file called **authorized_keys**:

   ` $ cat ~/.ssh/uploaded.pub >> authorized_keys `

4. make sure the **~/ssh/** directory has permission of **700** and all files in that folder has permission of **600**

   ` $ chmod 700 ~/ssh/ `

   ` $ chmod 600 ~/ssh/* `

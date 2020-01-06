from cryptography.fernet import Fernet
import os

def decryptage():

    ''' Lire la cle de decryptage AES 128 bit '''

    with open('keyfile', 'rb') as key:
        read_key = key.read()
        key.close()

    ''' Cree une instance de cryptage'''

    crypt = Fernet(read_key)

    ''' Chemin de decryptage '''

    dest = '/Users/mac/Documents/projets/Scripts/python-ransomware/test'

    ''' Parcourir les fichiers dans le dossier de reception'''

    for root, dirs, files in os.walk(dest):

        for path in files:
            full_path = os.path.join(root,path)

            '''Remettre le nom initial et formatter le chemin absolu '''

            name_file = os.path.basename(path).strip('(crypted)')
            decrypt_name_file = os.path.join(root, name_file)

            '''ouverture du fichier en mode lecture enfin de recuperer son contenu crypter '''

            with open(full_path,'rb+') as f:
                _data = f.read()

                ''' Decrypter le contenu du fichier '''

                data = crypt.decrypt(_data)

                with open(decrypt_name_file,'wb') as decrypt_file:
                    decrypt_file.seek(0)
                    decrypt_file.write(data)
                    decrypt_file.close()
                f.seek(0)
                f.close()
            os.remove(full_path)




decryptage()
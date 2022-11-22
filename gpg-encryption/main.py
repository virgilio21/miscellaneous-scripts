from gpg import decrypt
from gpg import encrypt

if __name__ == '__main__':
    
    filename_to_encrypt = 'test.csv'
    filename_encrypted = 'test.csv.gpg'
    filename_decrypted = 'test_decrypt.csv'
    filename_public_key = 'public_key.pgp'
    recipients = 'your@gmail.com'
    password = 'super_secret_pass_to_decrypt'

    encrypt(filename_public_key, filename_to_encrypt, filename_encrypted, recipients)

    decrypt(filename_encrypted, filename_decrypted, password)

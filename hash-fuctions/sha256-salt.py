import uuid
import hashlib


def hash_text(text, salt=''):

    print(salt)
    return hashlib.sha256(salt.encode() + text.encode()).hexdigest()


if __name__ == '__main__':

    salt = 'super_secret'
    text = 'gatitos'

    sha256_text = hash_text(text, salt)
    print(sha256_text)
    print(len(sha256_text))

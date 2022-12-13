import hashlib


def hash_text(text, salt=''):

    return hashlib.sha256(salt.encode() + text.encode()).hexdigest()


if __name__ == '__main__':

    salt = '$2b$12$WaKsRhoClB7lGsrxN1j7fO'
    text = 'gatitos'

    sha256_text = hash_text(text, salt)

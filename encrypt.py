import hashlib

class Encryption():

    def encrypt_md5(self,passwords):
        result = [hashlib.md5(item.encode('utf-8')).hex_digest for item in passwords]
        return result
        

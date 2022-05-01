import requests
import hashlib
import threading
import time


class Brute():

    def __init__(self,host,url,pass_file,user_file='',user_known=''):
        self.target = host + url
        self.passwords_list = [line.strip() for line in open(pass_file,'r')]
        self.users_list = [line.strip() for line in open(user_file,'r')] if user_file else None
        self.username = user_known

    def brutalize(method="POST",password_encryption=None, username_encryption=None,username_parame="username",password_param="password")
        if method == "POST":
            if not users_list:
                
                    
            
            

        
        
        
    def encrypt_md5(self):


  


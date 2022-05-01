import requests
import hashlib
import threading
import time



class Brute():

    #TODO:Implement option for username lists
    def __init__(self,host,port,url,passwords_file,pass_enc_type,user_name,wrong_pass_response_status_code = '200'):
        self.target = host + port + ":" + url 
        try:
            self.passwords_list = [line.strip() for line in open(passwords_file,'r')]
        except Exception:
            print("passwords file not found!")
        self.username = user_name
        
        self.password_encryption_type = pass_enc_type if pass_enc_type else False
        self.wrong_pass_response_status_code = wrong_pass_response_status_code

    # def brutalize(method="POST"):
    #     if method == "POST":
    #         if self.password_encryption_type:

            
                
        
    


  


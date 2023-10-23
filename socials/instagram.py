from socialmedia import SocialMedia
import requests
from bs4 import BeautifulSoup
import re

class Instagram(SocialMedia):
    def __init__(self):
        super().__init__(platform_url="https://www.instagram.com",platform_name="Instagram")
        
        
    def get_followers(self,username:str):
        escaped_username=re.escape(username)
        regex = fr"\b{escaped_username}\b"
        user_profile_url=f'{self.get_platform_url()}/{username}'
        user_profile=requests.get(user_profile_url)
        parser=BeautifulSoup(user_profile.text,'html.parser')
        check = re.findall(regex,user_profile.text)
        if check.count(username) == 1:
            print("Incorrect Username")
        else:
            print("passed")
            
            
       
        
a=Instagram()
a.get_followers("harrysharma02")
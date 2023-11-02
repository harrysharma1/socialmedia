from socialmedia import SocialMedia
import requests
from PIL import Image


class Instagram(SocialMedia):
    def __init__(self):
        super().__init__(platform_url='https://www.instagram.com',platform_name='Instagram')
        
        
        
    def get_followers(self,username:str):
        url = f'{self.platform_url}/{username}/?__a=1&__d=1'
        response = requests.get(url)
        if response.ok:
            response = response.json()
            print(response['graphql']['user']['edge_followed_by']['count'])
        else:
            self.http_error(response.status_code)
    
    def get_following(self,username:str):
        url = f'{self.platform_url}/{username}/?__a=1&__d=1'
        response = requests.get(url)
        if response.ok:
            response = response.json()
            print(response['graphql']['user']['edge_follow']['count'])    
        else:
            self.http_error(response.status_code)
            
    def show_profile_pic(self,username:str):
        url = f'{self.platform_url}/{username}/?__a=1&__d=1'
        response = requests.get(url)
        if response.ok and username!='':
            response = response.json()
            profile_pic = response['graphql']['user']['profile_pic_url_hd']
            print(profile_pic)
            img = Image.open(requests.get(profile_pic,stream=True).raw)
            img.show()        
        else:
            self.http_error(response.status_code)      
    
        

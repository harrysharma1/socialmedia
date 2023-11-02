from socialmedia import SocialMedia
import requests

class Instagram(SocialMedia):
    def __init__(self):
        super().__init__(platform_url='https://www.instagram.com',platform_name='Instagram')
        
        
        
    def get_followers(self,username:str):
        url = f'{self.platform_url}/{username}/>?__a=1&__d=1'
        response = requests.get(url)
        if response.ok:
            response = response.json()
            return response['graphql']['user']['edge_followed_by']['count']
 
        
    def get_profile_pic(self,username:str):
        url = f'{self.platform_url}/{username}/?__a=1&__d=1'
        response = requests.get(url)
        if response.ok:
            response = response.json()
            print(response['graphql']['user']['profile_pic_url_hd'])        
               
      

from socialmedia import SocialMedia
import instaloader

class Instagram(SocialMedia):
    def __init__(self):
        super().__init__(platform_url="https://www.instagram.com",platform_name="Instagram")
        
        
        
    def get_followers(self,username:str):
        insta = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(insta.context,username=username)
        return profile.followers
    
  
                    
  

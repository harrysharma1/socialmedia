class SocialMedia():
    def __init__(self,platform_url,platform_name,username):
        self.platform_url=platform_url
        self.platform_name=platform_name
        username=username
        
    def get_platform_url(self):
        return self.platform_url
    
    def get_platform_name(self):
        return self.platform_name
    
    def get_username(self):
        return self.username

class SocialMedia():
    def __init__(self,platform_url,platform_name):
        self.platform_url=platform_url
        self.platform_name=platform_name
        
    def get_platform_url(self):
        return self.platform_url
    
    def get_platform_name(self):
        return self.platform_name
    
    def http_error(self, response_status_code):
        match response_status_code:
            case 404:
                print("Page not found")
            case _:
                print("Undefined HTTP error")

   
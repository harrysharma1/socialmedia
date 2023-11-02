import pytest
from ..scraper.instagram import Instagram

class TestInstagram:
    
    def test_get_follower_count(instagram):
        instagram = Instagram()
        assert instagram.get_follower_count('') == 'Undefined HTTP error'
        
        

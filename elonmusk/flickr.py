from typing import List
import flickrapi
import os
from dotenv import load_dotenv

# Authentication
root_path = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(root_path, '..', '.env')
load_dotenv(env_path)

api_key = os.environ['FLICKR_API_PUBLIC_KEY']
api_key_secret = os.environ['FLICKR_API_SECRET_KEY']

f = flickrapi.FlickrAPI(api_key=api_key, secret=api_key_secret)


def get_random_photo(tags=List[str], tag_mode='all'):
    # get random number between 1 and 20
    random_number = 2
    for photo in f.walk(tag_mode=tag_mode, tags=';'.join(tags), extras='url_o'):
        if random_number == 1:
            return photo.get('url_o')
        else:
            random_number -= 1

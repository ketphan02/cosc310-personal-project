from typing import List
import flickrapi
import os
from dotenv import load_dotenv

root_path = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(root_path, '..', '.env')
load_dotenv(env_path)

f = flickrapi.FlickrAPI(
    api_key=os.environ['FLICKR_API_PUBLIC_KEY'],
    secret=os.environ['FLICKR_API_SECRET_KEY'],
)


def get_random_photo(tags = List[str]):
  # get random number between 1 and 20
  random_number = 3
  for photo in f.walk(tag_mode='all',
                      tags=';'.join(tags),
                      extras='url_o'):
      if random_number == 1:
          print(photo.get('url_o'))
          return photo.get('url_o')
      else:
          random_number -= 1
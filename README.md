# Elon Musk Bot ![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54) ![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?logo=telegram&logoColor=white) ![Dialogflow](https://img.shields.io/badge/Dialogflow-orange.svg?logo=dialogflow&logoColor=white)

<p align="center"> 
<img width="620" height="414" src="static/img/ElonMusk.png">
</p>

Elon Musk Bot is a chatbot inspired by the entrepreneur and billionaire Elon Musk. It can answer questions about Tesla, SpaceX, cryptocurrencies, and more - give it a try!

## Talking to the Bot

The bot is available at https://t.me/COSC310_ElonMusk_Dialogflow_bot

## Executing Tests

[Install Python](https://realpython.com/installing-python/) on your machine and ensure you have the dependencies installed with:

```
pip install -r requirements.txt
```

To execute the tests, run the following command at the root of the repository:

```
python -m unittest discover tests
```
## Code Structure

```
    .
    ├── elonmusk                        # Code for the Python back-end
    │   ├── main.py                     # Entrypoint for Cloud Function
    │   ├── intent_handlers.py          # Logic for each Intent (i.e. Topic) Elon can talk about
    │   ├── twitter.py                  # Authenticate Twitter API and use Twitter API as function
    │   ├── flickr.py                   # Authenticate Flickr API and use Flickr API as function
    │   └── webhook.py                  # Webhook for Diagflow instead of using Google Cloud Function
    ├── tests                           # Tests for the bot
    │   ├── data                        # Raw data from Dialogflow after Intent and Entity matching
    │   ├── mock_dialogflow_utils.py    # Utilities for writing tests
    │   ├── test_billionaire_tax.py     # Elon can talk about his tax contributions
    │   ├── test_crypto_advice.py       # Elon can offer crypto advice
    │   ├── test_dailyroutine.py        # Elon can offer insights into his daily routine
    │   ├── test_fight_putin.py         # Elon can talk about his current opinion on Russia and Putin's actions
    │   ├── test_neuralink_app.py       # Elon can elaborate on some applications of the Link
    │   ├── test_spacex_work.py         # Elon can talk about job opportunities at SpaceX
    │   ├── test_stand_with_ukraine.py  # Elon can offer his opinion on the current situation in Ukraine 
    │   ├── test_what_company.py        # Elon can answer about his companies
    │   ├── test_what_is_crypto.py      # Elon can answer questions related to crypto
    └── README.md                       # This file!
```

## New Feature in this Assignment
Integrated 2 APIs from the Assignment suggestion. Chosen APIs are:
1. **Twitter API** (use [`Tweepy`](https://www.tweepy.org/)): Crawl the latest Tweet of Elon Musk
2. **Flickr API** (use [`flickrapi`](https://stuvel.eu/software/flickrapi/)): Acquire the image with related tags and send to the conversation

### 1. Twitter API
Library use
```python
import tweepy
from tweepy import OAuthHandler
```
Authentication
```python
auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
api.verify_credentials()
```
API use
```python
api.user_timeline(screen_name='elonmusk')
```
### 2. Flickr API
Library use
```python
import flickrapi
```
Authentication
```python
f = flickrapi.FlickrAPI(api_key=api_key, secret=api_key_secret)
```
API use
```python
f.walk(tag_mode=tag_mode, tags=';'.join(tags), extras='url_o')
```
### Limitation
- For **Twitter API**, there is a long wait time between each API request, which make it hard to scale (solvable when purchasing the premium version of the API)
- For **Flickr API**, it's hard to control the given image since most images uploaded by the community.
## Built With

* [Python](https://www.python.org/) - Back End
* [Dialogflow](https://cloud.google.com/dialogflow/docs) - Natural Language Processing
* [Telegram](https://telegram.org/) - User Interface

## Previous work

- [Kiet Phan](https://github.com/ketphan02)
- [Ivan Carvalho](https://github.com/IvanIsCoding)
- [Lydia Lin](https://github.com/yuqi88)
- [Akshat Singal](https://github.com/aksingal-dev)
- [Paula Wong-Chung](https://github.com/KafkaNoNeko)

## Author
- [Kiet Phan](https://github.com/ketphan02)

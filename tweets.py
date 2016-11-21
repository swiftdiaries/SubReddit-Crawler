import tweepy
api_key = "NbH0F95crdYQMQKXVwjsZQy04"
api_secret = "SezwW4y5n4eWbpqXvd533Lqxi6yZbf9xto6TdgGyW2q9pm5R8y"
access_token_key = "230177047-Z4AMGUdIszkHdw7lnEW9oUcyv4a2UXnfhGtzdQlR"
access_token_secret = "tcML0unZWBL5R3Ny22jgy5ctaESsICoVBcec8z0CfYCh9"
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()
user = api.get_user('adhitadselvaraj')
tweet = api.get_status('776887082161610752')
print(tweet.text)

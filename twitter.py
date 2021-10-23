import tweepy
auth = tweepy.OAuthHandler("api key", "api secret key")
auth.set_access_token("consumer key", "consumer secret key")
api = tweepy.API(auth)
tweet = input("input: ")
api.update_status(status =(tweet))
print ("Done!")
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "367451421-uHFwpmINorzC9krB5NNXbByq2lnLjAfXweEULfe7"
access_token_secret = "0uBi2FTWEVyKaHvAzyNq5NuU3Z3OcAvD5eTy3vlezTHPN"
consumer_key = "B5bqvMF1YcvWSXkjQ1IM2JJFj"
consumer_secret = "nksLmNL0IVvKoK5OaBrWAr4UJhGD8o9nzvRvpHOQUaAE20RWqH"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['battletech'])

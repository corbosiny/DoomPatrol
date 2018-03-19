import tweepy
from textblob import TextBlob

defConsumerKey = 	"etBdGLiSfO5ZsTdrwDA5rEayE"
defConsumerSecret = "nbS2k8LknWooMVZkUJlNLIQT0FYkenoe94yZvQ0ZpYOG6tV9en"

defAccessToken = 	"842399854861144064-yWH1WWoejYUIk9JIOk6OmZn9IEOUmAs"
defAccessTokenSecret = "IZSkTqJDyaZM0Xw8PienFR2nvFvNwCcQq4ceFzOM3PZnT"



class TweetCollector():

    def __init__(self, consumerKey= defConsumerKey, consumerSecret= defConsumerSecret, accessToken= defAccessToken, accessTokenSecret= defAccessTokenSecret):
        self.auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        self.auth.set_access_token(accessToken, accessTokenSecret)
        self.api = tweepy.API(self.auth)        


    def getTweets(self, subject, city, numTweets= 100):
        geoCode = TweetCollector.getGeoCode(city)
        print(geoCode)
        tweets = self.api.search(subject, count=numTweets, show_user=False, rpp=numTweets, geocode= geoCode)
        return tweets


    def getCoordinates(tweets):
        coordinates = [tweet.coordinates for tweet in tweets]
        return coordinates


    def getGeoCode(city):
        return "{0},{1},{2}mi".format(city.longitude, city.latitude, city.radius)


    def getPolarityAnalysis(tweets):
        sentiments = []
        for tweet in tweets:
            sentiments.append(TextBlob(tweet.text).sentiment.polarity)
        return sentiments

    
    def getSubjectivityAnalysis(tweets):
        subjectivities = []
        for tweet in tweets:
            subjectivities.append(TextBlob(tweet.text).sentiment.subjectivity)
        return subjectivities


    def getAveragePolarity(tweets):
        polarities = [TextBlob(tweet.text).sentiment.polarity for tweet in tweets]
        try:
            return sum(polarities) / len(polarities)
        except:
            return 0

    def getAverageSubjectivity(tweets):
        subjectivities = [TextBlob(tweet.text).sentiment.subjectivity for tweet in tweets]
        try:
            return sum(subjectivities) / len(subjectivities)
        except:
            return 0

if __name__ == "__main__":
    subject = str(input("Enter a topic to search about: "))
    num = int(input("How many tweets would you like to collect: "))

    bot = TweetCollector()
    
    tweets = bot.getTweets(subject, num)

    for tweet in tweets:
        try:
            print(tweet.text, end= "\n\n\n")
        except:
            pass
            
    sentiments = TweetCollector.getPolarityAnalysis(tweets)
    print("sentiment length", len(sentiments))

    subjects = TweetCollector.getSubjectivityAnalysis(tweets)
    print("subject length", len(subjects))

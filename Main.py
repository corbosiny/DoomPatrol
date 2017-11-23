from twitterBot import TweetCollector
from visualBar import graphCityStats
from City import City


class DisasterAnalyzer():

    def __init__(self, cityArray, tweetBot):
        self.tweetBot = tweetBot
        self.cityArray = cityArray

    def displayCrisisLocations(self):
        self.cityArray = self.analyzeCrisisLocations(self.cityArray)
        graphCityStats(self.cityArray)
        

    def analyzeCrisisLocations(self, cityArray):
        tweetsPerCity = self.collectTweets(cityArray)

        print(len(tweetsPerCity))
        for tweets in tweetsPerCity:
            print(tweets)
                
        crisisScores = DisasterAnalyzer.generateCrisisScores(tweetsPerCity)
        for score in crisisScores:
            print(score)
            
        cityArray = DisasterAnalyzer.assignCrisisScores(cityArray, crisisScores)

        return cityArray
        

    def collectTweets(self, cityArray):
        tweetsPerCity = [self.tweetBot.getTweets("help", city) for city in cityArray]
        return tweetsPerCity


    def generateCrisisScores(tweetsPerCity):
        crisisScores = [[TweetCollector.getAveragePolarity(setOfTweets), TweetCollector.getAverageSubjectivity(setOfTweets)] for setOfTweets in tweetsPerCity]
        return crisisScores

    def assignCrisisScores(cityArray, crisisScores):
        for i in range(len(cityArray)):
            cityArray[i].assignCrisisScores(crisisScores[i][0], crisisScores[i][1])
        return cityArray

def enterCitys(searchCount):
    searchArray = []
    for i in range (0, searchCount):
        longitude = float(input("Enter a longitude to search: "))
        latitude = float(input("Enter a latitude to search: "))
        radius = float(input("Enter a search radius: "))
        name = input("Enter the name of the city: ")
        searchArray.append(City(longitude, latitude, radius, name))

    return searchArray



if __name__ == "__main__":
    searchCount = int(input("Enter how many searches you want to do: "))
    cityArray = enterCitys(searchCount)
    tweetBot = TweetCollector()

    analyzer = DisasterAnalyzer(cityArray, tweetBot)
    analyzer.displayCrisisLocations()

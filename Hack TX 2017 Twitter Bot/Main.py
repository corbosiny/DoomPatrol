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
                
        crisisScores = DisasterAnalyzer.generateCrisisScores(tweetsPerCity)

        for tweets in tweetsPerCity:
            print(len(tweets))
            
        for score in crisisScores:
            print(score)
            
        cityArray = DisasterAnalyzer.assignCrisisScores(cityArray, crisisScores)

        return cityArray
        

    def collectTweets(self, cityArray):
        tweetsPerCity = [self.tweetBot.getTweets("trump", city) for city in cityArray]
        return tweetsPerCity


    def generateCrisisScores(tweetsPerCity):
        crisisScores = []
        for setOfTweets in tweetsPerCity:
            averagePolarity = TweetCollector.getAveragePolarity(setOfTweets)
            averageSubjectivity = TweetCollector.getAverageSubjectivity(setOfTweets)
            crisisScores.append([averagePolarity, averageSubjectivity])
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

def parseCitys(fileName = "citys.txt"):
    searchArray = []
    with open(fileName, "r") as cityFile:
        rows = cityFile.readlines()
        rows = [row.strip() for row in rows]
        for row in rows:
            cityParameters = row.split(",")
            longitude = cityParameters[0]
            latitude = cityParameters[1]
            radius = cityParameters[2]
            name = cityParameters[3]
            
            searchArray.append(City(longitude, latitude, radius, name))
                    
    return searchArray




if __name__ == "__main__":
    cityArray = parseCitys()
    tweetBot = TweetCollector()

    analyzer = DisasterAnalyzer(cityArray, tweetBot)
    analyzer.displayCrisisLocations()

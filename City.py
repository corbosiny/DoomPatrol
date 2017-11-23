class City:
    def __init__(self, longitude= 30.275579, latitude= -97.743871, radius= 6, name= "austin"):
        self.longitude = longitude
        self.latitude = latitude
        self.radius = radius
        self.name = name

    def assignCrisisScores(self, polarity, subjectivity):
        self.polarity = polarity
        self.subjectivity = subjectivity

import numpy
import pandas
from sklearn import tree


def parseOutAnswers(dataFrame):
    answers = {}

    for passengerIndex, passenger in dataFrame.iterrows():
        passengerID = passenger['PassengerId']
        answers[passengerID] = passenger['Survived']
    
    return answers

def customHeuristic(dataFrame):

    predictions = {}

    for passengerIndex, passenger in dataFrame.iterrows():
        passengerID = passenger['PassengerId']
        
        if passenger['Sex'] == 'female' or (passenger['Age'] < 14):
            predictions[passengerID] = 1
        else:
            predictions[passengerID] = 0
            
    return predictions

def scoreClassifier(answerDict, predictionDict):
    score = 0
    for key in answerDict.keys():
        if answerDict[key] == predictionDict[key]:
            score += 1

    return float(score) / len(answerDict)

if __name__ == "__main__":
    trainDataFrame = pandas.read_csv("train.csv")
    answers = parseOutAnswers(trainDataFrame)
    
    predictions = customHeuristic(trainDataFrame)

    print("Score: ", scoreClassifier(answers, predictions))
    

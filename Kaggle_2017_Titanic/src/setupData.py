import os
import pandas as pd
import matplotlib
from sklearn.preprocessing import LabelEncoder


#be sure to fix your own path for DATA_PATH
DATA_PATH = "C:/Programming/DoomPatrol/Kaggle_2017_Titanic/"
def load_train_data(data_path = DATA_PATH):
    csv_path = os.path.join(data_path, "train.csv")
    return pd.read_csv(csv_path)

def parseOutAnswers(dataFrame):
    answers = {}

    for passengerIndex, passenger in dataFrame.iterrows():
        passengerID = passenger['PassengerId']
        answers[passengerID] = passenger['Survived']

    return answers


###########################################################
# 1.) Encode the sex data as 0 for female or 1 for male.
# 2.) Pull the survived column as answers
# 3.) Label the columns to drop and drop them
# 4.) Fill in NaN entries in Age column with median
###########################################################

def cleanData(df):
    encoder = LabelEncoder()
    df.["Sex Code"] = encoder.fit_transform(df["Sex"])    
    columns = ['PassengerId', 'Survived', 'Name', 'Sex', 'Ticket', 'Cabin','Embarked', 'SibSp']
    df.drop(columns, axis=1, inplace=True)
    median = df['Age'].median()
    df['Age'].fillna(median, inplace=True)
    
    return df




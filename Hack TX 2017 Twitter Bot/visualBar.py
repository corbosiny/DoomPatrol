import matplotlib.pyplot as plt
from City import City


def graphCityStats(cityArray):
    names = [city.name for city in cityArray]
    polar = [city.polarity for city in cityArray]
    subject = [city.subjectivity for city in cityArray]
    ax = plt.subplot(111)
    index = range(len(names))
    x1 = [index - .1 for index in index]
    x2 = [index + .1 for index in index]
    polarity = ax.bar(x1, subject, width=.2, color='r', align='center')
    subjectivity = ax.bar(x2, polar, width=.2,color='g', align='center')
    plt.xlabel('Cities')
    plt.ylabel('Urgency Score')
    plt.xticks(index, names, rotation=45)
    plt.title('Assistance Urgency')
    plt.legend([polarity, subjectivity], ['Crisis Level', 'Info. Reliability'])
    plt.subplots_adjust(bottom=.25)
    plt.show()

if __name__ == "__main__":
    polar = [5,3,9,10,25,3,7,12]
    subject = [2,5,4,4,7,10,18,1]
    name = ['Amarillo', 'Austin', 'Dallas', 'El Paso', 'Houston', 'San Antonio', 'Shit Stain', 'Waco']
    graphCityStats(cityArray)

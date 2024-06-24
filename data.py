import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def market2022(): # Function which stores the algorithm
    market2022 = pd.read_csv("Data\VR-worldwide-market-share-2022.csv") # reading the data in the csv file
    graph = sns.barplot(data = market2022, x = "Industry", y = "Market Share (%)") # creating a barplot and storing it in a variable called "graph"
    plt.title("Forecast distribution of the augmented and mixed reality market worldwide in 2022") # plotting the title
    for container in graph.containers: # for each bar in the bar graph
        graph.bar_label(container) # adds the value to the top of each bar
    plt.show() # displays graph


def market2020():
    market2020 = pd.read_csv("Data\VR-market-segments-2020-2025.csv")
    graph = sns.barplot(data = market2020, x = "Industry", y = "Market Share (Billions USD)", hue = "Year")
    plt.title("Forecast size of the augmented and virtual reality (VR/AR) market worldwide in 2020 and 2025, by segment (in billion U.S. dollars)")
    for container in graph.containers:
        graph.bar_label(container)
    plt.show()


def hospital2018():
    hospital2018 = pd.read_csv("Data\Hospital_2018_2025_predictions.csv")
    graph = sns.barplot(data = hospital2018, x = "Region", y = "Value (Billions USD)", hue = "Year")
    plt.title("Global Healthcare AR and VR Market in 2018 and 2025, by region (Billions USD)")
    for container in graph.containers:
        graph.bar_label(container)
    plt.show()


def publicUsage():
    Usage = pd.read_csv("Data\VR-public-usage.csv")
    graph = sns.barplot(data = Usage, x = "Category", y = "Public Usage (%)")
    plt.title("Ranking of purposes of use for virtual reality in Europe in 2015")
    for container in graph.containers:
        graph.bar_label(container)
    plt.show()

def numberDoctors():
    num = pd.read_csv("Data\\num_Doctors_2017.csv")
    graph = sns.barplot(data = num, x = "Country", y = "Value/1000HAB", order = num.sort_values("Value/1000HAB",ascending = False).Country)
    plt.title("The number of doctors per 1000 people (2017)")
    for container in graph.containers:
        graph.bar_label(container)
    plt.show()

def main():
    print("select graph")
    print("1 - market 2022")
    print("2 - market 2020")
    print("3 - hospital 2018")
    print("4 - public usage")
    print("5 - numberDoctors")
    num = int(input("Select: "))
    if num == 1:
        market2022()
    elif num == 2:
        market2020()
    elif num == 3:
        hospital2018()
    elif num == 4:
        publicUsage()
    elif num == 5:
        numberDoctors()
    else:
        print("1 - market 2022")


main()


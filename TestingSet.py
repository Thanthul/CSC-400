import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
# I dont think we really need this. but for redundancy's sake used to dictate specific Column Names
ColNames = ['Name', 'Platform', 'Year_of_Release', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Critic_Scores', 'Critic_Count', 'User_Score', 'User_Count', 'Developer', 'Rating']
data = pd.read_csv('GameSales2016.csv', names = ColNames, skiprows = 1)
# print(sales)
# There are 2 games without genres, I don’t know if we should add a 13th category unknown, just so that we aren’t losing anything in the dataset and prevent problems with the analysis.
#{Action = 0, Adventure = 1, Fighting = 2, Misc = 3, Platform = 4, Puzzle = 5, Racing = 6, Role-Playing = 7, Shooter = 8, Simulation = 9, Sports = 10, Strategy = 11}

#Num of Games in each genre, useful for train/test later
#Action = 3370, Adventure = 1303, Fighting = 849, Misc = 1750, Platform = 888
#Puzzle = 580, Racing = 1249, Role-Playing = 1500, Shooter = 1323
#Simulation = 874, Sports = 2348, Strategy = 683

#Calling Specific Columns
#CriticScores = data.Critic_Scores.tolist()
gSales = data.Global_Sales.tolist()
# print(GlobalSales)
#plt.scatter(CriticScores, GlobalSales, color = 'b') # good but confusing to look at
#plt.xlabel('Critic Scores')
#plt.ylabel('Global Sales')
#plt.show()
naSales = data.NA_Sales.tolist()
genre = data.Genre.tolist()
numAction = genre[:3370]
gSalesAction = gSales[:3370]
naSalesAction = naSales[:3370]
numAdventure = genre[3370:4673]
gSalesAdventure = gSales[3370:4673]
# numFighting = genre[4673:5522]
# gSalesFighting = gSales[4673:5522]
# numMisc = genre[5522:7272]
# gSalesMisc = gSales[5522:7272]
# numPlatform = genre[7272:8160]
# gSalesPlatform = gSales[7272:8160]
# numPuzzle = genre[8160:8740]
# gSalesPuzzle = gSales[8160:8740]
# numRacing = genre[8740:9989]
# gSalesRacing = gSales[8740:9989]
# numRole-Playing = genre[9989:11489]
# gSalesRole-Playing = gSales[9989:11489]
# numShooter = genre[11489:12812]
# gSalesShooter = gSales[11489:12812]
# numSimulation = genre[12812:13686]
# gSalesSimulation = gSales[12812:13686]
# numSports = genre[13686:16034]
# gSalesSports = gSales[13686:16034]
# numStrategy = genre[16034:16717]
# gSalesStrategy = gSales[16034:16717]
plt.hist2d(naSalesAction, gSalesAction)
plt.show()


#Do Note that in the excel file that critic scores with no values were given a "0"
#Excel File is added in the github page

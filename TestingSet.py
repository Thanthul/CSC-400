import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
# I dont think we really need this. but for redundancy's sake used to dictate specific Column Names
ColNames = ['Name', 'Platform', 'Year_of_Release', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Critic_Scores', 'Critic_Count', 'User_Score', 'User_Count', 'Developer', 'Rating']
data = pd.read_csv('GameSales2016.csv', names = ColNames, skiprows = 1)
# print(sales)
# There are 2 games without genres, I don’t know if we should add a 13th category unknown, just so that we aren’t losing anything in the dataset and prevent problems with the analysis.
#{Action = 0, Adventure = 1, Fighting = 2, Misc = 3, Platform = 4, Puzzle = 5, Racing = 6, Role-Playing = 7, Shooter = 8, Simulation = 9, Sports = 10, Strategy = 11}

#Calling Specific Columns
CriticScores = data.Critic_Scores.tolist()
GlobalSales = data.Global_Sales.tolist()
# print(GlobalSales)
plt.scatter(CriticScores, GlobalSales, color = 'b')
plt.xlabel('Critic Scores')
plt.ylabel('Global Sales')
plt.show()

#Do Note that in the excel file that critic scores with no values were given a "0"
#Excel File is added in the github page
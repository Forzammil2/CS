import csv
import re
import statistics
import matplotlib.pyplot as plt

#open the file to read
file = open("HighestHolywoodGrossingMovies.csv","r")

csvReader = csv.reader(file)

#setup lists
Title = []
WorldWideSalesInUSD = []
'''
MovieInfo = []
Year = []
Distributor = []
BudgetInUSD = []
DomesticOpeningInUSD = []
DomesticSalesInUSD = []
InternationalSalesInUSD = []
ReleaseDate = []
Genre = []
RunningTime = []
License = []
'''

#loop through file and add data to lists.
next(csvReader) #skips header row

#plot the graph
plt.bar(Title, WorldWideSalesInUSD)
plt.ylabel("Title")
plt.title("Movie title and ther world wide sales")
plt.xlabel("Amount")
plt.show()
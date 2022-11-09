# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:15:02 2022

@author: EbereInyiama
"""

"""Assignment 1
The data is the population of West African countries from 1991 to 2020
Data Source: World Development Indicators

Question 1 Line Plot
"""
# importing the modules

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#reading the file into a dataframe with a function

def WestAfricaPop():
    df_WestAfrica = pd.read_csv("WestAfricaPopulation.csv")
    return df_WestAfrica
    
Population = WestAfricaPop()
print()
print("The 16 countries of West Africa and their population from 1991 to 2020: \n", Population)
print()

"""plotting the population growth of 16 West African Countries over a span of 20 years, from 1991 to 2020"""

df_WestAfrica1 = WestAfricaPop()

plt.figure(figsize=(10,8))

plt.plot(df_WestAfrica1["Year"], df_WestAfrica1["Benin"], "k--", label="Benin")
plt.plot(df_WestAfrica1["Year"], df_WestAfrica1["Burkina Faso"], "r:", label="Burkina Faso")
plt.plot(df_WestAfrica1["Year"], df_WestAfrica1["Cote d'Ivoire"], "b--", label="Cote d'Ivoire")
plt.plot(df_WestAfrica1["Year"], df_WestAfrica1["Cabo Verde"], "g--", label="Cabo Verde")
plt.plot(df_WestAfrica1["Year"], df_WestAfrica1["Ghana"], color="orange", linestyle="dotted", label="Ghana")
plt.plot(df_WestAfrica1["Year"], df_WestAfrica1["Guinea"], color="green", linestyle="solid", label="Guinea")
plt.plot(df_WestAfrica1["Year"], df_WestAfrica1["Gambia, The"], "b-", label="Gambia, The")
plt.plot(df_WestAfrica1["Year"], df_WestAfrica1["Guinea-Bissau"], "r-.", label="Guinea-Bissau")
plt.plot(df_WestAfrica1["Year"], df_WestAfrica1["Liberia"], "k:", label="Liberia")
plt.plot(df_WestAfrica1["Year"], df_WestAfrica1["Mali"], color="cyan", linestyle="dotted", label="Mali")
plt.plot(df_WestAfrica1["Year"], df_WestAfrica1["Mauritania"], "m--", label="Mauritania")
plt.plot(df_WestAfrica1["Year"], df_WestAfrica1["Niger"], color="orange", linestyle="solid", label="Niger")
plt.plot(df_WestAfrica1["Year"], df_WestAfrica1["Nigeria"], "g-.", label="Nigeria")
plt.plot(df_WestAfrica1["Year"], df_WestAfrica1["Senegal"], "c-", label="Senegal")
plt.plot(df_WestAfrica1["Year"], df_WestAfrica1["Sierra Leone"], "m:", label="Sierra Leone")
plt.plot(df_WestAfrica1["Year"], df_WestAfrica1["Togo"], "b:", label="Togo")

# setting labels and the legend

plt.xlabel("Year")
plt.ylabel("Population")
plt.legend()

plt.show()
plt.savefig("lineplot.png")

"""Question 2: Bar Chart
Using Bar chart to express the population growth over 20 years"""

plt.figure(figsize=(10,8))

plt.subplot(4, 4, 1,)
plt.bar(Population["Year"], Population["Benin"], color="cyan", label="Benin")
plt.legend(loc="lower left")

plt.subplot(4, 4, 2)
plt.bar(Population["Year"], Population["Burkina Faso"], label="Burkina Faso")
plt.legend(loc="lower left")

plt.subplot(4, 4, 3)
plt.bar(Population["Year"], Population["Cote d'Ivoire"], color="magenta", label="Cote d'Ivoire")
plt.legend(loc="lower left")

plt.subplot(4, 4, 4)
plt.bar(Population["Year"], Population["Cabo Verde"], color="blue", label="Cabo Verde")
plt.legend(loc="lower left")

plt.subplot(4, 4, 5)
plt.bar(Population["Year"], Population["Ghana"], color="orange", label="Ghana")
plt.legend(loc="lower left")

plt.subplot(4, 4, 6)
plt.bar(Population["Year"], Population["Guinea"], color="red", label="Guinea")
plt.legend(loc="lower left")

plt.subplot(4, 4, 7)
plt.bar(Population["Year"], Population["Gambia, The"], color="green", label="Gambia, The")
plt.legend(loc="lower left")

plt.subplot(4, 4, 8)
plt.bar(Population["Year"], Population["Guinea-Bissau"], color="cyan", label="Guinea-Bissau")
plt.legend(loc="lower left")

plt.subplot(4, 4, 9)
plt.bar(Population["Year"], Population["Liberia"], color="red", label="Liberia")
plt.legend(loc="lower left")

plt.subplot(4, 4, 10)
plt.bar(Population["Year"], Population["Mali"], color="magenta", label="Mali")
plt.legend(loc="lower left")

plt.subplot(4, 4, 11)
plt.bar(Population["Year"], Population["Mauritania"], color="blue", label="Mauritania")
plt.legend(loc="lower left")

plt.subplot(4, 4, 12)
plt.bar(Population["Year"], Population["Niger"], label="Niger")
plt.legend(loc="lower left")

plt.subplot(4, 4, 13)
plt.bar(Population["Year"], Population["Nigeria"], color="green", label="Nigeria")
plt.legend(loc="lower left")

plt.subplot(4, 4, 14)
plt.bar(Population["Year"], Population["Senegal"], label="Senegal")
plt.legend(loc="lower left")

plt.subplot(4, 4, 15)
plt.bar(Population["Year"], Population["Sierra Leone"], color="purple", label="Sierra Leone")
plt.legend(loc="lower left")

plt.subplot(4, 4, 16)
plt.bar(Population["Year"], Population["Togo"], color="orange", label="Togo")
plt.legend(loc="lower left")

plt.xlabel("Year")
plt.subplots_adjust(hspace=0.8, wspace=0.8)
plt.savefig("subplots.png")
plt.show()

"""Question 2: Using Pie Chart to compare 2020 West African population
Selecting only year 2020 and comparing the population of each West African country for the year 2020"""


def WestAfricaPop2020():
    df_country_percentage = pd.read_csv("2020WestAfricaPopulation.csv")
    return df_country_percentage

Population2020 = WestAfricaPop2020()

print()
print("The populaton of West African countries in year 2020 is: \n", Population2020)
print()

"""adding two columns to show total population and percentage of each country population in the year 2020"""

df_country_percentage1 = WestAfricaPop2020()
df_country_percentage1["Total_Pop"] = df_country_percentage1["2020 Population"].sum()
df_country_percentage1["%Country"] = 100.0*df_country_percentage1["2020 Population"] / df_country_percentage1["Total_Pop"]

print()
print(df_country_percentage1)
print()

"""Using pie chart to visualize the percentage population of each West African Country in year 2020"""

CountryCode = np.array(df_country_percentage1["CountryCode"])
EachCountry = np.array(df_country_percentage1["%Country"])

plt.figure(figsize=(10,8))
plt.pie(EachCountry, labels=CountryCode)

plt.show()

"""Making use of explode on the pie chart"""

CountryCode = np.array(df_country_percentage1["CountryCode"])
EachCountry = np.array(df_country_percentage1["%Country"])

plt.figure(figsize=(10,8))
plt.pie(EachCountry, labels=CountryCode, explode=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])

plt.show()
plt.savefig("Pop_piechart.png")


# Hazel Gandhi
# 11/3/2024
# Homework 3, Part 2

#1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order
countries = ['India', 'Pakistan', 'USA', 'Canada', 'France', 'Germany', 'Sri Lanka']

#2) Using a for loop, print each element of the list
for country in countries:
    print(country)

#3) Sort the list permanently.
sorted_countries = sorted(countries)
print(sorted_countries)

#4) Display the first element of the list.
print("The first country is:", sorted_countries[0])

#5) Display the second-to-last element of the list.
print("The second to last country is:", sorted_countries[-2])

#6) Delete one of the countries from the list using its name.
sorted_countries.remove('Canada')

#7) Using a for loop, print each country's name in all caps.
for country in sorted_countries:
    print(country.upper())
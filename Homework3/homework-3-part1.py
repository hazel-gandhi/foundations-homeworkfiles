# Hazel Gandhi
# 11/1/2024
# Homework 3, Part 1

# SECTION 1.A: Lists

#1. Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
numbers = [22, 90, 0, -10, 3, 22, 48]

#2. Display the number of elements in the list.
print('The number of elements in this list are', len (numbers))

#3. Display the 4th element of this list.
print('The fourth element in this list is', (numbers[3]))

#4. Display the sum of the 2nd and 4th element of the list.
sum = (numbers[1] + numbers[3])
print('The sum of the second and fourth element is', sum)

#5. Display the 2nd-largest value in the list.
sorted_numbers = sorted(numbers)
print('The second largest number in this list is', sorted_numbers[-2])

#6. Display the last element of the original unsorted list
print('The last element of this list is', numbers[-1])

#7. Display the sum of all of the numbers divided by two.
for number in numbers:
    print('The sum of all numbers divided by 2 is', number/2)

#8. Print whether the median or the mean of the numbers is higher

mean = sum(numbers) / len(numbers)
median = numbers[3]
if mean > median:
    print('The mean is greater than the median')
else:
    print('The median is greater than the mean')

# SECTION 1.B: Dictionaries

#1. Oftentimes dictionaries are used to describe multiple aspects of a single object. Like, say, a movie. Define a dictionary called movie that works with the following code.
movie = {
    'title': 'American Honey',
    'year': 2016,
    'director': 'Andrea Arnold'
}
print('My favorite movie is', movie['title'], 'which was released in', movie['year'], 'and was directed by', movie['director'])

#2. On the lines after that, add keys to the movie dictionary for budget and revenue (you'll use code like movie['budget'] = 1000), and print out the difference between the two.

movie['budget'] = 3500000
movie['revenue'] = 1200000
difference = (movie['budget'] - movie['revenue'])
print('The difference between the budget and revenue is', difference)

#3. If the movie cost more to make than it made in theaters, print "That was a bad investment". If the film's revenue was more than five times the amount it cost to make, print "That was a great investment." Otherwise print "That was an okay investment."

if movie['budget'] > movie['revenue']:
    print('That was a bad investment')
else:
    print('This was a good investment')

#4. Sometimes dictionaries are used to describe the same aspects of many different objects. Make ONE dictionary that describes the population of the boroughs of NYC. Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. (Tip: keeping it all in either millions or thousands is a good idea)

population = {
    'Manhattan' : '1.6 million',
    'Brooklyn': '2.6 million',
    'Bronx': '1.4 million',
    'Queens': '2.3 million',
    'Staten Island': '0.47 million'
}

#5. Display the population of Brooklyn.
print ('The population of Brooklyn is', population['Brooklyn'])

#6. Display the combined population of all five boroughs.
total_population = sum(float(value.split()[0]) for value in population.values())
print('The total population of New York City is', total_population, 'million')

#7. Display what percent of NYC's population lives in Manhattan.
percent_manhattan = total_population/(population.value() [0] * 100)
print('The percent of NYC population living in Manhattan is', percent_manhattan)


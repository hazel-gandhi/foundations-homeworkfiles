##Cats file class 3
# 10/30/2024
print("Hello!!!!")

cats = ['Jack', 'Mulberry', 'Boxcar']
##print list
print(cats)
##how many cats are in the list?
print (len(cats))
##print the name of the first cat
print (cats[0])
##to print last cat, don't do cats[2], do cats [-1]:
print (cats[-1])

##print a list of cats, one below the other
for cat in cats:
    print (cat)

Boxcar = {
    'name': 'Boxcar',
    'age' : 4,
    'color': 'orange',
    'eyes': 0
}
##print Boxcar's color
print (Boxcar['color'])

##to understand what info is in the dictionary, print out the keys(left hand side of the dictionary)
print(Boxcar.keys())

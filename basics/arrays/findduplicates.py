# This program finds the duplicates within an array

data = [10, 21, 37, 9, 21, 5, 10, 28, 30, 10]
y = []
d = {}
xboithing = []
# Problem 1: Find what all numbers have duplicates
# Problem 2: Count the no. of ties each number is present in the array
for i in data:
    count = 0
    for ii in data:
        if ii == i:
            count += 1
        
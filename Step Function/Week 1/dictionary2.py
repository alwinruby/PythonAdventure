#Create a new dictionary called fruits using {}.
#Put these values in your fruits dictionary:
# {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

fruits ={
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
        }

print(fruits)


# Loop through each key in fruits. For each fruit i.e.(key) print out the key along with its price
for fruit,price in fruits.items():
    print(fruit, " : ",price)

print("\n")

#Let's determine how much money you would make if you sold 2 of all your fruits.
#Create a variable called total and set it to zero.
#Loop through the fruits dictionaries. For each key in fruits, multiply the price i.e. (value) by 2 and then add it to total
#Finally, outside your loop, print total

total = 0
for price in fruits.values():
    total = total + price*2
print("Total :", total)

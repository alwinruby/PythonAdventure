#Given the inventory
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
print(inventory)

#Add a key to inventory called 'pocket'.
#Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.

inventory.update({'pocket':['seashell', 'strange berry','lint']})
print(inventory)

print("\n")

# Use .sort() the items in the list stored under the 'backpack' key. (keep in mind that .sort() is a function associated with a list.

print("Before sort: ",inventory['backpack'])
inventory['backpack'].sort()
print("After sort: ",inventory['backpack'])

print("\n")


#Then .remove('dagger') from the list of items stored under the 'backpack' key.

print("Before remove: ",inventory['backpack'])
inventory['backpack'].remove('dagger')
print("After remove: ",inventory['backpack'])

print("\n")

# Add 50 to the number stored under the 'gold' key, this should result in the gold containing the value 550.

print("Before adding 50 to gold: ",inventory['gold'])

inventory['gold'] = inventory['gold'] + 50

print("After adding 50 to gold: ",inventory['gold'])

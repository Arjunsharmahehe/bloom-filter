import uuid
from bloomFilter import BloomFilter

# Reading the file with the usernames and updating the filter
file = open('usernames.txt', 'r')
usernames = file.readlines()
bf = BloomFilter(50000, 7)
for i in usernames:
    username = i.rstrip('\n')
    bf.insert(username)

file.close()


# Test the filter
print("The bloom filter has been loaded up")
while True:
    inp = input("Enter a username you wish to search (q to quit): ")
    if inp == 'q':
        break
    elif bf.lookup(inp):
        print("Username already exists")
    else:
        print("This is a new username")


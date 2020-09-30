songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[0])
print(songs[2])

print(songs [1:4] )
songs [2] = "Streets Ain't Safe"

print(songs)

songs.extend(["House Arrest Tingz","To My Lowest","Bank on It"])

print(songs)

del songs[0]

print(songs)

# for i in range(len(songs)):
#     print(songs[i])

for song in songs:
    print(song)


    # question 5 
    # one is printing the length and range within the list  while option 1 is printing out everything consist in the list. Over all the output is still the same..


#   Q6
animals = ["lion","shark","camel"]

print(animals)

animals.append("wolf")
print(animals)

print(animals[2])

del animals[0]

print(animals)

# for animal in animals:
#     print(animal)

for i in range(len(animals)):
    print(animals[i])
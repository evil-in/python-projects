#Program to count the number of characters

import pprint
print('Write a message')
message = input()

count= {} #dictionary used to store the character and no of counts

for character in message.lower():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

#for c, p in count.items():
    #print(c, ':', p)
    
pprint.pprint(count)

import math
bingo1 = input("Enter first name: ")
bingo2 = input("Enter second name: ")
bingo1 = bingo1.lower()
bingo2 = bingo2.lower()
name1 =[]
name1a= []
name2 = []
match = []

for let in bingo1:
        if let != ' ':
                name1.append(let)
                name1a.append(let)
for let2 in bingo2:
        if let2 != ' ':
                name2.append(let2)
#print(name1)
#print(name2)

for i in range(len(name1)):
                for j in range(len(name2)):
                        if name1[i] == name2[j]:
                                #print(name1[i])
                                match.append(name1[i])
                                name1a.remove(name1[i])
                                name2.remove(name1[i])
                                break

#print(name1a)
#print(name2)

#print(match)
                
score = len(name1a) + len(name2)            
#print(score)


flame = 'flames'

flames = []
for letter in flame:
        flames.append(letter)
#print(flames)

for i in range(5):
        result = flames
        for j in range(math.ceil(score/len(flames))):
                result = result + result
        #print(result)
        flames.remove(result[score-1])       
        flames = result[score:(score + 5 - i )]

#print(flames)

answer = flames[0]

if answer == 'f':
        print('FRIENDS')
elif answer == 'l':
        print('LOVERS')
elif answer == 'a':
        print('AFFECTION')
elif answer == 'm':
        print('MARRIAGE')
elif answer == 'e':
        print('ENEMIES')
elif answer == 'S':
        print('SEX')

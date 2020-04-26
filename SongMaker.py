# Music Generator, Beatles Music using First order markov
import random

wordDict = {}

#file stuff
file = open("rap_music.txt", "r")
newFile = open("newSong.txt", "w")

beatList = [] #list, we will iterate through it
count = 0 #count just gives each key a number value

#cleaning the file
punc = "!,.?:;()'[]{}~1234567890"
for line in file:
    for char in punc:
        line = line.replace(char, "")
    line = line.lower()
    lyrics = line.split()
    beatList += lyrics

    for word in lyrics:
        if word in wordDict:
            continue
        else:
            wordDict[word] = count
            count += 1
#print(wordDict)
#print(count)

biDict = {} #make the big dict of dicts

for w in wordDict: #for each unique word, we track the following words
    wDict = {} #the list of nextWords, with the count
    #nextList = [] # next word list
    prev = False
    for q in beatList: # q is str, key, current word
        if prev == True: # the last for loop found the word we wanted in this wDict as the key
            if q in wDict: #so we add q, the second word in the pair, to the dictionary. or add to the count.
                num = wDict[q]
                wDict[q] = num + 1
            else: #a new nextWord
                wDict[q] = 1

        if q == w: #checks if current q word can be the wDist word we want as key
            prev = True
        else:
            prev = False

    biDict[w] = wDict #adds wDict to biDict

#print(biDict)

#function that finds the probaility for the second word based on the first word (given)
def prob(firstWord):
    myDict = biDict[firstWord] #find the firstWord dictionary
    probList = []

    for sec in myDict:
        count = myDict[sec]
        while count > 0:
            probList.append(sec)
            count -= 1
    return random.choice(probList)



wordCount = 75 # number words in our song

prevWord = random.choice(beatList)
songStr = ""
while wordCount > 0:
    currentWord = prob(prevWord)
    songStr += currentWord + " "
    prevWord = currentWord
    wordCount -= 1

print(songStr)
#add tabs
newFile.write("Song Lyric Generation\nAngela Vaynshteyn\nKarolina Michalewska\nSabelle O'Connell\nWyatt Miller\n")
newFile.write(songStr)
#ADD to the FILE

file.close() #close
newFile.close()

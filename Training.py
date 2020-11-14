import re

from readFromFile import readFromFile


def Training():
    counter = {}

    line = readFromFile().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
    string = ''
    for j in counter:
        if counter[j] >= 10:
            temp = re.sub('(\W|[0-9])', '', j)
            if temp and len(temp) > 1:
                string = string + temp + '\n'

    actTraining = int(input('Какой язык в обычающей выборке?:\n'
                        '1 - Русский\n'
                        '2 - Английский\n'))
    if actTraining == 1:
        SaveTraining(string,1)
    elif actTraining == 2:
        SaveTraining(string,2)


def SaveTraining(string, type):
    if type == 1:
        file = open("Training/frequencyMethodRussian.txt", "w")
        file.write(str(string))
        file.close()
    elif type == 2:
        file = open("Training/frequencyMethodEnglish.txt", "w")
        file.write(str(string))
        file.close()
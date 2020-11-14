from langdetect import detect
from Training import Training
from saveInFile import SaveFile
from printDocuments import printExpectation
from readFromFile import readFromFile


def frequencyWordMethod():
    fileRus = open('Training/frequencyMethodRussian.txt')
    contentRus = fileRus.read()
    fileEng = open('Training/frequencyMethodEnglish.txt')
    contentEng = fileEng.read()
    file = readFromFile()
    numberOfRussianMatches = 0
    for word in contentRus:
        i = 0
        if word in file:
            i = i + 1
            numberOfRussianMatches = numberOfRussianMatches + i
    numberOfEnglishMatches = 0
    for word in contentEng:
        i = 0
        if word in file:
            i = i + 1
            numberOfEnglishMatches = numberOfEnglishMatches + i
    if numberOfEnglishMatches > numberOfRussianMatches:
        print('en')
    elif numberOfEnglishMatches < numberOfRussianMatches:
        print('ru')
    else:
        print('Не удалось распознать язык')
    printExpectation()


def shortWordMethod():
    print('В разработке')
    printExpectation()


def ownMethod():
    result = ('Результат идентификации текста: ', detect(str(readFromFile())))
    print(result)
    SaveFile(result,1)
    printExpectation()


from langdetect import detect
from printDocuments import printExpectation
from readFromFile import readFromFileEnglishText, readFromFileRussianText


def frequencyWordMethod():
    print('В разработке')
    printExpectation()


def shortWordMethod():
    print('В разработке')
    printExpectation()


def ownMethod():
    print('Результат идентификации текста: ', detect(str(readFromFileEnglishText())))
    print('Результат идентификации текста: ', detect(str(readFromFileRussianText())))
    printExpectation()
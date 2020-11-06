from langdetect import detect

from saveInFile import SaveFile
from printDocuments import printExpectation
from readFromFile import readFromFile


def frequencyWordMethod():
    print('В разработке')
    printExpectation()


def shortWordMethod():
    print('В разработке')
    printExpectation()


def ownMethod():
    result = ('Результат идентификации текста: ', detect(str(readFromFile())))
    SaveFile(result,1)
    printExpectation()


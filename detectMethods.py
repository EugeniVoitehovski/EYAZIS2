import pymorphy2
from langdetect import detect

from printDocuments import printExpectation
from readFromFile import readFromFile, re
from saveInFile import SaveFile


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


def load_words(filename):
    inFile = open(filename, 'r')
    words = inFile.readlines()
    counter = 0
    for word in words:
        words[counter] = re.sub('\n', '', word)
        counter = counter + 1
    return words


def shortWordMethod():
    # загрузка ПОЯ из файлов
    contentRus = load_words('Training/shortMethodRussian.txt')
    contentEng = load_words('Training/shortMethodEnglish.txt')
    # загрузка текста из анализируемого файла
    analyzing_file = readFromFile()
    # создание словарей
    engEntrances = {}
    ruEntrances = {}
    analyzer = pymorphy2.MorphAnalyzer()

    # инициализация словарей лексема -> кол-во вхождений
    for word in contentRus:
        ruEntrances[word] = 0
    for word in contentEng:
        engEntrances[word] = 0

    # подсчёт количества вхождений лексемы в тексте (учитываются все формы лексемы)
    # в подсчёте могут быть погрешности из-за того, что некоторые формы лексемы, найденные в pymorphy могут входить
    # список word_morph[0].lexeme дважды
    for word in contentRus:
        word_morph = analyzer.parse(word)
        lexemes = word_morph[0].lexeme
        for lexeme in lexemes:
            lexeme_word = lexeme.word
            matches = re.findall(lexeme_word, analyzing_file)
            ruEntrances[word] = ruEntrances[word] + len(matches)

    # аналогичный процесс для английских лексем
    for word in contentEng:
        word_morph = analyzer.parse(word)
        lexemes = word_morph[0].lexeme
        for lexeme in lexemes:
            lexeme_word = lexeme.word
            matches = re.findall(lexeme_word, analyzing_file)
            engEntrances[word] = engEntrances[word] + len(matches)
    # сумма всех вхождений русских лексем в тексте
    entrances_sum_ru = 0

    # сумма всех вхождений английских лексем в тексте
    entrances_sum_en = 0

    # подсчёт всех вхождений
    for lexeme, entrances in ruEntrances.items():
        entrances_sum_ru = entrances_sum_ru + entrances

    for lexeme, entrances in engEntrances.items():
        entrances_sum_en = entrances_sum_en + entrances

    # вычисление вероятностей появления для каждой лексемы
    if entrances_sum_ru != 0:
        for lexeme, entrances in ruEntrances.items():
            ruEntrances[lexeme] = entrances / entrances_sum_ru

    if entrances_sum_en != 0:
        for lexeme, entrances in engEntrances.items():
            engEntrances[lexeme] = entrances / entrances_sum_en

    ru_probability = 1.0
    eng_probability = 1.0

    # вычисление вероятности
    for entrances_amount in ruEntrances.values():
        if entrances_amount == 0:
            entrances_amount = 1
        ru_probability = ru_probability * entrances_amount
    for entrances_amount in engEntrances.values():
        if entrances_amount == 0:
            entrances_amount = 1
        eng_probability = eng_probability * entrances_amount

    print('Вероятность Русского языка: ' + str(ru_probability / 100))
    print('Вероятность Английского языка: ' + str(eng_probability / 100))
    # знаки инвертированы, т.к. в ходе вычисления вероятности языка происходит умножение дроби на дробь и результат
    # стремится к 0
    if eng_probability < ru_probability:
        print('en')
    elif eng_probability > ru_probability:
        print('ru')
    else:
        print('Не удалось распознать язык')
    printExpectation()
    printExpectation()


def ownMethod():
    result = ('Результат идентификации текста: ', detect(str(readFromFile())))
    print(result)
    SaveFile(result, 1)
    printExpectation()

from detectMethods import frequencyWordMethod, shortWordMethod, ownMethod
from printDocuments import printRusDocument, printEngDocument


def choose_method():
    method = int(input('Выберите метод из предложенных:\n'
                       '1 - Метод частотных слов\n'
                       '2 - Метод коротких слов\n'
                       '3 - Собственный метод\n'))
    if method == 1:
        print('Метод частотных слов')
        frequencyWordMethod()
    elif method == 2:
        print('Метод коротких слов')
        shortWordMethod()
    elif method == 3:
        print('Собственный метод')
        ownMethod()


def expectation():
     while True:
         act = int(input('Желаете продолжить:\n'
                           '1 - Да\n'
                           '2 - Нет\n'))
         if act == 1:
             choose_method()
         elif act == 2:
             print('До новых встреч!')
             break;



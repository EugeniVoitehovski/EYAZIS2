
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


def frequencyWordMethod():
    print('В разработке')

def shortWordMethod():
    print('В разработке')

def ownMethod():
    print('В разработке')

choose_method()
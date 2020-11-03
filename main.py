from langdetect import detect
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io


def readFromFileEnglishText():
    try:
        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        fp = open("texts/english.pdf", 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp,
                                      check_extractable=True):
            interpreter.process_page(page)
        text = retstr.getvalue()
        fp.close()
        device.close()
        retstr.close()
        # print(text)
        return text
    except IOError:
        print("No file")


def readFromFileRussianText():
    try:
        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        fp = open("texts/russian.pdf", 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in PDFPage.get_pages(fp,
                                      check_extractable=True):
            interpreter.process_page(page)
        text = retstr.getvalue()
        fp.close()
        device.close()
        retstr.close()
        #print(text)
        return text
    except IOError:
        print("No file")

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
    print(detect(str(readFromFileEnglishText())))
    print(detect(str(readFromFileRussianText())))


choose_method()


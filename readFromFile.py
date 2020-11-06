from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
from tkinter import filedialog
from tkinter import *

def LoadFile():
    root = Tk()
    root.withdraw()
    root.update()
    file = filedialog.askopenfilename()
    root.update()
    root.quit()
    return file


def readFromFile():
    try:
        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        fp = open(LoadFile(), 'rb')
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
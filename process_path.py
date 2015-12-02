from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

from os import listdir


class Process_Path():

    def __init__(self, path):
        self.process_files(path)



    def process_files(self):
        files=[f for f in listdir(self.path)]
        files_dic={}
        for file in files:
            #process the file based on the file extension
            file_ext=file.split('.')[-1]
            if file_ext=='txt':
                files_dic[file]=self.process_txt(self.path+file)
            elif file_ext=='pdf':
                files_dic[file]=self.process_pdf(self.path+file)
            elif file_ext=='html':
                files_dic[file]=self.process_html(self.path+file)

        return files_dic


    #process files of .txt format
    def process_txt(self, file_path):
        fl=open(file_path, 'r')
        text=fl.read()
        fl.close()
        return text



    def process_pdf(file_path='data\\pdf\\file.pdf'):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = file(file_path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
        fp.close()
        device.close()
        str = retstr.getvalue()
        retstr.close()
        return str

    def process_html(self, file_path):
        pass
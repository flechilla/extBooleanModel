from cStringIO import StringIO
from json import JSONEncoder, JSONDecoder
from os import listdir

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

from text_processor import TextProcessor


class PathProcessor:

    def __init__(self, path):
        self.path=path

    #foreach file in the path analize the extension and call
    #a method to extract the text depending on it..
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
        tp=TextProcessor()
        for file, text in files_dic.items():
            #call the text_processor module
            text_proc_result=tp.process(JSONEncoder().encode({'action':'process', 'data':text}))
            text_proc_result=JSONDecoder().decode(text_proc_result)['terms']
            files_dic[file]=text_proc_result
        return files_dic


    #process files of .txt format
    def process_txt(self, file_path):
        fl=open(file_path, 'r')
        text=fl.read()
        fl.close()
        return text


    #process the files of pdf extension.
    def process_pdf(self,file_path):
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


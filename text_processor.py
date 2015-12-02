
import re
from os import listdir, stat

from nltk.stem.lancaster import LancasterStemmer
from json import JSONDecoder, JSONEncoder

# TODO: enter dir with the docs
class Text_Processor:

    def __init__(self):
        self.terms=[]
        self.load_stopwords()


    def process(self, json):
        dec_json=JSONDecoder().decode(json)
        if dec_json['action']=='process':
            return self.lex_process(dec_json['data'])


    #load the stopwords (taken from nltk)
    def load_stopwords(self):
        self.stopwords=set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'])


    def lex_process(self, text):
        words=[]
        for line in text.splitlines():
            for w in line.split():
                words.append(w)
        return self.stemming(words)



    def remove_stopwords(self, words):
        return [w for w in words if w not in self.stopwords]



    def stemming(self, words):
        ps=LancasterStemmer()
        print [ps.stem(w) for w in words]
        return self.remove_stopwords([ps.stem(w) for w in words])


    def enc_json(self, terms):
        output=JSONEncoder.encode({'terms':terms})
        print output
        return output










    # def load_docs(self,docs_path="data\\docs"):
    #     docs=[doc for doc in listdir(docs_path)]
    #     self.docs_dics=[]
    #     for doc in docs:
    #         self.docs_dics.append(self.load(docs_path,doc))
    #     file=open('data\\logs.txt', 'w')
    #     file.write(str(self.docs_dics))
    #     file.close()
    #
    #
    # def load(self,docs_path,doc):
    #     word_counter={}
    #     tl=open(docs_path+'\\'+doc, 'r')
    #     line=tl.readline()
    #     while line:
    #         proc_line=self.process_text(line)
    #         self.word_counter(proc_line, word_counter)
    #         line=tl.readline()
    #     tl.close()
    #     return word_counter
    #
    # def word_counter(self, line, words_counter_dic):
    #     for word in line:
    #         if word in words_counter_dic.keys():
    #             words_counter_dic[word]+=1
    #         else:
    #             words_counter_dic[word]=1
    #
    # # start process_tweet
    # # **taken from internet
    # def process_text(self,text):
    #     # Convert to lower case
    #     text = text.lower()
    #     # Remove additional white spaces
    #     text = re.sub('[\s]+', ' ', text)
    #     # trim
    #     text = text.strip('\'"')
    #
    #     #delete not letter chars
    #     text=re.sub('[=|+|,|.|?|!|*|;|:|(|)|&|-|\|[|\]]','', text)
    #
    #     #delete consecutive chars with the same value
    #     pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    #     text=pattern.sub(r"\1",text)
    #
    #     return self.remove_stop_words(text)
    #
    # # end
    #
    #
    #
    # #remove the stopwords and set it to a dict
    # def remove_stop_words(self, text):
    #     text=text.split()
    #     output=[word for word in text if word not in STOP_WORDS and len(word)>2]
    #     return output

text="What doing this morning \n was something outing of going to \n ripping".encode()
print text
proc=Text_Processor().process('{"action":"process", "data":"What doing this morning was something outing of going to  ripping"}')
print proc


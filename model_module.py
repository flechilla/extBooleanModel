from json import JSONDecoder, JSONEncoder
from text_processor import TextProcessor
from os import listdir
from path_processor import PathProcessor
import pdb
from index_module import IndexModule

class ExtendedBoolean:
    def __init__(self, json):
        self.vocaulary=set([])
        json = JSONDecoder().decode(json)
        self.index_mod=IndexModule()
        
        if json['action'] == "build":
            self.build(json['path'])
        else:
            self.process_query(json['query'], json['count'])

    def build(self, path):
        pp = PathProcessor(path)
        self.terms = pp.process_files()
        self.calculate_tf()
        self.calculate_itf()
        self.index_mod.process_json(JSONEncoder().encode({'action': 'build', 'data':self.index}))


    def process_query(self, query, count):
        pass

    def calculate_tf(self):
        for file, terms in self.terms.items():
            words_counter_dic = {}
            max_frec=0
            for w in terms:
                self.vocaulary.add(w)
                if w in words_counter_dic.keys():
                    words_counter_dic[w] += 1
                    if words_counter_dic[w]>max_frec:
                        max_frec=words_counter_dic[w]
                else:
                    words_counter_dic[w] = 1
            for w in terms:
                words_counter_dic[w]/=float(max_frec)
            print 'max_frec', str(max_frec)
            self.terms[file] = words_counter_dic

    def calculate_itf(self):
        self.index=[]

        for w in self.vocaulary:
            files_with_words=[]
            for doc_name, doc_terms in self.terms.items():
                if w in doc_terms.keys():
                    files_with_words.append(doc_name)
            itf=len(self.terms)/float(len(files_with_words))
            self.index.append({'key':w, 'value':{'itf':itf, 'documents':[{'tf':self.terms[doc][w], 'document':doc} for doc in files_with_words]}})



eb = ExtendedBoolean('{"action":"build", "path":"data\\\\docs\\\\"}')
print eb.index_mod.process_json('{"action":"get", "key":"rol"}')





































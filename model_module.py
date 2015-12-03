from json import JSONDecoder, JSONEncoder
from text_processor import TextProcessor
from os import listdir
from path_processor import PathProcessor


class ExtendedBoolean:
    def __init__(self, json):
        json = JSONDecoder().decode(json)
        if json['action'] == "build":
            self.build(json['path'])
        else:
            self.process_query(json['query'], json['count'])

    def build(self, path):
        pp = PathProcessor(path)
        self.terms = pp.process_files()
        self.calculate_weights_tf()

    def process_query(self, query, count):
        pass

    def calculate_weights_tf(self):
        for file, terms in self.terms.items():
            words_counter_dic = {}
            max_frec=0
            for w in terms:
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


eb = ExtendedBoolean('{"action":"build", "path":"data\\\\docs\\\\"}')
print eb.terms

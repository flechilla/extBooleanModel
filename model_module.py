
from json import JSONDecoder, JSONEncoder
from text_processor import Text_Processor
from os import listdir

class Extended_Boolean:
    def __init__(self, json):
        json=JSONDecoder().decode(json)
        if json['action']=='build':
            self.build(json['path'])
        else:
            self.process_query(json['query'], json['count'])



    def build(self, path):
        pass





    def process_query(self, query, count):
        pass




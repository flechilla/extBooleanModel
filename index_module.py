from json import JSONDecoder, JSONEncoder


class IndexModule:
    def __init__(self):
        pass

    def process_json(self, json):
        json = JSONDecoder().decode(json)

        # check for the action
        if json['action'] == 'build':
            self.build_index(json)
        if json['action'] == 'get':
            return self.get_term(json['key'])

    def build_index(self, dic):
        self.index = {}
        for term in dic['data']:
            self.index[term['key']] = term['value']
        print self.index

    def get_term(self, term):
        return JSONEncoder().encode(self.index[term])

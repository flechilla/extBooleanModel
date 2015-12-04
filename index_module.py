from json import JSONDecoder, JSONEncoder


class IndexModule:
    def __init__(self):
        pass

    def process_json(self, json):
        json = JSONDecoder().decode(json)

        # check for the action
        if json['action'] == 'build':
            self.build_index(json)
        elif json['action'] == 'get':
            return self.get_term(json['key'])
        elif json['action'] == 'add' or json['action'] == 'update':
            self.add_term(json['key'], json['value'])
        elif json['action'] == 'delete':
            self.delete(json['key'])

    def build_index(self, dic):
        self.index = {}
        for term in dic['data']:
            self.index[term['key']] = term['value']
        print self.index

    def get_term(self, term):
        return JSONEncoder().encode(self.index[term])

    def add_term(self, key, value):
        self.index[key] = value

    def delete(self, key):
        self.index.pop(key)

from src.data import data as dt
from re import sub

class Types:

    def __init__(self):
        data = dt()
        self.data = data.content()


    def allTypes(self):
        types_counter = {}

        for file_line in self.data:
            #line = sub('\n','',line).lower().replace(' ', '')
            file_line = sub('\n', '', file_line).lower().replace(' ', '')
            for letter in file_line:
                if letter in types_counter:
                    types_counter[letter] += 1
                    continue
                types_counter[letter] = 1



        return types_counter
                

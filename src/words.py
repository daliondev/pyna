from src.data import data as dt
from re import sub

class Types:

    def __init__(self):
        data = dt()
        self.data = data.content()


    def allTypes(self):
        types_counter = {}

        for file_data in self.data:
            #line = sub('\n','',line).lower().replace(' ', '')
            for lines in file_data:
                lines = (sub('\n', '', lines).lower().replace(' ', ''))
                
                for letter in lines:
                    if letter in types_counter:
                        types_counter[letter] += 1
                        continue
                    types_counter[letter] = 1
        print(types_counter)
                


from src.words import Types
from src.graphic import bar

class main:
    def __init__(self) -> None:
        self.word = []
        self.count = []

        self.words = Types()
        
        
        # Se puede usar la siguiente linea para contar las palabras dadas
        #self.words_count = self.words.onlyWords()
        
        
        self.words_count = self.words.allTypes()

        for key, value in self.words_count.items():
            self.word.append(key)
            self.count.append(value)

        bar(self.word, self.count)

main()
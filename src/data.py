import os

class data:

    def __init__(self) -> None:
        self.cwd = os.getcwd()
        self.filesDirectory = f'{self.cwd}/data'
        self.files = os.listdir(self.filesDirectory)


    def read_content(self) -> list[str]:
        for file in self.files:
            with open(f'{self.filesDirectory}/{file}') as f:
                self.content = f.readlines()
                f.close()

        return self.content


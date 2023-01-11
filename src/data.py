import os


class data:

    def __init__(self) -> None:
        self.dataContent = []

        self.cwd = os.getcwd()

        # Path donde estan los archivos por leer
        self.filesDirectory = f'{self.cwd}/data'

        # Archivos listados
        self.files = os.listdir(self.filesDirectory)


    def content(self) -> list[str]:

        # Recorremos los nombres de los archivos dados por self.files
        for file in self.files:
            # Entramos al directorio donde estan los archivos para poder leerlos
            with open(f'{self.filesDirectory}/{file}') as f:
                self.dataContent.append(f.readlines())
                f.close()

        return self.dataContent


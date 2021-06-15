import os
import datetime


class Logger:

    def __init__(self, verbosity: int, save: bool = False, save_path: str = os.getcwd() + "\\logs\\"):
        self.__verbosity = verbosity
        self.__save = save
        self.__creation = datetime.datetime.today()
        self.__savePath = save_path
        self.__data = list()
        self.__logName = datetime.datetime.today()

        self.__credits = ["##########################################",
                          "# Convert Xls files into Csv             #",
                          f"# Log         {self.__logName} #",
                          "# @FunkyoEnma 2021                       #",
                          "# https://linktr.ee/FunkyoEnma           #",
                          "##########################################\n"]

        for i in self.__credits:
            print(i)
            self.__data.append(i)

    def changeVerbosity(self, verbosity):
        self.log(f"Vervosity changed from {self.__verbosity} to {verbosity}", 2)
        self.__verbosity = int(verbosity)

    @property
    def isSaving(self):
        return self.__save

    def setSaving(self, value):
        if self.isSaving != value:
            self.changSaving()

    def changSaving(self):
        self.log(f"El guardado del log ha sido {'Activado' if not self.__save else 'Desactivado'}"
                 f"{f' y sera guardado en {self.__savePath} al finalizar el programa' if not self.__save else ''}", 2)
        self.__save = not self.__save

    def log(self, data: str, log_verbosity: int):
        if log_verbosity <= self.__verbosity:
            line = f"{datetime.datetime.today()}: {data}"
            print(line)
            self.__data.append(line)

    def changeSavePath(self, path):
        self.log(f"La ruta de guardado del log ah cambiado a: {path}", 1)

    def save(self):
        if not os.path.exists(self.__savePath):
            os.mkdir(self.__savePath)

        with open(self.__savePath + str(self.__logName).replace(":", "-").replace(" ", "_").replace(".", "-")
                  + ".log", "w") as file:
            for i in range(len(self.__data)):
                file.write(self.__data[i] + "\n")

        file.close()

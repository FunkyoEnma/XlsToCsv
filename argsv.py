import datetime
from enum import Enum


class Args(Enum):

    input = 0
    output = 1
    save = 2
    savePath = 3
    verbosity = 4


class Confirm:
    from Log import Logger as __Log

    def __init__(self, args: list[str], log: __Log):
        self._log = log
        self._log.log("Argsv check starts", 2)
        self.__argsv = args
        self.__input = ["input", "in", "xls", "i", "entrada"]
        self.__output = ["output", "out", "csv", "o", "salida"]
        self.__save = ["save", "saving", "s", "loggging", "log", "l"]
        self.__savePath = ["savepath", "sp", "logsp", "logsavePath"]
        self.__verbosity = ["verbosity", "verb", "vl", "v", "lv"]

        self.__args = {Args.input.name: "", Args.output.name: "", Args.save.name: "", Args.savePath.name: "",
                       Args.verbosity.name: ""}

        self.__start = datetime.datetime.today()
        self.__checkInput()
        self.__checkOutput()
        self.__checkSave()
        self.__checkSavePath()
        self.__checkVerbosity()
        self.__finishtime = (datetime.datetime.today() - self.__start).total_seconds() * 1000
        self._log.log(f"Check finished in {self.__finishtime} ms", 1)

    def __checkInput(self):
        self._log.log("Checking input", 2)

        for i in self.__argsv:
            arg = i.split("=")[0].replace("-", "")
            if arg in self.__input:
                self._log.log("Input found", 2)
                self._log.log(f"Name '{arg}' and value: {i.split('=')[1]}", 3)
                self.__args[Args.input.name] = i.split("=")[1]
                if i.split("=")[1] == "":
                    raise ValueError("in-01", "Input value is void")
                else:
                    break

        if self.__args[Args.input.name] == "":
            raise ValueError("in-02", "No input provided")

    def __checkOutput(self):
        self._log.log("Checking output", 2)
        for i in self.__argsv:
            arg = i.split("=")[0].replace("-", "")
            if arg in self.__output:
                self._log.log("Output found", 2)
                self._log.log(f"Name '{arg}' and value: {i.split('=')[1]}", 3)
                self.__args[Args.output.name] = i.split("=")[1]
                break

    def __checkSave(self):
        self._log.log("Checking if saving log", 2)
        for i in self.__argsv:
            arg = i.split("=")[0].replace("-", "")
            if arg in self.__save:
                self._log.log("Saving param found", 2)
                self._log.log(f"Name '{arg}' and value: {i.split('=')[1]}", 3)
                self.__args[Args.save.name] = i.split("=")[1]
                break

    def __checkSavePath(self):
        self._log.log("Checking log SavePath", 2)
        for i in self.__argsv:
            arg = i.split("=")[0].replace("-", "")
            if arg in self.__savePath:
                self._log.log("Log SavePath found", 2)
                self._log.log(f"Name '{arg}' and value: {i.split('=')[1]}", 3)
                self.__args[Args.savePath.name] = i.split("=")[1]
                break

    def __checkVerbosity(self):
        self._log.log("Checking Verbosity", 2)
        for i in self.__argsv:
            arg = i.split("=")[0].replace("-", "")
            if arg in self.__verbosity:
                self._log.log("Verbosity found", 2)
                self._log.log(f"Name '{arg}' and value: {i.split('=')[1]}", 3)
                self.__args[Args.verbosity.name] = i.split("=")[1]
                break

    @property
    def all(self):
        return self.__args

    def arg(self, arg: Args):
        return self.__args[arg]

    @property
    def input(self):
        return self.__args[Args.input.name]

    @property
    def output(self):
        return self.__args[Args.output.name]

    @property
    def save(self):
        return self.__args[Args.save.name]

    @property
    def savePath(self):
        return self.__args[Args.savePath.name]

    @property
    def verbosity(self):
        return self.__args[Args.verbosity.name]


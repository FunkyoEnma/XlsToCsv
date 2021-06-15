################################
# Convert Xls files into Csv   #
#                              #
# @FunkyoEnma 2021             #
# https://linktr.ee/FunkyoEnma #
################################
import datetime
import os.path

import xlrd
# Import Excel library
# Formats supported:
#
# 'xls': 'Excel xls'
# 'xlsb': 'Excel 2007 xlsb file',
# 'xlsx': 'Excel xlsx file',
# 'ods': 'Openoffice.org ODS file',
# 'zip': 'Unknown ZIP file',
# None: 'Unknown file type',

import sys
import argsv

# create logger
from Log import Logger

log = Logger(3)


# confirm args
try:
    _args = argsv.Confirm(sys.argv, log).all

except ValueError as e:
    if e.args[0].split("-")[0] == "in":
        raise e


# check if input file exist
# noinspection PyUnboundLocalVariable
if not os.path.isfile(_args[argsv.Args.input.name]):
    raise FileNotFoundError("in-03", "Can't found file")


# define output dir
if _args[argsv.Args.output.name] == "":
    _args[argsv.Args.output.name] = os.getcwd() + "\\output\\"


# save log?
if _args[argsv.Args.save.name] == "True":
    _args[argsv.Args.save.name] = True
else:
    _args[argsv.Args.save.name] = False

log.setSaving(_args[argsv.Args.save.name])

# log savePath
if _args[argsv.Args.savePath.name] == "":
    _args[argsv.Args.savePath.name] = os.getcwd() + "\\logs\\"

log.changeSavePath(_args[argsv.Args.savePath.name])

# log verbosity
if _args[argsv.Args.verbosity.name] == "":
    _args[argsv.Args.verbosity.name] = 1

log.changeVerbosity(_args[argsv.Args.verbosity.name])


class Converter:

    import os

    def __init__(self, xls: str, csv: str):
        """
        Converts an xls file into a csv file

        :param xls: xls filepath
        :param csv: csv desided filepath if none csv file will be created in the current work directory
        """

        #####################################
        # checking for errors in attributes #
        #####################################

        import Errors

        # Check if xls and csv are paths
        Errors.checkPath(xls, "C:\\")

        self.__xls = xls
        self.__csv = csv

        log.log("The program has been initialized", 2)

        # To open Workbook

        log.log(f"An attempt is made to open the file: {self.__xls}", 3)

        wb = xlrd.open_workbook(self.__xls)

        sheet = wb.sheet_by_index(0)

        data = list()

        __convtime = datetime.datetime.today()

        for i in range(sheet.nrows):

            line = ""

            for j in range(sheet.ncols):
                line += f"{sheet.cell_value(i, j)}{'' if j == sheet.ncols - 1 else ','}"

            data.append(line)

        __convtime = (datetime.datetime.today() - __convtime).total_seconds() * 1000

        log.log(f"File converted in: {__convtime}ms", 2)
        log.log("Star saving csv file", 2)

        import os

        if not os.path.exists(self.__csv):
            os.mkdir(self.__csv)

        with open(f"{self.__csv}{os.path.splitext(os.path.basename(self.__xls))[0]}.csv", "w") as file:
            for line in data:
                file.writelines(line + "\n")

            file.close()

        log.log(f"File saved in {file.name}", 2)

        log.save()


Converter(_args[argsv.Args.input.name], _args[argsv.Args.output.name])

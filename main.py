file = r'C:\Users\Comercial\Desktop\abril.xls'

# Reading an excel file using Python
import xlrd

# Give the location of the file

# To open Workbook
wb = xlrd.open_workbook(file)
sheet = wb.sheet_by_index(0)

data = list()

for i in range(sheet.nrows):

    line = ""

    for j in range(sheet.ncols):
        line += f"{sheet.cell_value(i, j)}{'' if j == sheet.ncols - 1 else ','}"

    data.append(line)
    print(line)

with open("data.csv", "w") as file:
    for line in data:
        file.writelines(line + "\n")

    file.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Start('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

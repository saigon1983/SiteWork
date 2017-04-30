# В этом модуле описана функция создания таблицы параметров для каждой ТГ и сохранения этой таблицы в excel-файл
from configobj import ConfigObj
import openpyxl
from openpyxl.styles import Font
from openpyxl.styles.cell_style import CellStyle



def constructParametersTable():
    sourceFile = ConfigObj('DataFolder\\groupsParameters.ini')
    outputFile = openpyxl.Workbook()
    for tg in sourceFile:
        outputFile.create_sheet(tg, -1)
        currentSheet = outputFile.get_sheet_by_name(tg)
        line = 1
        for key in sourceFile[tg]:
            currentSheet['A{}'.format(line)] = key
            currentSheet['A{}'.format(line)].font = currentSheet['A{}'.format(line)].font.copy(bold=True, italic=True)
            line += 1
            if sourceFile[tg][key] == 0 or sourceFile[tg][key] == '0': continue
            if type(sourceFile[tg][key]) == str:
                result = ''
                for value in sourceFile[tg][key]:
                    result += value
                currentSheet['A{}'.format(line)] = sourceFile[tg][key]
                line += 1
            else:
                for value in sourceFile[tg][key]:
                    currentSheet['A{}'.format(line)] = value
                    line += 1
    sheet = outputFile.get_sheet_by_name('Sheet')
    outputFile.remove(sheet)
    outputFile.save('Output\\groups.xlsx')
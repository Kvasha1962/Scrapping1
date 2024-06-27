from openpyxl import Workbook

from ToCSV import (
    list_first_header,
    dict_second_header_new,
    list_third_header,
    list_first_table,
    )

wb = Workbook()
ws = wb.active
ws1 = wb.create_sheet("Гликемический индекс", -1)

list_second_header = [value for value in dict_second_header_new.values()]
print(list_second_header)

ws1.append(list_first_header)
# for column in list_second_header:
ws1.append(list_second_header)
ws1.append(list_third_header)

for row in list_first_table:
    ws1.append(row)

wb.save("Glik.xlsx")
